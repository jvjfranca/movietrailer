from media import Movies

# List to add movie objects
movie_list = []


# Function to add movies to the movie_list
def add_movies(movie_list, movie):
    movie_list.append(movie)


# Instantiating movie
star_wars_ep3 = Movies(
    movie_title='StarWars Ep 3',
    movie_art='http://bit.ly/2kkx5du',
    movie_trailer='https://www.youtube.com/watch?v=5UnjrG_N8hU'
)

# Adding movie to the movie_list
add_movies(movie_list, star_wars_ep3)

# Instantiating movie
madmax = Movies(
    movie_title='Mad Max: Fury Road',
    movie_art='http://bit.ly/2xO0z9b',
    movie_trailer='https://www.youtube.com/watch?v=hEJnMQG9ev8'
)

# Adding movie to the movie_list
add_movies(movie_list, madmax)

# Instantiating movie
lotr = Movies(
    movie_title='The Lord of the Rings: The Fellowship of the Ring',
    movie_art='http://bit.ly/2xXepWs',
    movie_trailer='https://www.youtube.com/watch?v=V75dMMIW2B4'
)

# Adding movie to the movie_list
add_movies(movie_list, lotr)


# Function to return the movie_list
def return_movies():
    return movie_list
