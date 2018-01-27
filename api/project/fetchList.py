import requests
import xmltodict
from .Database import Database
from .Output import outputFailure, outputSuccess


def parseBookList(bookList, grid, shelf):
    connection = Database()
    parsedList = {}
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
        connection.cursor.execute("SELECT * FROM books WHERE grid = %s AND bookid = %s", (grid, bookData["bookid"]))
        result = connection.cursor.fetchone()
        if (result is None):
            # book doesn't already exist for user

            connection.cursor.execute(
                "INSERT INTO books ( grid, title, imageurl, link, pages, rating, description, list, pages_read, bookid ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",
                (grid,
                 bookData["title"].encode('utf-8'),
                 bookData["imageurl"].encode('utf-8'),
                 bookData["link"].encode('utf-8'),
                 int(bookData["pages"]),
                 int(bookData["rating"]),
                 bookData["description"].encode('utf-8'),
                 shelf,
                 0,
                 bookData["bookid"]
                 ))
            bookData["fetched"] = True
        else:
            bookData["pages_read"] = int(result["pages_read"])
            bookData["fetched"] = False

        parsedList[thisBook["title_without_series"]] = bookData

    return parsedList


# Request list from GoodReads API
# Arguments: getReadList( int userId, str list, str sortMethod )
def fetchList(userId, list, sortMethod):
    warningMessage = []
    url = "https://www.goodreads.com/review/list.xml"
    urlParams = {'key': "MvliPKXB0RGuCSy4wSOdfg", 'v': "2", 'shelf': list, 'sort': sortMethod, 'id': userId}

    # Try requesting API, catch if connection couldn't be opened
    try:
        request = requests.get(url, params=urlParams).text
    except requests.exceptions.RequestException as e:
        return outputFailure(failMessage="Connection to GoodReads could not be made", warningMessage=warningMessage)
    else:
        # Try parsing XML, catch if data is invalid
        try:
            parsedRequest = xmltodict.parse(request)
        except xmltodict.expat.ExpatError as e:
            return outputFailure(failMessage="GoodReads output corrupted or not authorized",
                                 warningMessage=warningMessage)
        else:
            # Catch if API sends error, such as user not existing
            if ("error" in parsedRequest):
                return outputFailure(failMessage=("GoodReads API error: " + parsedRequest["error"]),
                                     warningMessage=warningMessage)

            # Default empty list if user doesn't have anything in list
            response = {}
            if ("review" in parsedRequest["GoodreadsResponse"]["reviews"]):
                response = parsedRequest["GoodreadsResponse"]["reviews"]["review"]

            re = parseBookList(response, grid=userId, shelf=list)
            return outputSuccess(results=re, warningMessage=warningMessage)
