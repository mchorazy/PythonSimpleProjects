def insertMovieSQL():
    return "INSERT INTO movies(movie_name) VALUES(%s)"

def updatedMovieSQL():
    return """UPDATED movies
            SET movie_name = %s
            WHERE movie_id = %s"""

def getMovieListSQL():
    return "SELECT movie_id, movie_name FROM movies ORDER BY movie_name"

def getMoviesNameSQL():
    return "SELECT movie_name FROM movies ORDER BY movie_name"

def deleteMovieSQL():
    return "DELETE FROM movies WHERE movie_name = %s"