from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from movie.views import MovieListView, MovieDetailsView

urlpatterns = [
    # URL to list all movie. ?page= for page number and &movie or ?movie for query for name and type of movie
    url(r'^$', MovieListView.as_view(), name="movie-list"),

    # URL for details of the movie
    url(r'^(?P<pk>.*)/$', MovieDetailsView.as_view(), name="movie-details"),

]