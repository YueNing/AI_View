###############################
# Author: Yue Ning
# Datum: 16.01.2019
# Last Change Datum: 22.01.2019
# Location: KIT
# File_Name: caption
# E-mail: n1085633848@gmail.com
###############################

import os,sys
import json
import argparse
sys.path.append('..')
import eval, prepro_feats
from eval import main as result_caption 
import shutil
import subprocess
import glob
from tqdm import tqdm
import numpy as np
import os
import argparse

import torch
from torch import nn
import torch.nn.functional as F
from torch.autograd import Variable
import pretrainedmodels
from pretrainedmodels import utils

'''
	parameter: 
	source_video_path,
	result_caption_path
'''
def change_files_name(feats_dir):
    f_dir = feats_dir[0]
    for filename in os.listdir(f_dir):
        os.rename(os.path.join(f_dir,filename), os.path.join(f_dir, filename).replace('tt4131496-Scene-0','video'))
    for filename in os.listdir(f_dir):
        os.rename(os.path.join(f_dir,filename), os.path.join(f_dir, filename).replace('video0','video'))

def extract_feats(args):
    params = args
    if params['model'] == 'inception_v3':
        C, H, W = 3, 299, 299
        model = pretrainedmodels.inceptionv3(pretrained='imagenet')
        load_image_fn = utils.LoadTransformImage(model)

    elif params['model'] == 'resnet152':
        C, H, W = 3, 224, 224
        model = pretrainedmodels.resnet152(pretrained='imagenet')
        load_image_fn = utils.LoadTransformImage(model)

    elif params['model'] == 'inception_v4':
        C, H, W = 3, 299, 299
        model = pretrainedmodels.inceptionv4(
            num_classes=1000, pretrained='imagenet')
        load_image_fn = utils.LoadTransformImage(model)

    else:
        print("doesn't support %s" % (params['model']))

    model.last_linear = utils.Identity()
    model = nn.DataParallel(model)
    model = model.cuda()
    prepro_feats.extract_feats(params, model, load_image_fn)

def get_command(opt):
    command = 'command {}'.format(opt['shot'])
    return command

def get_caption(opt_eval):
    change_files_name(opt_eval['feats_dir'])
    opt_eval['model'] = opt_eval['generate_caption_model']
    result_caption(opt_eval)

def run_caption(parser_cap):

    args = parser_cap.parse_args()
    args = vars((args))
    opt_cap = json.load(open(args["recover_opt"]))
    for k, v in args.items():
        opt_cap[k] = v
    os.environ['CUDA_VISIBLE_DEVICES'] = opt_cap["gpu"]
    eval.main(opt_cap)
    return 0

def get_captions_from_file():
    captions = {'test':1, 'test2':2}
    return captions

def process_caption(opt):
    caption = opt['command']
    no_caption = True
    if no_caption:
        run_caption(opt['parser_cap'])
    else:
        opt['captions'] = get_captions_from_file()
    return opt

def process_feats(opt):
    no_feats = True
    if no_feats:
        extract_features(opt['parser_feats'])
    else:
        reponse = "we have now the feats of"
    reponse="get the feats of"
    return reponse

def main(opt):
    parser_feats = argparse.ArgumentParser()
    parser_cap = argparse.ArgumentParser()
    parser_feats.add_argument("--gpu", dest='gpu', type=str, default='0',
                        help='Set CUDA_VISIBLE_DEVICES environment variable, optional')
    parser_feats.add_argument("--output_dir", dest='output_dir', type=str,
                        default='../data/feats/resnet152', help='directory to store features')
    parser_feats.add_argument("--n_frame_steps", dest='n_frame_steps', type=int, default=40,
                        help='how many frames to sampler per video')

    parser_feats.add_argument("--video_path", dest='video_path', type=str,
                        default='../data/test-video', help='path to video dataset')
    parser_feats.add_argument("--model", dest="model", type=str, default='resnet152',
                        help='the CNN model you want to use to extract_feats')
    parser_feats.add_argument("--saved_model", dest="saved_model", type=str, default='',
                        help='the pretrained CNN model you want to use to extract_feats')

    parser_cap.add_argument('--recover_opt', type=str, default='../data/save/opt_info.json',
                        help='recover train opts from saved opt_json')
    parser_cap.add_argument('--saved_model', type=str, default='../data/save/model_1050.pth',
                        help='path to saved model to evaluate')

    parser_cap.add_argument('--dump_json', type=int, default=1,
                        help='Dump json with predictions into vis folder? (1=yes,0=no)')
    parser_cap.add_argument('--results_path', type=str, default='results/')
    parser_cap.add_argument('--dump_path', type=int, default=0,
                        help='Write image paths along with predictions into vis json? (1=yes,0=no)')
    parser_cap.add_argument('--gpu', type=str, default='0',
                        help='gpu device number')
    parser_cap.add_argument('--batch_size', type=int, default=128,
                        help='minibatch size')
    parser_cap.add_argument('--sample_max', type=int, default=1,
                        help='0/1. whether sample max probs  to get next word in inference stage')
    parser_cap.add_argument('--temperature', type=float, default=1.0)
    parser_cap.add_argument('--beam_size', type=int, default=1,
                        help='used when sample_max = 1. Usually 2 or 3 works well.')
    
    opt['parser_feats'] = parser_feats
    opt['parser_cap'] = parser_cap
    opt['captions'] = {}
    for shot in opt['shots_videos']:
        opt['shot'] = shot
        change_files_name(opt['shot'])
    
    process_feats(opt)
    command = get_command(opt)
    opt['command'] = command
    opt= process_caption(opt)

    response = 'finished caption in videos:{}'.format(opt['title_id'])
    opt.pop('command', None)
    opt.pop('shot', None)
    return {"response":response, "opt":opt}