# # #
# # Developed by Gabor Buzasi
# # media.py
# # Version 1.0
# # #

""" Module contains the Movie class."""
class Movie():
    """ This class provides a way to store movie related information"""
    
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube):
        """ Constructor for the class Movie, that takes 4 parameters to instantiate a new object."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

