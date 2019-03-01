###############################
# Author: Yue Ning
# Datum: 1.01.2019
# Date last modified: 24.01.2019
# Location: Karlsruhe
# File_Name: deal_video 
# E-mail: n1085633848@gmail.com
###############################
import json
import os
import argparse
from tqdm import tqdm
import sys
import subprocess

def dump_to_json_format():
  return

def extract_frames_5s(opt):
  global video_index
  with open(os.devnull, "w") as ffmpeg_log:
    video_index = 0
    for video in opt["videos"]:
      for time_multiple in range(int(video['end_time']/5)):
        start = time_multiple*5
        end = (time_multiple+1)*5
        source_video = opt['video_input_path']+video['video_id']+'.mp4'
        output_file = opt['video_output_path']+"video"+str(video_index)+".mp4"
        video_index=video_index+1
        video_to_frames_5s_command = ["ffmpeg",
                      '-i', source_video,
                      '-y',
                      '-ss', str(start),
                      '-t', str(end),
                      '-c',"copy",
                      output_file]
        print(video_to_frames_5s_command)
        subprocess.call(video_to_frames_5s_command, stdout=ffmpeg_log, stderr=ffmpeg_log)
      print("%s extracted finish"%(video['video_id']))
def read_file_to_list(path):
  files = os.listdir(path)
  return files

def main(opt):
  files = read_file_to_list(opt["video_input_path"])
  extract_frames_5s(opt)
 
def add_keyframe(opt):
  command = ['ffmpeg', '-i', opt['input_video'], '-g', '1', '-keyint_min', '1', opt['keyframe_video_dir']+opt['name']+'.mp4']
  output = subprocess.check_output(
                                  command,
                                  shell=True, # Let this run in the shell
                                  stderr=subprocess.STDOUT
                          )
  response = 'set task to add key frame'
  return response

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--video_input_path', type=str, default='../data/source-video/', help='input video file directory')
  parser.add_argument('--video_output_path', type=str, default='../data/test-video/', help='video_output_path')
  parser.add_argument('--videodatainfo', type=str, default='videodatainfo.json', help='video_output_path')                  
  args = parser.parse_args()
  args = vars((args))
  opt = json.load(open(args["videodatainfo"]))
  for k, v in args.items():
    opt[k] = v
  video_index = 0
  main(opt)