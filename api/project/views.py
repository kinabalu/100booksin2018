import requests
import xmltodict



def getList(userId=None, bookCount=None, list=None, sortMethod=None):
    fail, failMessage, warningMessage = False, [], []

    def failOutput(failMessage=None, warningMessage=None):
        return {
            "fail": True,
            "failMessage": failMessage,
            "warningMessage": warningMessage
        }

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
    if bookCount is None:
        bookCount = 5
        warningMessage = warningMessage + ["Book count not provided, default of 5 used", ]
    else:
        try:
            bookCount = int(bookCount)
        except:
            bookCount = 5
            warningMessage = warningMessage + ["Book count invalid, default of 5 used", ]
    if list is None:
        fail = True
        failMessage = failMessage + ["Internal error; list not specified", ]

    if fail is True:
        return failOutput(failMessage, warningMessage)

    url = "https://www.goodreads.com/review/list.xml"
    urlParams = {
        "key": "MvliPKXB0RGuCSy4wSOdfg",
        "v": "2",
        "shelf": list,
        "sort": sortMethod,
        "id": userId
    }
    try:
        request = requests.get(url, params=urlParams).text
    except requests.exceptions.RequestException as e:
        fail = True
        failMessage = failMessage + ["Connection to GoodReads could not be made", ]
        return failOutput(failMessage, warningMessage)
    else:
        try:
            parsedRequest = xmltodict.parse(request)
        except xmltodict.expat.ExpatError as e:
            fail = True
            failMessage = failMessage + ["GoodReads output corrupted or not authorized", ]
            return failOutput(failMessage, warningMessage)
        else:
            return {
                "fail": False,
                "warningMessage": warningMessage,
                "length": parsedRequest["GoodreadsResponse"]["reviews"]["@total"],
                "bookCount": bookCount,
                "sortMethod": sortMethod,
                "list": list,
                "userId": userId,
                "books": parsedRequest["GoodreadsResponse"]["reviews"]["review"]
            }


# example: getReadList(userId="76836596", bookCount=None, sort="date_read")
def getReadList(userId=None, bookCount=None, sortMethod=None):
    return getList(userId, bookCount, "read", sortMethod)


def getToReadList(userId=None, bookCount=None, sortMethod=None):
    return getList(userId, bookCount, "to-read", sortMethod)
