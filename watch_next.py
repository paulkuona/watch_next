# Importing the spacy library
import spacy

# Loading the medium-sized English model into a variable (language callable object)
# nlp
nlp = spacy.load('en_core_web_md')

# =================== Defining some functions ===================

def read_movies_file(filename):
    """This function takes a filename/URL as an argument, reads the file,
    then splits each line into a key(movie title), and description, then
    appends these to a dictionary."""

    movies_descr = {} # Declaring empty dict of movies

    with open(filename, 'r') as file:
        content = file.readlines()
    
        for line in content:

            # Splitting each line into a key/value pair
            key, description = line.strip().split(" :")
            movies_descr[key] = description # Appends key/value pair to dict
    
    return movies_descr # Returns movie dictionary

def watch_next(watched, to_watch):
    """This function takes two dictionaries as arguments. The first dictionary
    is of movies a user has watched. The second contains movies a user would
    like to choose their next watch from. The function then looks for a movie
    from the second dictionary with the highest similarity to a movie in the first
    dictionary and recommends that as the movie to watch next."""

    # Declaring variables that will store the highest similarity (max_similarity) 
    # and details about the movie with the highest similarity (next_movie)
    max_similarity = 0
    next_movie = ""

    # Iterating through possible movies to watch
    for possible_watch in to_watch.keys():

            # Creating a Doc object representing possible_watch and its linguistic properties
            comparison_movie = nlp(to_watch[possible_watch])
            
            # Iterating through watched movies
            for watched_movie in watched.keys():
                
                # Creating a Doc object for a watched movie with its linguistic properties
                previous_watch = nlp(watched[watched_movie])

                # Calculating similarity between possible_watch and watched_movie
                similarity = comparison_movie.similarity(previous_watch)          
            
            # Checking to see if the calculated similarity is the highest at time of iteration
            if similarity > max_similarity:

                # Updating highest similarity 
                max_similarity = similarity

                next_movie = f"Title: {possible_watch}\nDescription: {to_watch[possible_watch]}\n"

    # Returning movie with highest similarity
    return next_movie

# =================== Finding & Recommending Next Watch ===================

# Creating dictionaries from txt files using the read_movies_file function
watched_movie_cat = read_movies_file("watched_movie.txt")
movies_to_watch = read_movies_file("movies.txt")

# Findin and printing the next movie to watch using the watch_next function
print("\n=================== WHAT TO WATCH NEXT BASED ON MOVIES YOU HAVE WATCHED ====================\n")
print(watch_next(watched_movie_cat, movies_to_watch))