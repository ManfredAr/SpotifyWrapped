from django.urls import include, path
from . import views

urlpatterns = [
    path('home/', views.authorise),
    path('', views.home),
    path('recent/', views.recent)
]