import psycopg2
from apistar import typesystem




# Database operations wrapper with built in statements
class Database(object):
    database = "books"
    host = "172.17.0.2"
    user = "postgres"
    password = "police_lama"
    bookCountList = [5, 10, 15, 20, 25, 30, 35]

    queries = {}

    connection = None
    def __init__(self):
        self.connection = psycopg2.connect(database=self.database, host=self.host, user=self.user, password=self.password)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM users;")
        return self.cursor.fetchall()

    def userExists(self, grid: typesystem.Integer=None):
        if(grid is None):
            return false
        grid = int(str(grid))
        self.cursor.execute("SELECT grid FROM users WHERE grid = %s", (grid, ))
        return self.cursor.fetchone() # is not None -- to return boolean if user exists


    def createUser(self, grid: typesystem.Integer=None):
        if (grid is None):
            return {"message": "Not all data provided to internal createUser function call"}

        userExists = self.userExists(grid)
        if(userExists is not None):
            # User exists already
            return {"message":"User already exists"}
        #self.cursor.execute("INSERT INTO users ( grid ) VALUES ( %s )", ( grid, ))
        return {"message":"End"}
