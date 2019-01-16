###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Last Change Datum: 16.01.2019
# Location: KIT
# File_Name: main
# E-mail: n1085633848@gmail.com
###############################

import os,sys
import imdb
import download_trailer
import imdb_analyse
import scenedetect
import deal_video
from tqdm import tqdm

# 加载Django环境，books_management_system是我的Django项目名称
sys.path.append('../mk')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mk.settings')
# 引入Django模块
import django
# 初始化Django环境
django.setup()
from backend.models import Movies, Movies_Shot

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
            print('set download task: %s'%(opt['name']))
        print('finish set the download tasks and wait for minutens\n')
        print('start to analyse the movies and save related information to database')
        for movie in urls:
            opt['url'] = movie.strip()
            opt['name'] =  opt['title_id'] = opt['url'].split('/')[4]
            imdb_analyse.main(opt)
        print('finish analyse the movies and save function\n')
        print('start to split full video to small shot videos and at the same time to save the information into database')
        for video in urls:
            opt['url'] = video.strip()
            opt['name'] = opt['title_id'] = opt['url'].split('/')[4]
            opt['source_videos'] = opt['output_dir']
            input_video = opt['output_dir']+'/'+opt['name']+'.mp4'
            opt['input_video'] = input_video
            response = scenedetect.main(opt)
            print(response)
        print('finished split function\n')

if __name__=='__main__':
    main()
