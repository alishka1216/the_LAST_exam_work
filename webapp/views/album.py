from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Album, Photo
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import AlbumForm, PhotoForm
# from webapp.base_view import CustomFormView, CustomListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class AlbumList(ListView):
    template_name = 'album/album_index.html'
    model = Album
    context_object_name = 'albums'
    ordering = ('title',)
    paginate_by = 5



class AlbumView(DetailView):
    template_name = 'album/album_view.html'
    model = Album
    context_object_name = 'album'


class AlbumCreate(CreateView):
    template_name = 'album/album_create.html'
    model = Album
    form_class = AlbumForm

    def get_success_url(self):
        return reverse('album-view', kwargs={'pk': self.object.pk})


class AlbumUpdate(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'album/album_update.html'
    form_class = AlbumForm
    context_object_name = 'album'
    permission_required = 'webapp.change_album'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()




    def get_success_url(self):
        return reverse('album-view', kwargs={'pk': self.object.pk})


class AlbumDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'album/album_delete.html'
    model = Album
    context_object_name = 'album'
    permission_required = 'webapp.delete_album'

    success_url = reverse_lazy('album-list')

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()


