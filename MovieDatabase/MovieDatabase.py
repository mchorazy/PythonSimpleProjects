from MovieDatabase.DatabaseOperation import *
from MovieDatabase.sqlQuery import *

class databaseMovie:
    def __init__(self):
        databaseConnect()

    def addMovie(self, moviename):
        self.moviename = moviename
        insertMovie(insertMovieSQL(), moviename)

    def updateMovie(self, movieid, moviename):
        self.movieid = movieid
        self.moviename = moviename
        updateMovie(updatedMovieSQL(),movieid,moviename)

    def printMovieList(self):
        printMovies(getMovieListSQL())

    def deleteMovie(self, moviename):
        if moviename in getMoviesList(getMoviesNameSQL()):
            deleteMovie(deleteMovieSQL(), moviename)
        else:
            print("Movie not found!")
