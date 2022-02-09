from rest_framework import generics
# Create your views here.
from .models import Movie
# Import serializers
from .serializers import MovieSerializer
# Create your views here.

# api/movies/
# INDEX, POST
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# api/movies/id
# SHOW, PUT, DELETE
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer