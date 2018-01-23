import requests
import xmltodict

# Request list from GoodReads API
# Arguments: getReadList( int userId, int bookCount, str list, str sortMethod )
#   int userId      : GoodReads user ID
#   int bookCount   : How many books to list. Defaults to 5 with warning
#   str list        : Which list to
#   str sortMethod  : Sorting method to us. full documentation of options is available on GoodReads API documentation. Defaults to "date_read" with warning
# Output:
# {
#   bool fail           : True if request failed for any reason
#   tup  failMessage    : List of failure messages
#   tup  warningMessages: List of warning messages
#   int  length         : Length of book list from GoodReads API
#   int  bookCount      : Length of output book list
#   str  sortMethod     : Sort method passed to GoodReads API
#   str  list           : Which list was fetched
#   int  userId         : Which user id was passed to GoodReads API
#   dict books          : Raw dictionary of output of list from GoodReads API
# }
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


