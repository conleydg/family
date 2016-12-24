from rest_framework import serializers
from .models import Movie, Tag, People

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('url', 'id', 'video', 'movie_date',
                  'upload_date', 'title', 'description')

class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('url', 'movie', 'tag')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = People
        fields = ('url', 'movie', 'person')
