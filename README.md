![d](icon.png)

# AI-View
get the video captioning and with this to analyse the plot, theme, genre

# project description
###### goal: use the source video(a lot of full film and video) to generate a personal preference promotional video

user select genre, theme, plot of videos and system generate the short personal preference promotional video. pytorch implementation of video captioning.

- frontend: django+HTML+javascript, realize the voice control(annyang) and frontend maschine human interaction
- backend: django+mysql, to manage data(such as video path, caption, video inforamtion)
- video_caption_generate: pytorch
- video classification(humar behavior): pytorch
- Multi-label universal video classification

#### Branchs
1. Spracherkennung: frontend+backend
2. video_caption: video caption, video classification(humar behavior), Multi-label universal video classification
3. master: frontend html file+full version code

#### Steps
##### Spracherkennung

In this Branch need to realize the human maschine interaction, use the django framework and voice control(annyang javescript)

1. interface design [@YueNing](https://github.com/YueNing/AI_View/tree/Spracherkennung/mk/frontend/templates/frontend) [@kevin](https://github.com/datadrivennarratives/AI_View/blob/master/html.zip)
2. backend data management and data structur design [@kevin](https://github.com/datadrivennarratives/AI_View/blob/master/mk/backend/models.py) [@brankyy](https://github.com/brankyy) **Not yet implemented**
3. voice control [@brankyy](https://github.com/brankyy) [@YueNing](https://github.com/yuening) **Not yet implemented**

##### video_caption

In this Branch need to realize the video process code, 

1. video caption(Video-based semantic content) [@YueNing](https://github.com/YueNing/AI_View/tree/video_caption)
2. video classification(Human behavior recognition) [@YueNing](https://github.com/YueNing/AI_View/tree/video_caption/video-classification-3d-cnn-pytorch)
3. Multi-label universal video classification(Video-based semantic content) [@YueNing](https://github.com/yuening) [@brankyy](https://github.com/brankyy) **Not yet implemented**

##### master

In this Branch merge all project code to here to get the final project code
 
#### About Links
- [Source video](https://drive.google.com/open?id=1f0A1u-ZpN7s1yFLTOn5KY38Bt8bnA1dY)
- [model](https://drive.google.com/open?id=1FnGXdHplAPNQldmDXp2p33qEQF_tCDHK)
- [Annyang voice contorl](https://github.com/TalAter/annyang)
- [Theoretical introduction Chinese](https://zhuanlan.zhihu.com/p/28179049)
- [Theoretical introduction paper](https://arxiv.org/pdf/1609.06782.pdf)