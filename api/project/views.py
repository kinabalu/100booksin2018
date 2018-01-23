from .getList import getList

# Get list from the "read" shelf
# Arguments: getReadList( int userId, int bookCount=5, str sortMethod="date_read" )
#   int userId      : GoodReads user ID
#   int bookCount   : How many books to list. Defaults to 5 with warning
#   str sortMethod  : Sorting method to us. full documentation of options is available on GoodReads API documentation. Defaults to "date_read" with warning
# See getList for output
def getReadList(userId=None, bookCount=None, sortMethod=None):
    """Call getList with and supply the "read" list and return result"""
    return getList(userId, bookCount, "read", sortMethod)


# Get list from the "to-read" shelf
# Arguments: getReadList( int userId, int bookCount=5, str sortMethod="date_read" )
#   int userId      : GoodReads user ID
#   int bookCount   : How many books to list. Defaults to 5 with warning
#   str sortMethod  : Sorting method to us. full documentation of options is available on GoodReads API documentation. Defaults to "date_read" with warning
# See getList for output
def getToReadList(userId=None, bookCount=None, sortMethod=None):
    """Call getList with and supply the "to-read" list and return result"""
    return getList(userId, bookCount, "to-read", sortMethod)
