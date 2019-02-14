from moviepy.editor import VideoFileClip, concatenate_videoclips
from backend import concat
from backend.models import k_Shot
import random
word2vector = {'drama':
                    {
                        'loss':['death','get up', 'discussion'], 
                        'kidnapping':['car ride', 'phone call', 'dramatic reunion'], 
                        'identity crisis':['despair','resolution','knowledge moment']
                    },
                'action':
                    {
                        'war':['attack', 'climax', 'make a plan'],
                        'space':['no return', 'aliens attack', 'missing your family'],
                        'competition':['win', 'lose', 'car chase']
                    },
                'comedy':
                    {
                        'confusion':['a object', 'a person'],
                        'surrealism':['shapes', 'colors'],
                        'relationship':['get-to-know', 'forced situation']
                    }
                }
            
def get_shots_url(plot):
    """
    >>> get_shots_url('despair')
    ['my_video_scenes_tmp/videos/001.mp4', 'my_video_scenes_tmp/videos/002.mp4', 'my_video_scenes_tmp/videos/003.mp4', 'my_video_scenes_tmp/videos/004.mp4', 'my_video_scenes_tmp/videos/005.mp4', 'my_video_scenes_tmp/videos/006.mp4']
    """
    shots_url = ['my_video_scenes_tmp/videos/001.mp4','my_video_scenes_tmp/videos/002.mp4','my_video_scenes_tmp/videos/003.mp4','my_video_scenes_tmp/videos/004.mp4','my_video_scenes_tmp/videos/005.mp4','my_video_scenes_tmp/videos/006.mp4']
    test_shots_url = []
    for object_s in k_Shot.objects.all():
        for pl in object_s.getplots():
            if pl == plot:
                test_shots_url.append(object_s.url[17:])

    if len(test_shots_url) >= 6:
        shots_url = random.sample(test_shots_url, 6)
    else:
        shots_url = test_shots_url
    return shots_url

def main(pl):
    """
    >>> main('death')
    show_video_amdin.mp4
    """
    for genre in word2vector:
        for theme in word2vector[genre]:
            for plot in word2vector[genre][theme]:
                if pl==plot:
                    movie_shots = get_shots_url(plot)
                    if genre == 'action':
                        opt = {"output_dir":"static/", "logo":"logo/logo_idents.mp4", "movie_shots":movie_shots, 'user_id':'admin', 'audio':'action/{}.mp3'.format(random.randint(1,5))}
                    elif genre == 'drama':
                        opt = {"output_dir":"static/", "logo":"logo/logo_idents.mp4", "movie_shots":movie_shots, 'user_id':'admin', 'audio':'drama/{}.mp3'.format(random.randint(11,14))}
                    elif genre == 'comedy':
                        opt = {"output_dir":"static/", "logo":"logo/logo_idents.mp4", "movie_shots":movie_shots, 'user_id':'admin', 'audio':'comedy/{}.mp3'.format(random.randint(6, 10))}
                    render_url = concat.main(opt)
                    return render_url
    return False

if __name__ == "__main__":
    # main('death')
    import doctest
    doctest.testmod(verbose=True)
