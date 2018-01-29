from apistar import http
from .fetchList import fetchList
from .Database import Database
from .Output import outputTrue, outputFalse, outputFailure, outputSuccess


# Set reading status of book
def setReadStatus(session: http.Session, pagesread=None, bookid=None):
    if (pagesread is None) or (bookid is None):
        # return {"grid": "Must supply pages read, and book id."}
        return outputFailure(failMessage="Must supply pages read, and book id.")
    try:
        pagesread = int(pagesread)
        bookid = int(bookid)
    except:
        return outputFailure(failMessage="GoodReads ID and book ID must be valid numbers.")

    if "loggedin" in session:
        grid = session["grid"]
        connection = Database()
        connection.setReadStatus(grid=grid, pagesRead=pagesread, bookId=bookid)
        connection.close()
        return outputSuccess()
    else:
        return outputFailure(failMessage="No UID")


#  Get list from the "read" shelf
def getReadList(session: http.Session, sortmethod=None):
    """Call getList with and supply the "read" list and return result"""
    if "loggedin" in session:
        grid = session["grid"]
        return fetchList(grid=grid, list="read", sortMethod=sortmethod)
    else:
        return outputFailure(failMessage="No UID", message="getReadList, not logged in")


# Get list from the "to-read" shelf
def getToReadList(session: http.Session, sortmethod=None):
    """Call getList with and supply the "to-read" list and return result"""
    if "loggedin" in session:
        grid = session["grid"]
        return fetchList(grid=grid, list="to-read", sortMethod=sortmethod)
    else:
        return outputFailure(failMessage="No UID")


# Login user
def logIn(session: http.Session, grid=None):
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
    session["loggedin"] = True
    session["grid"] = grid
    return outputSuccess(results={
        "grid": grid,
        "already_created": already
    })


# Request if user is already logged in
def isLoggedIn(session: http.Session):
    if "loggedin" in session:
        return outputTrue()
    return outputFalse()


# Log user out
def logOut(session: http.Session):
    if "loggedin" in session:
        del session["loggedin"]
        del session["grid"]
        return outputSuccess(message="Logged out.")
    else:
        return outputFailure(failMessage='Not logged in')
