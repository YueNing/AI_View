###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Location: KIT
# File_Name: imdb_analyse 
# E-mail: n1085633848@gmail.com
###############################

import os,sys
from imdb import IMDb
from tqdm import tqdm
# 加载Django环境，books_management_system是我的Django项目名称
sys.path.append('../mk')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mk.settings')
# 引入Django模块
import django
# 初始化Django环境
django.setup()
from backend.models import Movies, Movies_Shot

def movie_mysql():
        return 0

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
    
def main(opt):
    movies = Movies.objects.all()
    import pdb
    pdb.set_trace()
    ia = IMDb()
    the_matrix = ia.get_movie('0133093')
    #print(the_matrix['director'])
    # #print(ia.get_movie_infoset())
    # #dystopia = ia.get_k
    # #keyword('ai', results=5)
    # print(the_matrix['imdb'])
    # #get_genre(ia)
if __name__ == "__main__":
    opt={}
    main(opt)
