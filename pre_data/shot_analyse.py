###############################
# Author: Yue Ning
# Datum: 16.01.2019
# Last Change Datum: 16.01.2019
# Location: KIT
# File_Name: shot_analyse 
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
#from backend.models import Movies, Movies_Shot

class shot_analyse():
    def __init__(self, opt):
        self.opt = opt

def main(opt):
    response = ''
    return response

