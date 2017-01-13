## What's included: ##

**media.py**
This is a python file, it has a movie class defined, and this
class stores movie related information, such as movie title, trailer, 
poster image, and a link to a youtube trailer. This class includes doc string, to view this class information, type `print (media.Movie.__doc__)` in python command prompt. 

**entertainment.py**
This is a python file, it contains instances of a class movie defined in 
media.py file. Each instance of a class corresponds to a movie that 
is being displayed on the webpage. New movies can be added to the page by
creating another instance of a movie class.

**freshtomatoes.py**
This is a python file that has the html code and styling code to display the list of movies, this file lets the user play a trailer of each movie. This file contains python functions, this file uses a list of movie instances created in entertainment.py and passes this list to function open_movies_page to display this list of movies.

## How to Run this Program: ##
In order to run this program, right click on entertainment_center.py inside  the project directory and select
run, this will open up a page in a browser. The page will display a list of movies, and clicking on each movie will play the movie trailer.


## Adding new movies to the page: ##
Adding a new movie to the page requires creating an instance of a class, to add a new
movie simply open the file entertainment.py in python idle, then create a new instance of a class movie and give it the same name as the movie. Below is the example code to create a new instance of a movie class.
`
toy_story = media.Movie("movie name",                           
                        "short description",   
                        "PostImage URL",    
                        "Youtube Trailer URL")`

After instantiating an object of a class movie, add the above instance name to the list at the bottom of the entertainment.py file as shown below.

`movies = [toy_story, avatar, school_of_rock, 
          Terminator2, midnight_in_paris, hunger_games]
`
## Deleting movies from the page: ##
To delete a movie, simply delete an instance name from the movie list at the bottom of the entertainment.py file as shown below.

`movies = [toy_story, avatar, school_of_rock, 
          Terminator2, midnight_in_paris, hunger_games]
`



