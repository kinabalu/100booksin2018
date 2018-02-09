from .fetchlist import fetchList
from .database import Database
from .output import outputTrue, outputFalse, outputFailure, outputSuccess
import requests


# Get list of books on a shelf
def getList(token=None, listName=None):
    if (token is None) or (listName is None):
        return outputFailure(failMessage="Must provide user token and list")

    if (listName == "read") or (listName == "to-read"):
        return fetchList(token, listName)
    else:
        return outputFailure(failMessage="List name invalid")


# Set how many pages of a book have been read
def setReadStatus(pagesread=None, bookid=None, token=None):
    if (pagesread is None) or (bookid is None) or (token is None):
        return outputFailure(failMessage="Must supply pages read, GoodReads ID, and book id.")

    if not isinstance(pagesread, int):
        try:
            pagesread = int(pagesread)
        except:
            return outputFailure(failMessage="Pages read("+pagesread+") must be valid number.")
    if not isinstance(bookid, int):
        try:
            bookid = int(bookid)
        except:
            return outputFailure(failMessage="Book ID("+bookid+") must be a valid number.")

    connection = Database()
    connection.setReadStatus(token=token, pagesRead=pagesread, bookId=bookid)
    connection.close()
    return outputSuccess()


 # Returns token of user. If the user doesn't already exist in database, creates a new user/token
def logIn(grid=None):
    if grid is None:
        return outputFailure(failMessage="Must supply GoodReads ID")
    try:
        grid = int(grid)
    except:
        return outputFailure(failMessage="GoodReads ID must be valid number.")

    connection = Database()
    if connection.userExists(grid=grid) is False:
        # User does not exist already, create it
        token = connection.createUser(grid=grid)
    else:
        # User exists, assign it a new token
        token = connection.newToken(grid)
    connection.close()

    return outputSuccess(results={
        "token": token
    })


# Returns True if a token is a valid user in database, False if not
def tokenValid(token=None):
    if token is None:
        return outputFailure(failMessage="Requires token. ")

    connection = Database()
    if (connection.tokenValid(token)):
        return outputTrue()
    return outputFalse()


# Returns pages read of book for user -- for test purposes
def _testPagesRead(token, bookid):
    connection = Database()
    return outputSuccess(results=connection._testPagesRead(token, bookid))
