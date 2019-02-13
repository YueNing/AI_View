import json
import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, render_to_response
from backend.models import Movies, Movies_Shot
from backend import concat, concatekev
selected_plots_id = []

def index(request):
    return render_to_response('frontend/index.html')

def genre_selection(request):
    genres = ['Action', 'Drama', 'Comedy']
    content = {'genres':genres}
    return render_to_response('frontend/genre_selection.html', content)

def action_theme_selection(request):
    return render_to_response('frontend/action_theme_selection.html')
def drama_theme_selection(request):
    return render_to_response('frontend/drama_theme_selection.html')
def comedy_theme_selection(request):
    return render_to_response('frontend/comedy_theme_selection.html')

# finished
def drama_identity_crisis_plot_selection(request):
    return render_to_response('frontend/drama_identity_crisis_plot_selection.html')
def drama_identity_crisis_despair(request):
    render_url = concatekev.main('despair')
    return render_to_response('frontend/videosplay.html',{'url':render_url, 'title':'drama_identity_crisis_despair'})
def drama_identity_crisis_resolution(request):
    render_url = concatekev.main('resolution')
    return render_to_response('frontend/videosplay.html',{'url':render_url, 'title':'drama_identity_crisis_resolution'})
def drama_identity_crisis_knowledge_moment(request):
    render_url = concatekev.main('knowledge moment')
    return render_to_response('frontend/videosplay.html',{'url':render_url, 'title':'drama_identity_crisis_knowledge_moment'})

# finished
def drama_loss_plot_selection(request):
    return render_to_response('frontend/drama_loss_plot_selection.html')
def drama_loss_getup(request):
    render_url = concatekev.main('get up')
    return render_to_response('frontend/videosplay.html',{'url':render_url, 'title':'drama_loss_getup'})
def drama_loss_death(request):
    render_url = concatekev.main('death')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'drama_loss_death'})
def drama_loss_discussion(request):
    render_url = concatekev.main('discussion')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'drama_loss_discussion'})

# finished
def drama_kidnapping_plot_selection(request):
    return render_to_response('frontend/drama_kidnapping_plot_selection.html')
def drama_kidnapping_car_ride(request):
    render_url = concatekev.main('car rode')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'drama_kidnapping_car_ride'})
def drama_kidnapping_phone_call(request):
    render_url = concatekev.main('phone call')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'drama_kidnapping_phone_call'})
def drama_kidnapping_dramatic_reunion(request):
    render_url = concatekev.main('dramatic reunion')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'drama_kidnapping_dramatic_reunion'})

# finished
def comedy_surrealism_plot_selection(request):
    return render_to_response('frontend/comedy_surrealism_plot_selection.html')
def comedy_surrealism_shapes(request):
    render_url = concatekev.main('shapes')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'comedy_surrealism_shapes'})
def comedy_surrealism_colors(request):
    render_url = concatekev.main('colors')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'comedy_surrealism_colors'})

# finished      
def comedy_confusion_plot_selection(request):
    return render_to_response('frontend/comedy_confusion_plot_selection.html')
def comedy_confusion_a_object(request):
    render_url = concatekev.main('a object')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'comedy_confusion_a_object'})
def comedy_confusion_a_person(request):
    render_url = concatekev.main('a person')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'comedy_confusion_a_person'})

# finished
def comedy_relationship_plot_selection(request):
    return render_to_response('frontend/comedy_relationship_plot_selection.html')
def comedy_relationship_get_to_know(request):
    render_url = concatekev.main('get-to-know') 
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'comedy_relationship_get_to_know'})
def comedy_relationship_forced_situation(request):
    render_url = concatekev.main('forced situation')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'comedy_relationship_forced_situation'})    

# finished
def action_competition_plot_selection(request):
    return render_to_response('frontend/action_competition_plot_selection.html')
def action_competition_win(request):
    render_url = concatekev.main('win')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_competition_win'})    
def action_competition_lose(request):
    render_url = concatekev.main('lose')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_competition_lose'})    
def action_competition_car_chase(request):
    render_url = concatekev.main('car chase')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_competition_car_chase'})    

# finished
def action_war_plot_selection(request):
    return render_to_response('frontend/action_war_plot_selection.html')
def action_war_attack(request):
    render_url = concatekev.main('attack')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_war_attack'})    
def action_war_climax(request):
    render_url = concatekev.main('climax')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_war_climax'})    
def action_war_make_a_plan(request):
    render_url = concatekev.main('make a plan')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_war_make_a_plan'})    
    
def action_space_plot_selection(request):
    return render_to_response('frontend/action_space_plot_selection.html')
def action_space_no_return(request):
    render_url = concatekev.main('no return')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_space_no_return'})    
def action_space_aliens_attack(request):
    render_url = concatekev.main('aliens attack')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_space_aliens_attack'})    
def action_space_missing_your_family(request):
    render_url = concatekev.main('missing your family')
    return render_to_response('frontend/videosplay.html', {'url':render_url, 'title':'action_space_missing_your_family'})    

def render_result(request):
    import pdb
    opt = {'output_dir':'static/', 'user_id':'admin', 'movie_shots':[]}
    genre = request.GET['genre']
    theme = request.GET['theme']
    plot = request.GET['plot']
    shots = Movies_Shot.objects.filter(genre=genre)
    if len(shots)>=7:
        show_shots = random.sample(set(shots), 7)
    else:
        show_shots = shots
    for show_shot in show_shots:
        opt['movie_shots'].append(show_shot.video_url) 
    render_url = concat(opt)
    content = {'render_url':render_url}
    return render_to_reponse('frontend/render_result.html', content)


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
