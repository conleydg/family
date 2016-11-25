from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from .models import Movie, Tag, People
from .serializers import MovieSerializer, TagSerializer, PeopleSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer





def index(request):
    context = {'movies':Movie.objects.all()}
    return render(request, 'conley/index.html', context)

def movie_screen(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {'movie':movie}
    return render(request, 'conley/movie_screen.html', context)
