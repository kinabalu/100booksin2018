import psycopg2
import psycopg2.extras


# Database operations wrapper with built in statements
class Database(object):
    database = 'books'
    host = '172.17.0.3'
    user = 'postgres'
    password = 'police_lama'
    bookCountList = [5, 10, 15, 20, 25, 30, 35]
    queries = {
        "userExists": 'SELECT grid FROM users WHERE grid = %s',
        "createUser": 'INSERT INTO users ( grid ) VALUES ( %s )',
        "setReadStatus": 'UPDATE books SET pages_read = %s WHERE bookid = %s AND grid = %s'
    }
    connection = None

    def __init__(self):
        self.connection = psycopg2.connect(database=self.database, host=self.host, user=self.user,
                                           password=self.password)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def userExists(self, grid):
        assert isinstance(grid, int)

        grid = int(str(grid))
        self.cursor.execute(self.queries["userExists"], (grid,))
        fetch = self.cursor.fetchone()
        if fetch is None:
            return False
        else:
            return True

    def createUser(self, grid):
        assert isinstance(grid, int)
        try:
            self.cursor.execute(self.queries["createUser"], (grid,))
        except:
            return False

        return True

    def setReadStatus(self, grid=None, bookId=None, pagesRead=None):
        assert isinstance(grid, int)
        assert isinstance(bookId, int)
        assert isinstance(pagesRead, int)

        self.cursor.execute(self.queries["setReadStatus"],
                            (pagesRead, bookId, grid))
    def close(self):
        self.connection.close()