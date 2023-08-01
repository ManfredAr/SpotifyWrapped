from django.urls import include, path
from . import views

urlpatterns = [
    path('home/', views.authorise),
    path('', views.home),
    path('tracks/', views.recent),
    path('song/filter/', views.recent)
]