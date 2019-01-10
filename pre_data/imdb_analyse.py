###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Location: KIT
# File_Name: imdb_analyse 
# E-mail: n1085633848@gmail.com
###############################

import os

from imdb import IMDb

def get_title_id(url):
    title_id = url.split('/')[4]
    return title_id

def analyse_videos(title_id):
    ia = IMDb()
    movie = ia.get_movie(title_id)
    genre = movie['genres']
    director = movie['director']
    cover_url = movie['cover_url']
    plot = movie['plot']
    save_to = movie_mysql()
    save_to.save(movie)

def read_from_file(opt):
    with open(opt['input'], 'r', encoding='UTF-8') as f:
        for line in tqdm(f.readlines()):
            title_id = get_title_id(line)
            analyse_videos(title_id)

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
