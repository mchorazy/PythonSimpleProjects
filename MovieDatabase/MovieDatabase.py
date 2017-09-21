import psycopg2
from Config import config

class databaseMovie:
    def __init__(self):
        self.databaseMovie = {}

    def addMovie(self, movie, details=[]):
        self._movie = movie
        self._details = details
        self.databaseMovie[self._movie] = self._details

    def printDatabase(self):
        return self.databaseMovie

    def deleteMovie(self, movie):
        if movie in self.databaseMovie:
            del self.databaseMovie[movie]
        else:
            print("Movie not found!")

def createDatabase():
    conn = psycopg2.connect("dbname=movies user=movie password=database")

if __name__ == "__main__":
    movieDB = databaseMovie()
    movieDB.addMovie('Gladiator', [1980,'Ridley','Drama'])
    movieDB.addMovie('Batman', [1999, 'john', 'Scif-fi'])
    print(movieDB.printDatabase())