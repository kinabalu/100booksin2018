import requests
import xmltodict




# Consistent error output
def failOutput(failMessage=None, warningMessage=None):
    return {
        "fail": True,
        "failMessage": failMessage,
        "warningMessage": warningMessage
    }




# Request list from GoodReads API
# Arguments: getReadList( int userId, str list, str sortMethod )
def getList(userId=None, list=None, sortMethod=None):
    fail, failMessage, warningMessage = False, [], []
    url = "https://www.goodreads.com/review/list.xml"
    urlParams = {
        "key": "MvliPKXB0RGuCSy4wSOdfg",
        "v": "2",
        "shelf": list,
        "sort": sortMethod,
        "id": userId
    }

    # Data validation
    if userId is None:
        fail = True
        failMessage = failMessage + ["No user ID provided", ]
    else:
        try:
            userId = int(userId)
        except:
            fail = True
            failMessage = failMessage + ["User ID invalid", ]
    if sortMethod is None:
        sortMethod = "date_read"
        warningMessage = warningMessage + ['No sort specified, default to date_read', ]
    if list is None:
        fail = True
        failMessage = failMessage + ["Internal error; list not specified", ]

    # Output failue message if data is invalid
    if fail is True:
        return failOutput(failMessage, warningMessage)

    # Try requesting API, catch if connection couldn't be opened
    try:
        request = requests.get(url, params=urlParams).text
    except requests.exceptions.RequestException as e:
        fail = True
        failMessage = failMessage + ["Connection to GoodReads could not be made", ]
        return failOutput(failMessage, warningMessage)
    else:
        # Try parsing XML, catch if data is invalid
        try:
            parsedRequest = xmltodict.parse(request)
        except xmltodict.expat.ExpatError as e:
            fail = True
            failMessage = failMessage + ["GoodReads output corrupted or not authorized", ]
            return failOutput(failMessage, warningMessage)
        else:

            # Catch if user doesn't exist
            if("error" in parsedRequest):
                fail = True
                failMessage = failMessage + ["GoodReads API error: "+parsedRequest["error"], ]
                return failOutput(failMessage, warningMessage)

            # Default empty list if user doesn't have anything in list
            response = {}
            if("review" in parsedRequest["GoodreadsResponse"]["reviews"]):
                response = parsedRequest["GoodreadsResponse"]["reviews"]["review"]

            return {
                "fail": False,
                "warningMessage": warningMessage,
                "length": int(parsedRequest["GoodreadsResponse"]["reviews"]["@total"]),
                "sortMethod": sortMethod,
                "list": list,
                "userId": userId,
                "response": response
            }


