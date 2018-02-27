import psycopg2
import psycopg2.extras
import hashlib
import time


# Database operations wrapper with built in statements
class Database(object):
    database = 'books'
    #host = '172.17.0.4'
    host = '172.18.0.4'
    user = 'postgres'
    password = 'police_lama'
    bookCountList = [5, 10, 15, 20, 25, 30, 35] # Going to do this on the client side actually
    queries = {
        "userExists": 'SELECT grid FROM users WHERE grid = %s',
        "bookExists": "SELECT pages_read FROM books WHERE grid = %s AND bookid = %s",
        "createUser": 'INSERT INTO users ( grid, token ) VALUES ( %s, %s )',
        "setReadStatus": 'UPDATE books SET pages_read = %s WHERE bookid = %s AND grid = %s',
        "setNewToken": 'UPDATE users SET token = %s WHERE grid = %s',
        "userIdByToken": "SELECT grid FROM users WHERE token = %s",
        "userTokenById": "SELECT token FROM users WHERE grid = %s",
        "createBook": "INSERT INTO books ( grid, title, imageurl, link, pages, rating, list, pages_read, bookid ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s )",
        "pagesRead": "SELECT pages_read FROM books WHERE grid = %s AND bookid = %s"
    }
    connection = None

    # Open connection and set to autocommit
    def __init__(self):
        #if(gethostname())

        self.connection = psycopg2.connect(database=self.database, host=self.host, user=self.user,
                                           password=self.password)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Check if a user exists, by goodreads id. True if so, False if not
    def userExists(self, grid):
        assert isinstance(grid, int)

        grid = int(str(grid))
        self.cursor.execute(self.queries["userExists"], (grid,))
        fetch = self.cursor.fetchone()
        if fetch is None:
            return False
        else:
            return True

    # Create a user, using a goodreads id and a token. Returns token of new user
    def createUser(self, grid):
        assert isinstance(grid, int)

        token = self.generateToken(grid)
        self.cursor.execute(self.queries["createUser"], (grid, token))
        return token

    # Set read status of book, with token of user, goodreads bookid, and the number of pages read. True if execution succeeded, False if not
    def setReadStatus(self, token, bookId, pagesRead):
        assert isinstance(token, str)
        assert isinstance(bookId, int)
        assert isinstance(pagesRead, int)

        grid = self.getUserID(token)
        try:
            self.cursor.execute(self.queries["setReadStatus"], (pagesRead, bookId, grid))
        except:
            return False

        return True

    # Close database connection
    def close(self):
        self.connection.close()

    # Return users goodreads id by token
    def getUserID(self, token):
        assert isinstance(token, str)

        self.cursor.execute(self.queries["userIdByToken"], (token,))
        fetch = self.cursor.fetchone();
        if(fetch is None):
            return None
        return str(fetch[0])

    # Return token by goodreads id
    def getToken(self, grid):
        assert isinstance(grid, int)

        self.cursor.execute(self.queries["userTokenById"], (grid,))
        fetch = self.cursor.fetchone();
        if (fetch is None):
            return None
        return fetch[0]

    # Check if token is a valid user, for use by the front end. True if user exists in database, False if not
    def tokenValid(self, token):
        assert isinstance(token, str)

        query = self.getUserID(token)
        return True if (query is not None) else False

    # Generate and return a new unique token
    def generateToken(self, grid):
        assert isinstance(grid, int)

        token = (str(grid) + "|" + str(time.time())).encode('utf-8')
        token = hashlib.md5(token).hexdigest()
        return token

    # Assign a user a new token, returns new token
    def newToken(self, grid):
        assert isinstance(grid, int)

        token = self.generateToken(grid)
        self.cursor.execute(self.queries["setNewToken"], (token, grid))
        return token

    # Return the pages_read value for book - for testing the setting of pages read
    def _testPagesRead(self, token, bookid):
        grid = self.getUserID(token)
        self.cursor.execute(self.queries["pagesRead"], (grid, bookid))
        fetch = self.cursor.fetchone()
        return fetch
