from .getList import getList

def getReadList(userId=None, bookCount=None, sortMethod=None):
    return getList(userId, bookCount, "read", sortMethod)


def getToReadList(userId=None, bookCount=None, sortMethod=None):
    return getList(userId, bookCount, "to-read", sortMethod)
