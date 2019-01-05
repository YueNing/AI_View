from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'frontend'
urlpatterns = [
    # ex: /mysample/
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('genre_selection',views.genre_selection, name='genre_selection'),
    path('action_theme_selection',views.action_theme_selection, name='action_theme_selection'),
    path('comedy_theme_selection',views.comedy_theme_selection, name='comedy_theme_selection'),
    path('drama_theme_selection',views.drama_theme_selection, name='drama_theme_selection'),
    path('drama_identity_crisis_plot_selection',views.drama_identity_crisis_plot_selection, name='drama_identity_crisis_plot_selection'),
    path('drama_loss_plot_selection',views.drama_loss_plot_selection, name='drama_loss_plot_selection'),
    path('drama_kidnapping_plot_selection',views.drama_kidnapping_plot_selection, name='drama_kidnapping_plot_selection'),
    path('comedy_surrealism_plot_selection',views.comedy_surrealism_plot_selection, name='comedy_surrealism_plot_selection'),
    path('comedy_confusion_plot_selection',views.comedy_confusion_plot_selection, name='comedy_confusion_plot_selection'),
    path('comedy_relationship_plot_selection',views.comedy_relationship_plot_selection, name='comedy_relationship_plot_selection'),
    path('action_competition_plot_selection',views.action_competition_plot_selection, name='action_competition_plot_selection'),
    path('action_war_plot_selection',views.action_war_plot_selection, name='action_war_plot_selection'),
    path('action_space_plot_selection',views.action_space_plot_selection, name='action_space_plot_selection'),

]
