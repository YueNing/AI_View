###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Location: KIT
# File_Name: imdb_analyse 
# E-mail: n1085633848@gmail.com
###############################

import os,sys
import datetime
from imdb import IMDb
from tqdm import tqdm
import subprocess

# 加载Django环境，books_management_system是我的Django项目名称
sys.path.append('../mk')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mk.settings')
# 引入Django模块
import django
# 初始化Django环境
django.setup()
from backend.models import Movies, Movies_Shot

class movie_analyse():
        def __init__(self,opt):
                self.opt = opt
                self._movie_id = self.opt['title_id'][2:]
                self._movie = IMDb().get_movie(self._movie_id)
                self._title = self._movie['title']
                self._genres = self._movie['genres']
                self._director = self._movie['director']
                self._plot = self._movie['plot']
                self.full_time = self.getLength()
        @property
        def title(self):
                return self._title
        @property
        def movie_id(self):
                return self._movie_id
        @property
        def movie(self):
                return self._movie
        @property
        def  genres(self):
                return self._genres[0]
        @property
        def director(self):
                return self._director[0]['name']
        @property
        def plot(self):
                return self._plot[0]
        
        def getLength(self):
                if os.path.isfile(self.opt['output_dir']+'/'+self.opt['title_id']+'.mp4'):
                        input_video = self.opt['output_dir']+'/'+ self.opt['title_id'] + '.mp4'
                        #input_video_path = os.path.abspath(input_video)
                        cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(input_video)
                        output = subprocess.check_output(
                                cmd,
                                shell=True, # Let this run in the shell
                                stderr=subprocess.STDOUT
                        )
                        
                        return datetime.timedelta(seconds=float(output))

class Save():
        def __init__(self, data):
                self.data = data
                self.response = self.process()
        def process(self):
                return 'successful save the data: %s'%(self.data['movie_id'])

def analyse_videos(opt):
       movie = movie_analyse(opt)
       save_data = {}
       save_data['movie_id'] = movie.movie_id
       save_data['title'] = movie.title
       save_data['genres'] = movie.genres
       save_data['director'] =movie.director
       save_data['plot'] = movie.plot
       save_data['full_time'] = movie.full_time
       return save_data

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
        # import pdb
        # pdb.set_trace()
        save_data = analyse_videos(opt)
        django_mysql_saver = Save(save_data)
        print(save_data)
        print(django_mysql_saver.response)

if __name__ == "__main__":
    opt={}
    main(opt)
