###############################
# Author: Yue Ning
# Datum: 7.01.2019
# Last change Datum: 16.1.2019
# Location: KIT
# File_Name: downloader
# E-mail: n1085633848@gmail.com
###############################

import os
from tqdm import tqdm
import time
import subprocess
import argparse
import wget
downloader = ['youtube-dl', 'you-get', 'wget', 'curl']

def curl_downloader(opt):
    return

def wget_downloader(opt):
    if opt['downloader'] == 'wget': 
        with open(opt['input'], 'r', encoding='UTF-8') as f:
            for line in tqdm(f.readlines()):
                filename = wget.download(line.strip(), out=opt['output_dir'])
                print("%s download finish"%(filename))
                time.sleep(1)

def youtube_dl_downloader(opt=None):
    if opt['downloader'] == 'youtube-dl' and opt['url']:
        if not opt['name']:
            if not os.path.isfile(opt['output_dir']+'/'+opt['name']+'.mp4'):
                print('don not have video name opt, then default save the videos')
                command = ["youtube-dl", '-o', opt['output_dir']+'/'+'%(title)s.%(ext)s'+'.mp4', opt['url']]
                subprocess.Popen(command)
        else:
            if not os.path.isfile(opt['output_dir']+'/'+opt['name']+'.mp4'):
                with open(os.devnull, 'w') as youtube_dl_log:           
                    command = ["youtube-dl", '-o', opt['output_dir']+'/'+opt['name']+'.mp4', opt['url']]
                    subprocess.Popen(command, stdout=youtube_dl_log, stderr=youtube_dl_log)

    elif opt['downloader'] == 'youtube-dl' and opt['input'] and opt['output_dir']:
        global index
        index = 0
        with open(os.devnull, 'w') as youtube_dl_log:
            with open(opt['input'], 'r', encoding='UTF-8') as f:
                for line in tqdm(f.readlines()):
                    command =["youtube-dl", '-o', opt['output_dir']+'/'+'%(title)s.%(ext)s'+'.mp4', line.strip()]
                    index = index + 1
                    subprocess.Popen(command, stdout=youtube_dl_log,stderr=youtube_dl_log)
    else:
        print('parameters is erros')

def you_get_downloader(opt):
    return

def select_downloader(downloader, opt):
    selected_downloader = {
        'youtube-dl': youtube_dl_downloader(opt),
        'you-get': you_get_downloader(opt),
        'wget': wget_downloader(opt),
        'curl': curl_downloader(opt)
    }
    return selected_downloader.get(downloader, None)

def main(opt):
    if not os.path.isdir(opt['output_dir']):
        os.makedirs(opt['output_dir'])
    select_downloader(opt['downloader'], opt)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='videos_url', help='input videos urls')
    parser.add_argument('--output_dir', type=str, default='videos', help='input videos urls')
    parser.add_argument('--downloader', type=str, default='youtube-dl', help='input videos urls')
    args = parser.parse_args()
    opt = vars(args)
    index = 0
    main(opt)