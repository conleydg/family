from rest_framework import serializers
from .models import Movie, Tag, People

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'video', 'movie_date',
                  'upload_date', 'title')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('movie', 'tag')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = People
        fields = ('movie', 'person')
