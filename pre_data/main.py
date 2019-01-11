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

def main():
    movies = Movies.objects.all()
    print(movies)

if __name__=='__main__':
    # 加载Django环境，books_management_system是我的Django项目名称
    sys.path.append('../mk')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mk.settings')
    # 引入Django模块
    import django

    # 初始化Django环境
    django.setup()
    from backend.models import Movies, Movies_Shot
    main()
