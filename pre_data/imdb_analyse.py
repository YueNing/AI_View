###########################
# Author: Yue Ning
# Date: 7.1.2019
###########################
import os

from imdb import IMDb

def get_genre(ia):
    top250 = ia.get_top250_movies()
    # Iterate through the first 20 movies in the top 250
    for movie_count in range(0, 20):
        # First, retrieve the movie object using its ID
        movie = ia.get_movie(top250[movie_count].movieID)
        # Print movie title and genres
        print(movie['title'])
        print(*movie['genres'], sep=", ")
    
def main():
    ia = IMDb()
    the_matrix = ia.get_movie('0133093')
    #print(the_matrix['director'])
    #print(ia.get_movie_infoset())
    #dystopia = ia.get_k
    #keyword('ai', results=5)
    print(the_matrix['imdb'])
    #get_genre(ia)
if __name__ == "__main__":
    main()
