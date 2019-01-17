###############################
# Author: Yue Ning
# Datum: 16.01.2019
# Last Change Datum: 16.01.2019
# Location: KIT
# File_Name: caption
# E-mail: n1085633848@gmail.com
###############################

import os

def change_files_name(shot):
    return 0

def extract_features():
    return 0

def get_command(opt):
    command = 'command {}'.format(opt['shot'])
    return command

def get_captions_from_file():
    captions = {'test':1, 'test2':2}
    return captions

def process_caption(opt):
    caption = opt['command']
    opt['captions'] = get_captions_from_file()
    return opt

def main(opt):
    opt['captions'] = {}
    for shot in opt['shots_videos']:
        opt['shot'] = shot
        change_files_name(opt['shot'])
    
    extract_features()
    command = get_command(opt)
    opt['command'] = command
    opt= process_caption(opt)

    response = 'finished caption in videos:{}'.format(opt['title_id'])
    opt.pop('command', None)
    opt.pop('shot', None)
    return {"response":response, "opt":opt}