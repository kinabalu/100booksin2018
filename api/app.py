from apistar import http, Route
from apistar.frameworks.wsgi import WSGIApp as App
from project.views import getReadList, getToReadList, logIn, isLoggedIn

routes = [
    # Get lists
    Route('/getread', 'GET', getReadList),
    Route('/gettoread', 'GET', getToReadList),

    # Test if user is already logged in
    Route('/isloggedin', 'GET', isLoggedIn),

    # "Log in" - Start session for user, insert into db if not already existent
    Route('/login', 'GET', logIn),
]

app = App(routes=routes)

#------------------#
# To-do
#------------------#
#   -Make output consistent
#   -Validate that user id is a valid user before creating row and session
#   -Store book information on database
#       -Populate books in database on new user login
#       -List of books in shelf should only be requested from GoodReads after a certain time since last refresh, not every time client fetches
#   -Create book list parsing function to parse a cleaner list of books, and add reading statistics
#   -Make methods to set book reading status