from .models import MoviesDetails
from .serializers import MoviesDetailsSerializer
from rest_framework.generics import ListAPIView


class MoviesDetailsModelViewSet(ListAPIView):
    queryset = MoviesDetails.objects.all()
    serializer_class = MoviesDetailsSerializer
    filterset_fileds = ['released_year']



