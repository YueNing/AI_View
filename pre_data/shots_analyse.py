###############################
# Author: Yue Ning
# Datum: 21.01.2019
# Last Change Datum: 21.01.2019
# Location: Karlsruhe
# File_Name: shots_analyse 
# E-mail: n1085633848@gmail.com
###############################
import os,sys
import datetime
import csv

# 加载Django环境，books_management_system是我的Django项目名称
sys.path.append('../mk')
sys.path.append('./mk')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mk.settings')
# 引入Django模块
import django
# 初始化Django环境
django.setup()
from backend.models import Movies, Movies_Shot

class shots_analyse():
    def __init__(self,opt):
        self.opt = opt
        self.save_data = {}
        self.shots = os.listdir(self.opt['shots_dir']+self.opt['name'])
        self.shots_videos = []
        self.shots_video_stats = []
        self.shots_video_scenes = [] 
        for shot in self.shots:
            if shot.endswith('stats.csv'):
                self.shots_video_stats.append(shot)
            elif shot.endswith('.mp4'):
                self.shots_videos.append(shot)
            elif shot.endswith('Scenes.csv'):
                self.shots_video_scenes.append(shot)
        self.response = self._process()

    def _process(self):
        response = self.save()
        return response

    #*FUNC: analyse the file video information get the start and end time
    def analyse_split_video_csv(self):
        input_file =open(self.opt['shots_dir']+self.opt['name']+'/'+self.opt['name']+'-Scenes.csv')
        read = csv.reader(input_file)
        for k, row in enumerate(read):
            if row[0] == str(int(self.save_data['shot_id'])):
                start_time = datetime.timedelta(seconds=float(row[3]))
                end_time = datetime.timedelta(seconds=float(row[6]))                
                break
        return [start_time, end_time]

    #TODO: analyse the file results caption S2VTAttModel.json
    def analyse_result_caption_json(self):
        caption = 'caption shot'
        return caption
    
    def save(self):
        for shot in self.shots_videos:
            self.save_data['shot_id'] =  shot.split('-')[2][:-4]
            self.save_data['title'] = self.opt['name']
            self.save_data['video_url'] = self.opt['url']
            [self.save_data['start_time'], self.save_data['end_time']] = self.analyse_split_video_csv()
            self.save_data['caption'] = self.analyse_result_caption_json()
            self.save_data['movies'] = Movies.objects.filter(title_id=self.opt['title_id'][2:])[0]
            if not Movies_Shot.objects.filter(shot_id=self.save_data['shot_id']): 
                shots_saver = Movies_Shot(shot_id=self.save_data['shot_id'], title=self.save_data['title'],
                                        video_url=self.save_data['video_url'], start_time=self.save_data['start_time'],
                                        end_time=self.save_data['end_time'], caption=self.save_data['caption'], 
                                        movies=self.save_data['movies'], genre=self.save_data['movies'].genres)
                shots_saver.save()
            else:
                shots_saver = Movies_Shot(id=Movies_Shot.objects.filter(shot_id=self.save_data['shot_id'])[0].id, shot_id=self.save_data['shot_id'], title=self.save_data['title'],
                        video_url=self.save_data['video_url'], start_time=self.save_data['start_time'],
                        end_time=self.save_data['end_time'], caption=self.save_data['caption'], 
                        movies=self.save_data['movies'], genre=self.save_data['movies'].genres)
                shots_saver.save()                
                print('exist shot:{}, update the data'.format(self.save_data['shot_id']))
        return "finish save shots"

def main(opt):
    response = 'successfully save the shot\'s information'
    shots_analyser = shots_analyse(opt)
    print(shots_analyser.response)
    return response