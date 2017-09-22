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

        for query in createTables():
            cursor.execute(query)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()

def executeSql(sqlQuery, moviename):
    connection = None
    movie_id = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(sqlQuery, (moviename,))
        movie_id = cursor.fetchone()[0]

        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as errorDescription:
        print('Error description:\n', errorDescription)
    finally:
        if connection is not None:
            connection.close()
    return movie_id