from apistar import http, Route
from apistar.frameworks.wsgi import WSGIApp as App
from project.views import getReadList, getToReadList, logIn, setReadStatus

routes = [
    # Get lists
    Route('/getread', 'GET', getReadList),
    Route('/gettoread', 'GET', getToReadList),

    # Old methods relying on session
    #Route('/isloggedin', 'GET', isLoggedIn),
    #Route('/login', 'GET', logIn),
    #Route('/logout', 'GET', logOut),

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
