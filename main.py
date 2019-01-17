####################################
# File name: main.py               #
# Author: Yue Ning                 #
# Submission:                      #
# Instructor:                      #
# Date created: 1/1/2019           #
# Date last modified: 4/1/2019     #
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
def get_caption(opt):
	opt_eval['model'] = opt_eval['generate_caption_model']
	result_caption(opt_eval)

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
    # if params['saved_model'] != '':
    #     model.load_state_dict(torch.load(params['saved_model']), strict=False)
    model = model.cuda()
    prepro_feats.extract_feats(params, model, load_image_fn)

def main(opt_video_datainfo, opt_eval):
	print("split video to 5s video....")
	extract_frames_5s(opt_video_datainfo)
	print("split video finish")
	print("\n extract feats........")
	extract_feats(opt_video_datainfo)
	print("\n extract feats finish")
	print("\n get the caption")
	get_caption(opt_eval)
	print("\n finish get the caption")
	#prepro_feats()
	#eval()
	#os.system("python prepro_feats.py --output_dir data/feats/resnet152 --model resnet152 --n_frame_steps 40  --gpu 0 --video_path data/test-video")
	#os.system("eval.py --recover_opt data/save/opt_info.json")

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
  parser.add_argument('--saved_model', type=str, default='data/save/model_800.pth',
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