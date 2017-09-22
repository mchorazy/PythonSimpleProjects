from MovieDatabase.DatabaseOperation import databaseConnect, insertMovie
from MovieDatabase.sqlQuery import insertMovieSQL

class databaseMovie:
    def __init__(self):
        databaseConnect()

    def addMovie(self, moviename):
        self.moviename = moviename
        insertMovie(insertMovieSQL(), moviename)


    def printDatabase(self):
        return self.databaseMovie

    def deleteMovie(self, movie):
        if movie in self.databaseMovie:
            del self.databaseMovie[movie]
        else:
            print("Movie not found!")

#if __name__ == "__main__":