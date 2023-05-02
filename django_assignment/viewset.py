from rest_framework import viewsets, filters
from .models import Work, Artist
from .serializers import WorkSerializer, ArtistSerializer, RegistrationSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['work_type', 'link']

    def get_queryset(self):
        queryset = self.queryset
        artist_name = self.request.query_params.get('artist')
        work_type = self.request.query_params.get('work_type')

        if artist_name:
            queryset = queryset.filter(artist__name=artist_name)
        elif work_type:
            queryset = queryset.filter(work_type=work_type)

        return queryset


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
