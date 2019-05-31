from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
from movie.models import Movie
class MovieListView(ListView):
    model = Movie
    template_name = "movie/index.html"
    queryset = Movie.objects.all()
    #limit 10 movies per page /?page=1
    paginate_by = 10

    def get_queryset(self):
        qs = Movie.objects.all();
        query = self.request.GET.get('movie')
        if query is not None:
            qs = qs.filter(
                # query for name of movie
                Q(name__icontains=query) |
                # query for type of movie
                Q(type__name__icontains=query)
            )
        return qs

class MovieDetailsView(DetailView):
    template_name = "movie/details.html"
    queryset = Movie.objects.all()

