import requests
import urllib.request
import xmltodict
from .database import Database
from .output import outputFailure, outputSuccess



# Request list from GoodReads API
def fetchList(token, list):
    assert isinstance(token, str)
    assert isinstance(list, str)
    warningMessage = []
    connection = Database()
    grid = str(connection.getUserID(token))
    if(grid is None):
        return outputFailure(failMessage="Token incorrect")

    url = "https://www.goodreads.com/review/list.xml"
    # https://www.goodreads.com/review/list.xml?key=MvliPKXB0RGuCSy4wSOdfg&v=2&id=76836596&shelf=read
    urlParams = {
        "key": "MvliPKXB0RGuCSy4wSOdfg",
        "v": 2,
        "id": grid,
        "shelf": list,
    }
    # Try requesting API, catch if connection couldn't be opened
    try:
        request = requests.get(url, params=urlParams)
        request.encoding = "utf8"
        request = request.text

    except requests.exceptions.RequestException as e:
        # Request could not be made

        return outputFailure(failMessage="Connection to GoodReads could not be made: " + str(e), warningMessage=warningMessage)
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
            results = parseBookList(bookList=response, grid=grid, shelf=list, connection=connection, token=token)

            return outputSuccess(results=results, warningMessage=warningMessage, message=token)



# Parse book list into only the useful parts
# This will be made more efficient by getting a list of books for user and comparing each book to that list to see if it exists,
#   rather than querying the database for each book to see if it exists
def parseBookList(bookList, grid, shelf, token, connection):
    parsedList = []
    if(type(bookList) is not list):
        bookList = [bookList, ]


    for single_book in bookList:
        thisBook = single_book["book"]
        bookData = {
            "bookid": int(thisBook["id"]["#text"]),
            "title": thisBook["title_without_series"],
            "imageurl": thisBook["image_url"],
            "link": thisBook["link"],
            "rating": float(thisBook["average_rating"]),
            #"description": thisBook["description"],
            "list": shelf
        }
        if("num_pages" in thisBook and thisBook["num_pages"] is not None):
            bookData["pages"] = int(thisBook["num_pages"])
        else:
            bookData["pages"] = 999

        connection.cursor.execute(connection.queries["bookExists"], (grid, bookData["bookid"]))
        result = connection.cursor.fetchone()
        if (result is None):
            # Book doesn't already exist in database for user, create one

            connection.cursor.execute(
                connection.queries["createBook"],
                (grid,
                 bookData["title"],
                 bookData["imageurl"],
                 bookData["link"],
                 int(bookData["pages"]),
                 int(bookData["rating"]),
                 shelf,
                 0,
                 bookData['bookid'],
                 ))
            bookData["fetched"] = True
        else:
            bookData["pages_read"] = result["pages_read"]
            bookData["fetched"] = False

        parsedList.append(bookData)

    connection.close()
    return parsedList
