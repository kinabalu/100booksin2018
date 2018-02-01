from apistar import http
from .fetchList import fetchList
from .Database import Database
from .Output import outputTrue, outputFalse, outputFailure, outputSuccess


# Set reading status of book
def setReadStatus(pagesread=None, bookid=None, grid=None):
    if (pagesread is None) or (bookid is None) or (grid is None):
        # return {"grid": "Must supply pages read, and book id."}
        return outputFailure(failMessage="Must supply pages read, GoodReads ID, and book id.")
    try:
        pagesread = int(pagesread)
        bookid = int(bookid)
    except:
        return outputFailure(failMessage="GoodReads ID and book ID must be valid numbers.")

    connection = Database()
    connection.setReadStatus(grid=grid, pagesRead=pagesread, bookId=bookid)
    connection.close()
    return outputSuccess()


#  Get list from the "read" shelf
def getReadList(sortmethod=None, grid=None):
    """Call getList with and supply the "read" list and return result"""
    if(isinstance(grid, str)):
        try:
            grid = int(grid)
        except:
            return outputFailure(failMessage="GoodReads ID must be valid integer")
    return fetchList(grid=grid, list="read", sortMethod=sortmethod)


# Get list from the "to-read" shelf
def getToReadList(sortmethod=None, grid=None):
    """Call getList with and supply the "to-read" list and return result"""
    if (isinstance(grid, str)):
        try:
            grid = int(grid)
        except:
            return outputFailure(failMessage="GoodReads ID must be valid integer")
    return fetchList(grid=grid, list="to-read", sortMethod=sortmethod)


# Login user
def logIn(grid=None):
    if grid is None:
        return outputFailure(failMessage="Must supply GoodReads ID")

    try:
        grid = int(grid)
    except:
        return outputFailure(failMessage="GoodReads ID must be valid number.")

    already = True

    connection = Database()
    if connection.userExists(grid=grid) is False:
        already = False
        if (not connection.createUser(grid=grid)):
            return outputFailure(failMessage="Failed to create user")
    connection.close()
    return outputSuccess(results={
        "grid": grid,
        "already_created": already
    })
