from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'mysample'
urlpatterns = [
    # ex: /mysample/
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
]
