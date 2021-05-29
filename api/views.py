# from api.permissions import CustomerAccessPermission

from api.serializer.sterializer import PhotoSerializer, AlbumSerializer
from webapp.models import Photo, Album
from rest_framework.viewsets import ModelViewSet
from api.serializer import sterializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    IsAuthenticatedOrReadOnly = [IsAuthenticatedOrReadOnly]
    # permission_classes = [CustomerAccessPermission]


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    IsAuthenticatedOrReadOnly = [IsAuthenticatedOrReadOnly]
    # permission_classes = [CustomerAccessPermission]