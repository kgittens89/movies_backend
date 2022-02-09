from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    movie_url = serializers.ModelSerializer.serializer_url_field(view_name='movie_detail')

    class Meta:
        model = Movie
        fields = ('title', 'genre', 'release_date', 'movie_poster', 'movie_url')
