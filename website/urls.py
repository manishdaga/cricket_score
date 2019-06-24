from django.urls import path
from website import views

urlpatterns = [
    path('',views.home,name='home-page'),
    path('news/',views.news,name='news-page'),
    path('news_desc/',views.news_desc,name='news_desc-page'),
    path('photo/',views.photo,name='photo-page'),
    path('score/',views.score,name='score-page'),
    path('team/',views.team,name='team-page'),
    path('video/',views.video,name='video-page'),
    path('live_score/',views.live_score,name='live_score-page'),
    path('widgets/',views.widgets,name='widgets-page'),
    
]
