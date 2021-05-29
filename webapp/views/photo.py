
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Album, Photo, PhotoUser
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import AlbumForm, PhotoForm
# from webapp.base_view import CustomFormView, CustomListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    template_name = 'photo/photo_index.html'
    model = Photo
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        photos_id = []
        for photo_id in PhotoUser.objects.filter(user=user):
            photos_id.append(photo_id.photo.pk)
        context['favorite_photos'] = photos_id

        return context

    def get_queryset(self):
        return Photo.objects.filter(review__user_id=self.request.user.pk).order_by('-check_in')



class PhotoView(DetailView):
    template_name = 'photo/photo_view.html'
    model = Photo
    context_object_name = 'photo'


class CreatePhotoView(CreateView):
    template_name = 'photo/photo_create.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        photo = form.save(commit=False)
        photo.album = album
        photo.save()
        form.save_m2m()

        return redirect('photo-view', pk=photo.pk)

    def get_success_url(self):
        return reverse('photo-view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Photo
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('photo-view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    context_object_name = 'photo'
    permission_required = 'webapp.delete_photo'

    success_url = reverse_lazy('photo-list')

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()






