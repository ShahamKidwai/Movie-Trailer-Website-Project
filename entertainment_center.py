import fresh_tomatoes  # file import fresh_tomatoes.py
import media  # file import media.py

# toy_story, instance of a movie class
# initializes an object with movie data
toy_story = media.Movie("Toy Story",                                                     
                        "A story of a boy and his toys that come to life",   
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",    
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# avatar, an instance of a movie class
# initializes an object with movie data
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

# school_of_rock, an instance of a movie class
# intializes an object with movie data
school_of_rock = media.Movie("School of Rock",
                             "Using rock Music to Learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# midnight_in_paris, an instance of a movie class
# intializes an object with movie data
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://youtu.be/FAfR8omt-CY")

# hunger_games, an instance of a movie class
# intializes an object with movie data
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://youtu.be/mfmrPu43DF8")

# Terminator2, an instance of a movie class
# initializes an object with movie data
Terminator2 = media.Movie("Terminator 2",
                          "A story of a cyborg designed to kill humans",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Terminator-2-judgement-day.jpg/250px-Terminator-2-judgement-day.jpg",
                          "https://www.youtube.com/watch?v=F1os6UU6jhU")

movies = [toy_story, avatar, school_of_rock, 
          Terminator2, midnight_in_paris, hunger_games]  # creates a movie list

fresh_tomatoes.open_movies_page(movies)  # passes a movie list into a func
