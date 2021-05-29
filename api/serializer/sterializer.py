from rest_framework import serializers
from webapp.models import Album, Photo


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title', 'description', 'author', 'data']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['avatar', 'title', 'author', 'status']
