# # #
# # Developed by Gabor Buzasi
# # entertainment_center.py
# # Version 1.0
# # #

""" Module instantiates 6 objects of the Movie class
    and adds them to a list, which will be passed to the
    fresh_tomatoes module's function."""

import generate_html
import media

# If you'd like to change this to your own favorite movie
# change the parameters accordingly to your details and
# possibly change the name of the object as well.

the_perk_wallflower = media.Movie("The Perks of being a Wallflower", # Movie Title
                     "An introvert freshman is taken under the wings" # Movie Storyline separated into two lines
                     " of two seniors who welcome him to the real world.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMzIxOTQyODU1OV5BMl5BanBnXkFtZTcwMDQ4Mjg4Nw@@._V1_SY1000_CR0,0,676,1000_AL_.jpg", # NOQA # Box-Art or poster-image URL
                     "https://www.youtube.com/watch?v=n5rh7O4IDc0") # YouTube Trailer link

berlin_calling = media.Movie("Berlin Calling",
                             "A man tours clubs around the globe with his "
                             "manager and girlfriend. On the eve of their "
                             "largest album release he is admitted to a "
                             "psychiatric clinic after overdosing at a gig.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BM2Q5MGQ2NTctM2MzZC00NjRiLTliNjEtZmE2NjFlNTY4ZTk3L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMzA3Njg4MzY@._V1_SY1000_CR0,0,707,1000_AL_.jpg", # NOQA
                             "https://www.youtube.com/watch?v=drdf8OeBUUM")

dont_mess_zohan = media.Movie("You Don't Mess with the Zohan",
                              "An Israeli Special Forces Soldier fakes his "
                              "death so he can re-emerge in New York City "
                              "as a hair stylist.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMzE2MzEzNDc5M15BMl5BanBnXkFtZTcwMzYxOTA3MQ@@._V1_.jpg", # NOQA
                              "https://www.youtube.com/watch?v=ucmnTmYpGhI")

trainspotting = media.Movie("Trainspotting",
                            "Renton, deeply immersed in the Edinburgh drug "
                            "scene, tries to clean up and get out, "
                            "despite the allure of the drugs and influence "
                            "of friends.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMzA5Zjc3ZTMtMmU5YS00YTMwLWI4MWUtYTU0YTVmNjVmODZhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg", # NOQA
                            "https://www.youtube.com/watch?v=8LuxOYIpu-I")

idiocracy = media.Movie("Idiocracy",
                        "Private Joe Bauers, the definition of "
                        "'average American', is selected by the Pentagon to "
                        "be the guinea pig for a top-secret hibernation "
                        "program. Forgotten, he awakes five centuries "
                        "in the future. He discovers a society so incredibly "
                        "dumbed down that he's easily the most intelligent "
                        "person alive.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMWQ4MzI2ZDQtYjk3MS00ODdjLTkwN2QtOTBjYzIwM2RmNzgyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX676_AL_.jpg", # NOQA
                        "https://www.youtube.com/watch?v=BBvIweCIgwk")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole "
                           "in space in an attempt to ensure humanity's "
                           "survival.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg", # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Assign the objects into a list
movies = [the_perk_wallflower, berlin_calling, dont_mess_zohan,
          trainspotting, idiocracy, interstellar]

# Pass the list of movies 'movies' object to the
# open_movies_page function of 'generate_html' module
generate_html.open_movies_page(movies)

