####################################
# File name: main.py               #
# Author: Yue Ning                 #
# Submission:                      #
# Instructor:                      #
# Date created: 1/1/2019           #
# Date last modified: 20/1/2019     #
# Python Version: 3.5              #
####################################

import os
import sys
import opts
import json
import argparse
from pre_data.deal_video import extract_frames_5s
import prepro_feats
import pretrainedmodels
from pretrainedmodels import utils
import torch
from torch import nn
from eval import main as result_caption
from pre_data import imdb_analyse,download_trailer,scenedetect,caption
# 加载Django环境，books_management_system是我的Django项目名称
sys.path.append('./mk')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mk.settings')
# 引入Django模块
import django
# 初始化Django环境
django.setup()
from backend.models import Movies, Movies_Shot
# first need to get source-video and edit the videodatainfo.json 
# run the under command get the test video
# python deal_video.py --video_input_path data/source-video/ --video_output_path data/test-video/  --videodatainfo videodatainfo.json

# run the under command extract the features from the test video 
# python prepro_feats.py --output_dir data/feats/resnet152 --model resnet152 --n_frame_steps 40  --gpu 0 --video_path data/test-video

# change the info.json get the right test video index(about feats in test-video) and 
# run the under command to get caption result in result file
# featurs dir is writted in opt_info.json default data/feats/resnet152/test-video
# python eval.py --recover_opt data/save/opt_info.json

'''
	parameter: 
	source_video_path,
	result_caption_path
'''
def get_caption(opt_eval):
	opt_eval['model'] = opt_eval['generate_caption_model']
	result_caption(opt_eval)

def check_videos(output_dir):
    videos = os.listdir(output_dir)
    for video in videos:
        if video.endswith('.mp4'):
            return True
        else:
            return False

def check_video(opt):
    video = os.path.isfile(opt['output_dir']+opt['name']+'.mp4')
    if os.path.exists(video):
        return True
    else:
        print('video:{} is not downloaded'.format(opt['name']))

def check_database(name):
    # import pdb
    # pdb.set_trace()
    if not Movies.objects.filter(title_id=name[2:]):
        return True
    else:
        return False

def check_split(name):
    check_dir = 'my_video_scenes_tmp/'+name
    if os.path.exists(check_dir) and os.path.isdir(check_dir):
        if not os.listdir(check_dir):
            return True
        else:
            return False
    else:
        return True

def main(opt_video_datainfo, opt_eval):
	#print("split video to 5s video....")
	#extract_frames_5s(opt_video_datainfo)
	#print("split video finish")
    opt = {}
    opt['downloader'] = 'youtube-dl'
    opt['output_dir'] = 'data/source_videos/'
    with open('pre_data/videos_url') as f:
        print('INFO:download now the videos.....')
        urls = f.readlines()
        for url in urls:
            opt['url'] = url.strip()
            opt['name'] = opt['url'].split('/')[4]
            if os.path.isfile(opt['output_dir']+opt['name']+".mp4"):
                print('video:{} is already exist'.format(opt['name']))
            elif os.path.isfile(opt['output_dir']+opt['name']+".mp4.part"):
                print('download task:{} is already exist '.format(opt['name']))
                print('finish set the download tasks:{} and wait for minutes\n'.format(opt['name']))              
            else:
                download_trailer.main(opt)
                print('set download task: %s'%(opt['name']))
        print("INFO:download tasks set finished....\n")

        videos_not_empty = check_videos(opt['output_dir'])
        if videos_not_empty:
            print("INFO:Process videos......................")
            for url in urls:
                opt['url'] = url.strip()
                opt['title_id'] = opt['name'] = opt['url'].split('/')[4]
                opt['source_videos'] = opt['output_dir']
                input_video = opt['output_dir']+'/'+opt['name']+'.mp4'
                opt['input_video'] = input_video

                exist_video = check_video(opt)
                not_in_database = check_database(opt['name'])
                not_split = check_split(opt['name'])
                not_extracted = False
                not_get_caption = False
                print("video:{} processed now.........".format(opt['name']))
                if exist_video:
                    if not_in_database:
                        print("start analyse video:{} and save data".format(opt['name']))
                        imdb_analyse.main(opt)
                        print("|n finish analyse video:{}".format(opt['name']))
                    else:
                        print('already saved into database!'.format(opt['name']))
                    if exist_video and not_split:
                        print("start split video:{}".format(opt['name']))
                        response = scenedetect.main(opt)
                        print(response)
                        print("finish split video:{}".format(opt['name']))
                    else:
                        print('already split'.format(opt['name']))
                    
                    if exist_video and not_extracted:
                        print("extract feats........")
                        caption.extract_feats(opt_video_datainfo)
                        print("extract feats finish")
                    else:
                        print('already extracted '.format(opt['name']))
                                    
                    if exist_video and not_get_caption:
                        print("get the caption")
                        caption.get_caption(opt_eval)
                        print("finish get the caption")
                    else:
                        print('already get the caption '.format(opt['name']))
                else:
                    print('don not have this , please check downloaded or not!'.format(opt['name']))
                print("video:{} processed finished.........\n".format(opt['name']))                

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--video_input_path', type=str, default="data/source-video/",
                        help='video input path')
  parser.add_argument('--video_output_path', type=str, default="data/test-video/",
                        help='video input path')
  parser.add_argument('--videodatainfo', type=str, default="pre_data/videodatainfo.json",
                        help='video input path')
  parser.add_argument("--gpu", dest='gpu', type=str, default='0',
                        help='Set CUDA_VISIBLE_DEVICES environment variable, optional')
  parser.add_argument("--output_dir", dest='output_dir', type=str,
                        default='data/feats/resnet152', help='directory to store features')
  parser.add_argument("--n_frame_steps", dest='n_frame_steps', type=int, default=40,
                        help='how many frames to sampler per video')
  parser.add_argument("--video_path", dest='video_path', type=str,
                        default='data/test-video', help='path to video dataset')
  parser.add_argument("--model", dest="model", type=str, default='resnet152',
                        help='the CNN model you want to use to extract_feats')
  parser.add_argument('--recover_opt', type=str, default='data/save/opt_info.json',
                        help='recover train opts from saved opt_json')
  parser.add_argument('--saved_model', type=str, default='data/save/model_1050.pth',
                        help='path to saved model to evaluate')
  parser.add_argument('--dump_json', type=int, default=1,
                        help='Dump json with predictions into vis folder? (1=yes,0=no)')
  parser.add_argument('--results_path', type=str, default='results/')
  parser.add_argument('--dump_path', type=int, default=0,
                        help='Write image paths along with predictions into vis json? (1=yes,0=no)')
  parser.add_argument('--batch_size', type=int, default=128,
                        help='minibatch size')
  parser.add_argument('--sample_max', type=int, default=1,
                        help='0/1. whether sample max probs  to get next word in inference stage')
  parser.add_argument('--temperature', type=float, default=1.0)
  parser.add_argument('--beam_size', type=int, default=1,
                        help='used when sample_max = 1. Usually 2 or 3 works well.')
  parser.add_argument('--generate_caption_model', type=str, default='S2VTAttModel',
                        help='generate_caption_model')
  args = parser.parse_args()
  os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
  args = vars((args))
  opt_video_datainfo = json.load(open(args["videodatainfo"]))
  opt_eval = json.load(open(args["recover_opt"]))
  args['generate_caption_model'] = opt_eval['model']
  for k, v in args.items():
    opt_video_datainfo[k] = v
    opt_eval[k] = v
  video_index = 0
  main(opt_video_datainfo, opt_eval)