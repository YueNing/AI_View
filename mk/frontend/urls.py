from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'frontend'
urlpatterns = [
    # ex: /mysample/
    #url(r'^$', views.index, name='index'),
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('go', views.index_go, name='index_go'),
    path('genres', views.genres_selected, name='genres_selected'),
    path('themes', views.themes_selected, name='themes_selected'),
    path('plots', views.plots_selected, name='plots_selected'),
    path('plots_1', views.plots_selected_1, name='plots_selected_1'),
    path('plots_2', views.plots_selected_2, name='plots_selected_2'),
    path('plots_3', views.plots_selected_3, name='plots_selected_3'),
    path('plots_4', views.plots_selected_4, name='plots_selected_4'),
    path('plots_5', views.plots_selected_5, name='plots_selected_5'),
    path('render', views.render_for_ai, name='render_for_ai'),
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
    path('render_result',views.render_result, name='render_result'),

]
