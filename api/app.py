from apistar import Route
from apistar.frameworks.wsgi import WSGIApp as App
from project.views import setReadStatus, getList, logIn, tokenValid, _testPagesRead

routes = [
    # Get shelf lists
    Route("/shelf/{token}/{listName}/", "GET", getList),

    # Check user into database -- will be POST
    Route("/user/{grid}/", "GET", logIn),

    # Check if token is valid
    Route("/token/{token}/", "GET", tokenValid),

    # Update pages read for specific book
    Route('/pagesread/{token}/{bookid}/{pagesread}/', 'GET', setReadStatus),

    # Check pages read of book, for testing purposes
    Route('/testpagesread/{token}/{bookid}/', 'GET', _testPagesRead),
]

app = App(routes=routes)

# ------------------#
# To-do
# ------------------#
#   -Write thorough unit testings
