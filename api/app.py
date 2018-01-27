from apistar import http, Route
from apistar.frameworks.wsgi import WSGIApp as App
from project.views import getReadList, getToReadList, logIn, isLoggedIn, setReadStatus, logOut

routes = [
    # Get lists
    Route('/getread', 'GET', getReadList),
    Route('/gettoread', 'GET', getToReadList),

    # Test if user is already logged in
    Route('/isloggedin', 'GET', isLoggedIn),

    # "Log in" - Start session for user, insert into db if not already existent
    # Only GET for testing, will be POST
    Route('/login', 'GET', logIn),

    # "Log out" end session - frontend will prompt for credentials again after this
    Route('/logout', 'GET', logOut),

    # Update pages read for specific book
    Route('/pagesread', 'GET', setReadStatus)
]

app = App(routes=routes)

# ------------------#
# To-do
# ------------------#
#   -Write thorough unit testing
#
# Flow:
#   -> Client requests GET:/loggedin
#   --> If api returns true, client then requests GET:/getread or /gettoread
#   --> If api returns false, client prompts user for GoodReads id, and uses POST:/login to log user in and create session
