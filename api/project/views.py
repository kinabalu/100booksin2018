from .fetchlist import fetchList
from .database import Database
from .output import outputTrue, outputFalse, outputFailure, outputSuccess


def getList(token=None, listName=None):
    # Get list of books on a shelf

    if (token is None) or (listName is None):
        return outputFailure(failMessage="Must provide user token and list")

    if (listName == "read"):
        return fetchList(token=token, list="read")
    elif (listName == "to-read"):
        return fetchList(token=token, list="to-read")
    else:
        return outputFailure(failMessage="List name invalid")


def setReadStatus(pagesread=None, bookid=None, token=None):
    # Set how many pages of a book have been read

    if (pagesread is None) or (bookid is None) or (token is None):
        return outputFailure(failMessage="Must supply pages read, GoodReads ID, and book id.")
    try:
        pagesread = int(pagesread)
        bookid = int(bookid)
    except:
        return outputFailure(failMessage="GoodReads ID and book ID must be valid numbers.")

    connection = Database()
    connection.setReadStatus(token=token, pagesRead=pagesread, bookId=bookid)
    connection.close()
    return outputSuccess()


def logIn(grid=None):
    # Returns token of user. If the user doesn't already exist in database, creates a new user/token

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


def tokenValid(token=None):
    # Returns True if a token is a valid user in database, False if not

    if token is None:
        return outputFailure(failMessage="Requires token. ")

    connection = Database()
    if (connection.tokenValid(token)):
        return outputTrue()
    return outputFalse()
