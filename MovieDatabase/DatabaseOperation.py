import psycopg2
from MovieDatabase.Config import config

def createTables():
    """Create tables in database"""
    sqlQuery = (
        """
        CREATE TABLE movies (
            movie_id SERIAL PRIMARY KEY
            movie_name VARCHAR(255) NOT NULL
        )
        """
    )
    return sqlQuery

def databaseConnect():
    """Create connection with database
    Using configuration from Config.py"""
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        """for query in createTables():
            cursor.execute(query)"""
        [cursor.execute(query) for query in createTables()]

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()

def insertMovie(sqlQuery, movie_name):
    """Insert movie in database"""
    connection = None
    movie_id = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(sqlQuery, (movie_name,))
        movie_id = cursor.fetchone()[0]

        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()
    return movie_id

def updateMovie(sqlQuery, movie_id, movie_name):
    """Update movie record"""
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(sqlQuery, (movie_name, movie_id))
        result = cursor.rowcount

        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()
    return result

def printMovies(sqlQuery):
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        """for movie in rows:
            print(movie)"""
        [print(movie) for movie in rows]

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()

def getMoviesList(sqlQuery):
    connection = None
    movieList = []
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        """for movie in rows:
            movieList.append(movie)"""
        [movieList.append(movie) for movie in rows]
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()
    return movieList

def deleteMovie(sqlQuery, movie_name):
    connection = None
    deletedmovie = 0
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(sqlQuery, (movie_name,))
        deletedmovie = cursor.rowcount

        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()
    return deletedmovie
