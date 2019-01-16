###############################
# Author: Yue Ning
# Datum: 7.01.2019
# Last Change Datum: 16.01.2019
# Location: KIT
# File_Name: scene detect
# E-mail: n1085633848@gmail.com
###############################

import os
import subprocess

def get_command(opt):
    output_dir = 'my_video_scenes_tmp/'+ opt['title_id']    
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    command = "scenedetect --input {} --output {} --stats my_video.stats.csv detect-content list-scenes split-video".format(opt['input_video'], output_dir)
    return command

def process_split(opt):
    response = ''
    if opt['command']:
        subprocess.check_output(
            opt['command'],
            shell=True, # Let this run in the shell
            stderr=subprocess.STDOUT
        )
        response = "successfully split the video: {}".format(opt['title_id'])
        return response
    else:
        response = 'error command'
        return response

def main(opt):
    command = get_command(opt)
    opt['command'] = command
    response = process_split(opt)
    return response