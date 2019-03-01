###############################
# Author: Yue Ning
# Datum: 7.01.2019
# Last Change Datum: 22.01.2019
# Location: KIT
# File_Name: scene detect
# E-mail: n1085633848@gmail.com
###############################

import os
import subprocess

def get_command(opt):
    output_dir = 'my_video_scenes_tmp/'+ opt['title_id']
    opt['slot_output_dir'] = output_dir
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    command = "scenedetect --input {} --output {} --stats my_video.stats.csv detect-content list-scenes split-video".format(opt['input_video'], output_dir)
    return command

def process_split(opt):
    response = ''
    if opt['input_video'] and not os.listdir(opt['slot_output_dir']):
        subprocess.check_output(
            opt['command'],
            shell=True,
            stderr=subprocess.STDOUT
        )
        response = "successfully split the video: {}".format(opt['title_id'])
        return response
    else:
        response = 'Warning:check Whether the download was successful or check split result directory(finished): {}'.format(opt['title_id'])
        return response

def main(opt):
    command = get_command(opt)
    opt['command'] = command
    response = process_split(opt)
    opt.pop('slot_output_dir', None)
    return response