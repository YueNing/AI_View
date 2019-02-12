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
    
    # finished
    path('drama_identity_crisis_plot_selection',views.drama_identity_crisis_plot_selection, name='drama_identity_crisis_plot_selection'),
    path('drama_identity_crisis_knowledge_moment',views.drama_identity_crisis_knowledge_moment, name='drama_identity_crisis_knowledge_moment'),
    path('drama_identity_crisis_resolution',views.drama_identity_crisis_resolution, name='drama_identity_crisis_resolution'),
    path('drama_identity_crisis_despair',views.drama_identity_crisis_despair, name='drama_identity_crisis_despair'),
    # finished
    path('drama_loss_plot_selection',views.drama_loss_plot_selection, name='drama_loss_plot_selection'),
    path('drama_loss_getup',views.drama_loss_getup, name='drama_loss_getup'),
    path('drama_loss_death',views.drama_loss_death, name='drama_loss_death'),
    path('drama_loss_discussion',views.drama_loss_discussion, name='drama_loss_discussion'),
    # finished
    path('drama_kidnapping_plot_selection',views.drama_kidnapping_plot_selection, name='drama_kidnapping_plot_selection'),
    path('drama_kidnapping_dramatic_reunion',views.drama_kidnapping_dramatic_reunion, name='drama_kidnapping_dramatic_reunion'),
    path('drama_kidnapping_car_ride',views.drama_kidnapping_car_ride, name='drama_kidnapping_car_ride'),
    path('drama_kidnapping_phone_call',views.drama_kidnapping_phone_call, name='drama_kidnapping_phone_call'),
    # finished
    path('comedy_surrealism_plot_selection',views.comedy_surrealism_plot_selection, name='comedy_surrealism_plot_selection'),
    path('comedy_surrealism_shapes',views.comedy_surrealism_shapes, name='comedy_surrealism_shapes'),
    path('comedy_surrealism_colors',views.comedy_surrealism_colors, name='comedy_surrealism_colors'),
    # finished
    path('comedy_confusion_plot_selection',views.comedy_confusion_plot_selection, name='comedy_confusion_plot_selection'),
    path('comedy_confusion_a_object',views.comedy_confusion_a_object, name='comedy_confusion_a_object'),
    path('comedy_confusion_a_person',views.comedy_confusion_a_person, name='comedy_confusion_a_person'),
    # finished
    path('comedy_relationship_plot_selection',views.comedy_relationship_plot_selection, name='comedy_relationship_plot_selection'),
    path('comedy_relationship_get_to_know',views.comedy_relationship_get_to_know, name='comedy_relationship_get_to_know'),
    path('comedy_relationship_forced_situation',views.comedy_relationship_forced_situation, name='comedy_relationship_forced_situation'),
    # finished
    path('action_competition_plot_selection',views.action_competition_plot_selection, name='action_competition_plot_selection'),
    path('action_competition_win',views.action_competition_win, name='action_competition_win'),
    path('action_competition_lose',views.action_competition_lose, name='action_competition_lose'),
    path('action_competition_car_chase',views.action_competition_car_chase, name='action_competition_car_chase'),
    # finished
    path('action_war_plot_selection',views.action_war_plot_selection, name='action_war_plot_selection'),
    path('action_war_attack',views.action_war_attack, name='action_war_attack'),
    path('action_war_climax',views.action_war_climax, name='action_war_climax'),
    path('action_war_make_a_plan',views.action_war_make_a_plan, name='action_war_make_a_plan'),
    # finished
    path('action_space_plot_selection',views.action_space_plot_selection, name='action_space_plot_selection'),
    path('action_space_no_return',views.action_space_no_return, name='action_space_no_return'),
    path('action_space_aliens_attack',views.action_space_aliens_attack, name='action_space_aliens_attack'),
    path('action_space_missing_your_family',views.action_space_missing_your_family, name='action_space_missing_your_family'),

]
