from django.urls import path, include

from . import views

app_name = 'shop'

urlpatterns = [
path('', views.index, name='index'),
path('games', views.get_games, name='games'),
path('html', views.get_html, name='html'),


]
