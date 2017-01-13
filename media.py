import webbrowser  # imports a webbrowser module

# the class movie stores movie data and uses a constructor to store movie data
# a constructor of this class takes movie data as input, stores it in variables


class Movie():
    """ the movie class stores movie related information, which includes title,
        storyline, a link to movie poster image and a link to movie trailer
        this class uses instance variable title, storyline, poster_image_url to
        store movie information"""
# the constructor of this class is defined below is used to store movie data
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title  # instance variables store movie data
        self.storyline = movie_storyline  
        self.poster_image_url = poster_image  
        self.trailer_youtube_url = trailer_youtube                                             

# the function below, show_trailer opens up movie trailer page on a browser


def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
