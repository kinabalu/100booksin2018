from apistar import Route
from apistar.frameworks.wsgi import WSGIApp as App
from project.views import setReadStatus, getList, logIn, tokenValid, _testPagesRead
from wsgicors import CORS

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

class CORSApp(App):
    def __call__(self, environ, start_response):
        cors = CORS(super().__call__, headers='*', methods='*', maxage='180', origin='*')
        return cors(environ, start_response)



app = CORSApp(routes=routes)
#app = App(routes=routes)