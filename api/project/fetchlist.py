import requests
import xmltodict
from .database import Database
from .output import outputFailure, outputSuccess


# Request list from GoodReads API
def fetchList(token, list):
    assert isinstance(token, str)
    assert isinstance(list, str)

    warningMessage = []
    sortMethod = "date_read"
    connection = Database()
    grid = connection.getUserID(token)

    # User with token provided is nonexistent in database
    if grid is None:
        return outputFailure(failMessage="User not in database")
    else:
        grid = grid

    url = "https://www.goodreads.com/review/list.xml"
    urlParams = {'key': "MvliPKXB0RGuCSy4wSOdfg", 'v': "2", 'shelf': list, 'sort': sortMethod, 'id': grid}

    # Try requesting API, catch if connection couldn't be opened
    try:
        request = requests.get(url, params=urlParams).text
    except requests.exceptions.RequestException as e:
        # Request could not be made

        return outputFailure(failMessage="Connection to GoodReads could not be made", warningMessage=warningMessage)
    else:
        # Request was made successfully

        # Try parsing XML, catch if data is invalid
        try:
            parsedRequest = xmltodict.parse(request)
        except xmltodict.expat.ExpatError as e:
            # Request was made but the output was not as expected
            return outputFailure(failMessage="GoodReads output corrupted or not authorized",
                                 warningMessage=warningMessage)
        else:
            # Output was XML as expected

            # Catch if API sends error, such as user not existing
            if ("error" in parsedRequest):
                return outputFailure(failMessage=("GoodReads API error: " + parsedRequest["error"]),
                                     warningMessage=warningMessage)

            # Default empty list if user doesn't have anything in list
            response = parsedRequest["GoodreadsResponse"]["reviews"]["review"] if (
                        "review" in parsedRequest["GoodreadsResponse"]["reviews"]) else {}

            # Parse and return goodreads booklist
            results = parseBookList(response, grid=grid, shelf=list, connection=connection, token=token)
            return outputSuccess(results=results, warningMessage=warningMessage, message=token)


# Parse book list into only the useful parts
# This will be made more efficient by getting a list of books for user and comparing each book to that list to see if it exists,
#   rather than querying the database for each book to see if it exists
def parseBookList(bookList, grid, shelf, token, connection):
    parsedList = []
    for book in bookList:
        thisBook = book["book"]
        bookData = {
            "bookid": int(thisBook["id"]["#text"]),
            "title": thisBook["title_without_series"],
            "imageurl": thisBook["image_url"],
            "link": thisBook["link"],
            "pages": int(thisBook["num_pages"]),
            "rating": float(thisBook["average_rating"]),
            "description": thisBook["description"],
            "list": shelf
        }
        connection.cursor.execute(connection.queries["bookExists"], (grid, bookData["bookid"]))
        result = connection.cursor.fetchone()
        if (result is None):
            # Book doesn't already exist in database for user, create one

            connection.cursor.execute(
                connection.queries["createBook"],
                (grid,
                 bookData["title"].encode('utf-8'),
                 bookData["imageurl"].encode('utf-8'),
                 bookData["link"].encode('utf-8'),
                 int(bookData["pages"]),
                 int(bookData["rating"]),
                 bookData["description"].encode('utf-8'),
                 shelf,
                 0,
                 bookData["bookid"],
                 token
                 ))
            bookData["fetched"] = True
        else:
            bookData["pages_read"] = int(result["pages_read"])
            bookData["fetched"] = False

        parsedList.append(bookData)

    connection.close()
    return parsedList
