import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, render_to_response
from backend.models import Movies, Movies_Shot
from backend import concat
selected_plots_id = []

def index(request):
    return render_to_response('frontend/index.html')

def genre_selection(request):
    return render_to_response('frontend/genre_selection.html')

def action_theme_selection(request):
    return render_to_response('frontend/action_theme_selection.html')
def drama_theme_selection(request):
    return render_to_response('frontend/drama_theme_selection.html')
def comedy_theme_selection(request):
    return render_to_response('frontend/comedy_theme_selection.html')

def drama_identity_crisis_plot_selection(request):
    return render_to_response('frontend/drama_identity_crisis_plot_selection.html')

def drama_identity_crisis_despair(request):
    return render_to_response('frontend/videosplay.html',{'url':'001.mp4', 'title':'drama_identity_crisis_despair'})
def drama_identity_crisis_resolution(request):
    return render_to_response('frontend/videosplay.html',{'url':'001.mp4', 'title':'drama_identity_crisis_resolution'})
def drama_identity_crisis_knowledge_moment(request):
    return render_to_response('frontend/videosplay.html',{'url':'001.mp4', 'title':'drama_identity_crisis_knowledge_moment'})

def drama_loss_plot_selection(request):
    return render_to_response('frontend/drama_loss_plot_selection.html')

def drama_loss_getup(request):
    return render_to_response('frontend/videosplay.html',{'url':'001.mp4', 'title':'drama_loss_getup'})

def drama_loss_death(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'drama_loss_death'})

def drama_loss_discussion(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'drama_loss_discussion'})

def drama_kidnapping_plot_selection(request):
    return render_to_response('frontend/drama_kidnapping_plot_selection.html')

def drama_kidnapping_car_ride(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'drama_kidnapping_car_ride'})
def drama_kidnapping_phone_call(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'drama_kidnapping_phone_call'})
def drama_kidnapping_dramatic_reunion(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'drama_kidnapping_dramatic_reunion'})

def comedy_surrealism_plot_selection(request):
    return render_to_response('frontend/comedy_surrealism_plot_selection.html')
def comedy_surrealism_shapes(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'comedy_surrealism_shapes'})
def comedy_surrealism_colors(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'comedy_surrealism_colors'})
      
def comedy_confusion_plot_selection(request):
    return render_to_response('frontend/comedy_confusion_plot_selection.html')
def comedy_confusion_a_object(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'comedy_confusion_a_object'})
def comedy_confusion_a_person(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'comedy_confusion_a_person'})


def comedy_relationship_plot_selection(request):
    return render_to_response('frontend/comedy_relationship_plot_selection.html')
def comedy_relationship_get_to_know(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'comedy_relationship_get_to_know'})
def comedy_relationship_forced_situation(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'comedy_relationship_forced_situation'})    

def action_competition_plot_selection(request):
    return render_to_response('frontend/action_competition_plot_selection.html')
