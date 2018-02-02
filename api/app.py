from apistar import Route
from apistar.frameworks.wsgi import WSGIApp as App
from project.views import setReadStatus, getList, logIn, tokenValid

routes = [
    # Get shelf lists
    Route("/shelf/{token}/{listName}/", "GET", getList),

    # Check user into database -- will be POST
    Route("/user/{grid}/", "GET", logIn),

    # Check if token is valid
    Route("/token/{token}/", "GET", tokenValid),

    # Update pages read for specific book
    Route('/pagesread/{token}/{bookid}/{pagesread}/', 'GET', setReadStatus)
]

app = App(routes=routes)

# ------------------#
# To-do
# ------------------#
#   -Write thorough unit testings
