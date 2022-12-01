from django.urls import path, include
from .views import index, show_articles, showarticle, show_topics, send_input_data, create_topic, create_article
from .views import show_cat, show_cake, show_socialising, show_computer, show_water,show_weeds

app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('topics', show_topics, name='topics'),
    path('input', send_input_data, name='input'),
    path('topic/add', create_topic, name='add_topic'),
    path('article/create', create_article, name='create_article'),
    path('article/show', show_articles, name='show_articles'),
    path('cat', show_cat, name='show_cat'),
    path('cake', show_cake, name='show_cake'),
    path('socialising', show_socialising, name='show_socialising'),
    path('computer', show_computer, name='show_computer'),
    path('water', show_water, name='show_underwater'),
    path('weeds', show_weeds, name='show_weeds'),
]
