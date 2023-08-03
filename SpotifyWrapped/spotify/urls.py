from django.urls import include, path
from . import views

urlpatterns = [
    path('home/', views.authorise),
    path('', views.home),
    path('tracks/', views.recent),
    path('song/filter/', views.recent),
    path('album/', views.albums),
    path('artist/', views.artist),
    path('genre/', views.genre),
    path('recommendation/', views.recommendation),
]