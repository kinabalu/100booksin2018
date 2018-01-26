from .getList import getList
from .Database import Database
from apistar import http, typesystem

# Type to Force Int - instead of typing typesystem.Integer
class FInt(typesystem.Integer):
    pass




# Get list from the "read" shelf
def getReadList(session: http.Session, sortMethod=None):
    """Call getList with and supply the "read" list and return result"""
    if("loggedin" in session):
        grid = session["grid"]
        return getList(userId=grid, list="read", sortMethod=sortMethod)
    else:
        return {"message":"No UID"}




# Get list from the "to-read" shelf
def getToReadList(session: http.Session, sortMethod=None):
    """Call getList with and supply the "to-read" list and return result"""
    if ("loggedin" in session):
        grid = session["grid"]
        return getList(userId=grid, list="to-read", sortMethod=sortMethod)
    else:
        return {"message": "No UID"}




# Login user
def logIn(session: http.Session, grid: FInt=None):
    if(grid is None):
        return {"grid":"Must be a valid number."}

    already = True

    connection = Database()
    if(not connection.userExists(grid)):
        connection.createUser(grid=grid)
        already = False

    session["loggedin"] = True
    session["grid"] = grid
    return {"result":True, "grid":grid, "already_created":already}




# Request if user is already logged in
def isLoggedIn(session: http.Session):
    if ("loggedin" in session):
        return True
    return False
