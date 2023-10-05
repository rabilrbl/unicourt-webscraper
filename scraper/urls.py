from . import views
from django.urls import path

urlpatterns = [
    path('start_python_movie_scraping', views.python_movie_scrap)
]
