###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Location: KIT
# File_Name: module_mysql
# E-mail: n1085633848@gmail.com
###############################

import os,sys
import imdb
import download_trailer
import imdb_analyse
import scenedetect
import deal_video
from tqdm import tqdm

def download(opt):
    download_trailer.main(opt)

def main():
    opt = {}
    opt['downloader'] = 'youtube-dl'
    opt['output_dir'] = 'source_videos'
    with open('videos_url') as f:
        print('download now the videos')
        urls = f.readlines()
        for url in urls:
            opt['url'] = url.strip()
            opt['name'] = opt['url'].split('/')[4]
            download(opt)
            # imdb_analyse.main(opt)
            # import pdb
            # pdb.set_trace()
            #movies = Movies.objects.all()
            #print(movies)
            print('set download task: %s'%(opt['name']))
        print('finish set the download tasks and wait for minutens')
        print('start to analyse the movies and save related information to database')
        for movie in urls:
            opt['url'] = movie.strip()
            opt['name'] = opt['url'].split('/')[4]
            imdb_analyse.main(opt)
        print('finish analyse the movies and save function')
        

if __name__=='__main__':
    main()
