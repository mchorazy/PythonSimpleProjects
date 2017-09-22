from MovieDatabase.DatabaseOperation import databaseConnect, executeSql
from MovieDatabase.sqlQuery import insertMovie

class databaseMovie:
    def __init__(self):
        databaseConnect()

    def addMovie(self, moviename):
        self.moviename = moviename
        executeSql(insertMovie(), moviename)


    def printDatabase(self):
        return self.databaseMovie

    def deleteMovie(self, movie):
        if movie in self.databaseMovie:
            del self.databaseMovie[movie]
        else:
            print("Movie not found!")

#if __name__ == "__main__":