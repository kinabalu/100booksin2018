from apistar.test import TestClient
from project.views import getReadList, getToReadList


def test_getReadList():
    # Test getReadList view directly
    # -----------------
    # Test that providing nothing results in error
    test2 = getReadList()
    assert test2["fail"] == True

    # Test that not providing userId results in an error
    test1 = getReadList(bookCount=7, sortmethod="date_read")
    assert test1["fail"] == True
    assert test1["failMessage"] == ["No user ID provided", ]
    # Test that providing invalid userId results in an error
    test1 = getReadList(userId="hunter2", bookCount=7, sortmethod="date_read")
    assert test1["fail"] == True
    assert test1["failMessage"] == ["User ID invalid", ]

    # Test that not providing book count results in a warning, and no error
    test1 = getReadList(userId=76836596, sortmethod="date_read")
    assert test1["fail"] == False
    assert test1["warningMessage"] == ["Book count not provided, default of 5 used", ]

    # Test that not providing sort method results in a warning, and no error
    test3 = getReadList(userId=76836596, bookCount="7")
    assert test3["fail"] == False
    assert test3["warningMessage"] == ['No sort specified, default to date_read', ]

    # Test that not providing sort method or book counts results in two warnings, but no error
    # Book count should default to 5, sort method should default to date_read
    test4 = getReadList(userId=76836596)
    assert test4["fail"] == False
    assert test4["bookCount"] == 5
    assert test4["sortMethod"] == "date_read"
    assert test4["warningMessage"] == ['No sort specified, default to date_read', 'Book count not provided, default of 5 used']

    # Test that providing all data does not result in any errors or warnings, and that data is accurate
    test5 = getReadList(userId=76836596, bookCount="7", sortmethod="date_read")
    assert test5["fail"] == False
    assert test5["userId"] == 76836596
    assert test5["bookCount"] == 7
    assert test5["sortMethod"] == "date_read"
    assert test5["warningMessage"] == []



def test_getToReadList():
    # Test getToReadList view directly
    #-----------------
    # Test that providing nothing results in error
    test2 = getToReadList()
    assert test2["fail"] == True

    # Test that not providing userId results in an error
    test1 = getToReadList(bookCount=7, sortmethod="date_read")
    assert test1["fail"] == True
    assert test1["failMessage"] == ["No user ID provided", ]

    # Test that providing invalid userId results in an error
    test1 = getToReadList(userId="hunter2", bookCount=7, sortmethod="date_read")
    assert test1["fail"] == True
    assert test1["failMessage"] == ["User ID invalid", ]

    # Test that not providing book count results in a warning, and no error
    test1 = getToReadList(userId=76836596, sortmethod="date_read")
    assert test1["fail"] == False
    assert test1["warningMessage"] == ["Book count not provided, default of 5 used", ]

    # Test that not providing sort method results in a warning, and no error
    test3 = getToReadList(userId=76836596, bookCount="7")
    assert test3["fail"] == False
    assert test3["warningMessage"] == ['No sort specified, default to date_read', ]

    # Test that not providing sort method or book counts results in two warnings, but no error
    # Book count should default to 5, sort method should default to date_read
    test4 = getToReadList(userId=76836596)
    assert test4["fail"] == False
    assert test4["bookCount"] == 5
    assert test4["sortMethod"] == "date_read"
    assert test4["warningMessage"] == ['No sort specified, default to date_read', 'Book count not provided, default of 5 used']

    # Test that providing all data does not result in any errors or warnings, and that data is accurate
    test5 = getToReadList(userId=76836596, bookCount="7", sortmethod="date_read")
    assert test5["fail"] == False
    assert test5["userId"] == 76836596
    assert test5["bookCount"] == 7
    assert test5["sortMethod"] == "date_read"
    assert test5["warningMessage"] == []