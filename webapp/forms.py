from django import forms
from webapp.models import Album, Photo


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'author', 'data']



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['avatar', 'title', 'author', 'status' ]