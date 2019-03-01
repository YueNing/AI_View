from moviepy.editor import AudioFileClip,VideoFileClip, concatenate_videoclips
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
                        'relationship':['get to know', 'forced situation']
                    }
                }

# clip1 = VideoFileClip("001.mp4")
# clip2 = VideoFileClip("002.mp4")
# clip3 = VideoFileClip("003.mp4")
# clip4 = VideoFileClip("004.mp4")
# clip5 = VideoFileClip("005.mp4")
# clip6 = VideoFileClip("006.mp4")
# clip7 = VideoFileClip("007.mp4")
# final_clip = concatenate_videoclips([clip1,clip2, clip3, clip4, clip5, clip6, clip7])
# final_clip.write_videofile("my_concatenation.mp4",audio="../music/action/01.mp3")