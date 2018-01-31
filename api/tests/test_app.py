from apistar.test import TestClient
from app import app


def _getClientData(url=None):
    if (url is not None):
        client = TestClient(app)
        response = client.get(url)
        return response.json()
    return True


def test_GetLists():
    # Test that requesting "read" list without logging in results in error
    test1 = _getClientData("/getread")
    assert test1["fail"] == True

    # Test that requesting "to-read" list without logging in results in error
    test2 = _getClientData("/gettoread")
    assert test2["fail"] == True


def test_login(url=None):
    # Test that logging in without UID results in error
    test3 = _getClientData("/login")
    assert test3["fail"] == True
    assert test3["failMessage"] == "Must supply GoodReads ID"

    # Test that logging in with invalid UID results in error
    test4 = _getClientData("/login?grid=asdasd")
    assert test4["fail"] == True
    assert test4["failMessage"] == "GoodReads ID must be valid number."

    # Test that logging in with valid UID results in no error
    test5 = _getClientData("/login?grid=234567")
    assert test5["fail"] == False

# Test that getting list "read" works now that user is logged in
# --- Can't get sessions working with TestClient
