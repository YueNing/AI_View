
from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys, os
# /home/ubuntu/mk/AI_View
my_path = os.path.abspath(os.path.dirname(__file__))
def main(opt):
    """ return the url of concatenate video
    >>> main(opt={"output_dir":"my_videos_tmp/","movie_shots":['my_videos_tmp/test1.mp4'],'user_id':'1'})
    '/home/ubuntu/mk/AI_View/mk/backend/../../my_videos_tmp/show_video_1.mp4' 
    """
    opt['output_dir'] = os.path.join(my_path, '../../'+opt['output_dir'])
    for index, m in enumerate(opt['movie_shots']):
        opt['movie_shots'][index] = os.path.join(my_path, '../../'+m)
    clips = []
    for clip in opt['movie_shots']:
        clips.append(VideoFileClip(clip))
    final_clip = concatenate_videoclips(clips)
    write_url = os.path.join(my_path, opt['output_dir']+"show_video_{}.mp4".format(opt['user_id']))
    final_clip.write_videofile(write_url)
    return write_url

if __name__ =='__main__':
    #opt={"output_dir":os.path.join(my_path, "../../my_videos_tmp/"),"movie_shots":[os.path.join(my_path, '../../my_videos_tmp/test1.mp4')],'user_id':'1'}
    #main(opt)
    import doctest
    doctest.testmod()