def action_competition_win(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_competition_win'})    
def action_competition_lose(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_competition_lose'})    
def action_competition_car_chase(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_competition_car_chase'})    

def action_war_plot_selection(request):
    return render_to_response('frontend/action_war_plot_selection.html')
def action_war_attack(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_war_attack'})    
def action_war_climax(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_war_climax'})    
def action_war_make_a_plan(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_war_make_a_plan'})    
    
def action_space_plot_selection(request):
    return render_to_response('frontend/action_space_plot_selection.html')
def action_space_no_return(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_space_no_return'})    
def action_space_aliens_attack(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_space_aliens_attack'})    
def action_space_missing_your_family(request):
    return render_to_response('frontend/videosplay.html', {'url':'001.mp4', 'title':'action_space_missing_your_family'})    

def index_particle(request):
    return render_to_response('frontend/index_particle.html')

def index_go(request):
    show_genres = []
    genres = Movies.objects.values('genres')
    for genre in genres:
        for key, value in genre.items():
            if value not in show_genres:
                show_genres.append(value)
    context = json.dumps({'genres':show_genres})
    return render(request, 'frontend/index_go.html',{"context":context})

def genres_selected(request):
    # show_themes = ['space', 'war', 'hhhh']
    show_themes = []
    show_themes_database = Movies.objects.filter(genres=request.GET['genre']).values_list('themes')
    for theme in show_themes_database:
        show_themes.append(theme[0])
    context = json.dumps({'themes':show_themes, 'genre':request.GET['genre'], 'msg':'true'})
    return HttpResponse(context, content_type='application/json')

def themes_selected(request):
    show_plots = []
    show_plots_id = []
    genre = request.GET['genre']
    movies_shots = Movies_Shot.objects.filter(movies__genres=genre).values_list('caption', 'id').distinct()
    for caption in movies_shots[0:20]:
        show_plots.append(caption[0])
        show_plots_id.append(caption[1])
    context = json.dumps({'msg':'finish', 'genre':genre, 'plots':show_plots, 'plots_id':show_plots_id})
    return HttpResponse(context, content_type='application/json')

def plots_selected(request):
    selected_plots_id = []
    show_plots = []
    show_plots_id = []
    genre = request.GET['genre']
    time = 5
    selected_plots_id = request.GET['selected_id']
    movies_shots = Movies_Shot.objects.filter(movies__genres=genre).values_list('caption', 'id', 'start_time', 'end_time').distinct()
    for caption in movies_shots[20:40]:
        show_plots.append(caption[0])
        show_plots_id.append(caption[1])
    # show_plots_id = ['780', '790']
    # show_plots = ['test1','test2']
    context = json.dumps({'msg':'set plots', 'plots':show_plots, 'plots_id':show_plots_id, 'genre':request.GET['genre'], 'selected_plots_id':selected_plots_id, 'time':time})
    # import pdb
    # pdb.set_trace()
    return HttpResponse(context, content_type='application/json')

def plots_selected_1(request):
    selected_plots_id = []
    show_plots = []
    show_plots_id = []
    genre = request.GET['genre']
    time = 5
    selected_plots_id = request.GET['selected_id']
    movies_shots = Movies_Shot.objects.filter(movies__genres=genre).values_list('caption', 'id').distinct()
    for caption in movies_shots[20:40]:
        show_plots.append(caption[0])
        show_plots_id.append(caption[1])
    old_id = request.GET['old_id']
    # show_plots_id = ['780', '790']
    # show_plots = ['test1','test2']
    context = json.dumps({'msg':'set plots', 'plots':show_plots, 'plots_id':show_plots_id, 'genre':request.GET['genre'], 'selected_plots_id':[selected_plots_id,old_id], 'time':time})
    # import pdb
    # pdb.set_trace()
    return HttpResponse(context, content_type='application/json')

def plots_selected_2(request):
    selected_plots_id = []
    time = 5
    selected_plots_id = request.GET['selected_id']
    old_id_1 = request.GET['old_id_1']
    old_id_2 = request.GET['old_id_2']
    show_plots_id = ['750', '760']
    show_plots = ['test1','test2']
    context = json.dumps({'msg':'set plots', 'plots':show_plots, 'plots_id':show_plots_id, 'genre':request.GET['genre'],
                                 'selected_plots_id':[selected_plots_id,old_id_1,old_id_2], 'time':time})
    return HttpResponse(context, content_type='application/json')

def plots_selected_3(request):
    selected_plots_id = []
    time = 5
    selected_plots_id = request.GET['selected_id']
    old_id_1 = request.GET['old_id_1']
    old_id_2 = request.GET['old_id_2']
    old_id_3 = request.GET['old_id_3']
    show_plots_id = ['750', '760']
    show_plots = ['test1','test2']
    context = json.dumps({'msg':'set plots', 'plots':show_plots, 'plots_id':show_plots_id, 'genre':request.GET['genre'],
                         'selected_plots_id':[selected_plots_id,old_id_1, old_id_2,old_id_3], 'time':time})
    # import pdb
    # pdb.set_trace()
    return HttpResponse(context, content_type='application/json')

def plots_selected_4(request):
    selected_plots_id = []
    time = 5
    selected_plots_id = request.GET['selected_id']
    old_id_1 = request.GET['old_id_1']
    old_id_2 = request.GET['old_id_2']
    old_id_3 = request.GET['old_id_3']
    old_id_4 = request.GET['old_id_4']
    show_plots_id = ['750', '760']
    show_plots = ['test1','test2']
    context = json.dumps({'msg':'set plots', 'plots':show_plots, 'plots_id':show_plots_id, 'genre':request.GET['genre'], 
                            'selected_plots_id':[selected_plots_id,old_id_1, old_id_2, old_id_3, old_id_4], 'time':time})
    # import pdb
    # pdb.set_trace()
    return HttpResponse(context, content_type='application/json')

def plots_selected_5(request):
    selected_plots_id = []
    time = 5
    selected_plots_id = request.GET['selected_id']
    old_id_1 = request.GET['old_id_1']
    old_id_2 = request.GET['old_id_2']
    old_id_3 = request.GET['old_id_3']
    old_id_4 = request.GET['old_id_4']
    old_id_5 = request.GET['old_id_5']
    show_plots_id = ['750', '760']
    show_plots = ['test1','test2']
    context = json.dumps({'msg':'set plots', 'plots':show_plots, 'plots_id':show_plots_id, 'genre':request.GET['genre'],
                         'selected_plots_id':[selected_plots_id, old_id_1, old_id_2, old_id_3, old_id_4, old_id_5], 'time':time})
    # import pdb
    # pdb.set_trace()
    return HttpResponse(context, content_type='application/json')

def render_for_ai(request):
    render_url = '../../../../data/key_source_videos/tt1477834.mp4'
    opt = {'output_dir':'static/', 'user_id':'admin', 'movie_shots':[]}
    # import pdb
    # pdb.set_trace()
    ids = request.GET['plots_id']
    ids = json.loads(ids)
    for id in ids:
        tmp_url = Movies_Shot.objects.filter(id=id).values('video_url')
        opt['movie_shots'].append(tmp_url[0]['video_url'])
    render_url = concat.main(opt)
    context = json.dumps({'msg':'finish', 'render_url':render_url})
    return HttpResponse(context, content_type='application/json')