from apistar.test import TestClient
from app import app


def _getClientData(url=None):
    client = TestClient(app)
    response = client.get(url)
    return response.json()


def test_getClientData():
    test1 = _getClientData("/asdasdasd")
    assert test1 == {"message":"Not found"}


def test_app():
    # Test that requesting a shelf without using correct key results in error
    test1 = _getClientData("/shelf/19872/read")
    assert test1["fail"] == True


    # Test that requesting shelf with invalid list results in error
    test2 = _getClientData("/shelf/19872/recently_added")
    assert test2["fail"] == True


    # Test that logging in with an invalid goodreads id results in error
    test3 = _getClientData("/user/asd/")
    assert test3["fail"] == True


    # Test that logging in with a valid goodreads id does not result in an error, and that it returns a token
    test4 = _getClientData("/user/76836596/")
    assert test4["fail"] == False
    assert "result" in test4
    assert "token" in test4["result"]
    # Save this token for later tests
    userToken = test4["result"]["token"]


    # Test that checking if an invalid is valid token returns false, but not an error
    test5 = _getClientData("/token/asd/")
    assert test5["result"] == False
    assert test5["fail"] == False


    # Test that checking if a valid token is valid returns true, and no error
    test6 = _getClientData("/token/" + userToken)
    assert test6["result"] == True
    assert test6["fail"] == False


    # Test that requesting shelf with valid user token, but invalid list, results in error
    test7 = _getClientData("/shelf/" + userToken + "/recently_added")
    assert test7["fail"] == True


    # Test that requesting shelf with valid user token, and valid list, results in no error, and that the result is a list containing dictionaries
    test8 = _getClientData("/shelf/" + userToken + "/read")
    assert test8["fail"] == False
    assert "result" in test8
    assert isinstance(test8["result"], list)
    assert isinstance(test8["result"][0], dict)
    # Save this book list for later tests
    userBooksFirstBookBookid = test8["result"][0]["bookid"]


    # Test that updating pages read for a book with invalid number results in an error, and that the pages read has not been updated
    test8Value = "invalid_number"
    test8Url = "/pagesread/" + str(userToken) + "/" + str(userBooksFirstBookBookid) + "/" + test8Value
    test8 = _getClientData(test8Url)
    assert test8["fail"] == True
    test8Check = _getClientData("/testpagesread/" + str(userToken) + "/" + str(userBooksFirstBookBookid))
    assert test8Check["result"] != test8Value
    # Save the actual pages read for later, so we can set it back
    userBookPagesRead = test8Check["result"][0]


    # Test that updating pages read for a book with a valid number results in an no error, and that the pages read has been updated
    test9Value = 94
    test9Url = "/pagesread/" + str(userToken) + "/" + str(userBooksFirstBookBookid) + "/" + str(test9Value)
    test9 = _getClientData(test9Url)
    assert test9["fail"] == False
    test9Check = _getClientData("/testpagesread/" + str(userToken) + "/" + str(userBooksFirstBookBookid))
    assert test9Check["result"][0] == test9Value


    # Set the pages read back to original-------------------------------------------------------------------------------
    reset = _getClientData("/pagesread/" + str(userToken) + "/" + str(userBooksFirstBookBookid) + "/" + str(userBookPagesRead))
    assert reset["fail"] == False
