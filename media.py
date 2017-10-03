import webbrowser


class Movies:
    """
        This class represents a movie, it have tree atributes:
        movie_title
        movie_art
        movie_trailer
    """
    # Constructor to create a movie object
    def __init__(self, movie_title, movie_art, movie_trailer):

        self.movie_title = movie_title
        self.movie_art = movie_art
        self.movie_trailer = movie_trailer

    # Method to show the movie trailer
    def show_trailer(self):
        webbrowser.open(self.movie_trailer)

    # Property to return the title
    @property
    def title(self):
        return self.movie_title

    # Property to return the movie art
    @property
    def poster_image_url(self):
        return self.movie_art

    # Property to return the movie trailer
    @property
    def trailer_youtube_url(self):
        return self.movie_trailer
