import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, render_to_response
from backend.models import Movies, Movies_Shot

def index(request):
    return render_to_response('frontend/index+.html')

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
def drama_loss_plot_selection(request):
    return render_to_response('frontend/drama_loss_plot_selection.html')
def drama_kidnapping_plot_selection(request):
    return render_to_response('frontend/drama_kidnapping_plot_selection.html')
def comedy_surrealism_plot_selection(request):
    return render_to_response('frontend/comedy_surrealism_plot_selection.html')
def comedy_confusion_plot_selection(request):
    return render_to_response('frontend/comedy_confusion_plot_selection.html')
def comedy_relationship_plot_selection(request):
    return render_to_response('frontend/comedy_relationship_plot_selection.html')
def action_competition_plot_selection(request):
    return render_to_response('frontend/action_competition_plot_selection.html')
def action_war_plot_selection(request):
    return render_to_response('frontend/action_war_plot_selection.html')
def action_space_plot_selection(request):
    return render_to_response('frontend/action_space_plot_selection.html')


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
    movies_shots_captions = Movies_Shot.objects.filter(movies__genres=request.GET['genre']).values_list('caption').distinct()
    for caption in movies_shots_captions[0:20]:
        show_plots.append(caption[0])
    context = json.dumps({'msg':'finish', 'plots':show_plots})
    return HttpResponse(context, content_type='application/json')