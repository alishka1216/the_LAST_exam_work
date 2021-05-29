from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from webapp.views import (
    IndexView,
    PhotoView,
    PhotoUpdateView,
    PhotoDeleteView,
    CreatePhotoView,
    AlbumList,
    AlbumView,
    AlbumCreate,
    AlbumUpdate,
    AlbumDelete,
)
from webapp.views.like import (
    AddPhoto,
    RemovePhoto,
    AddAlbum,
    RemoveAlbum
)
app_name = 'article'

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('photo/', IndexView.as_view(), name='photo-list'),
    path('photo/add/<int:pk>/', CreatePhotoView.as_view(), name='photo-add'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo-view'),
    path('photo/update/<int:pk>/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('', AlbumList.as_view(), name='album-list'),
    path('album/<int:pk>/', AlbumView.as_view(), name='album-view'),
    path('album/add/', AlbumCreate.as_view(), name='album-add'),
    path('album/update/<int:pk>/', AlbumUpdate.as_view(), name='album-update'),
    path('album/delete/<int:pk>/', AlbumDelete.as_view(), name='album-delete'),
    path('<int:pk>/Addalbum/', AddAlbum.as_view(), name='album_like'),
    path('<int:pk>/RemoveAlbum/', RemoveAlbum.as_view(), name='album_unlike'),
    path('<int:pk>/AddPhoto/', AddPhoto.as_view(), name='photo_like'),
    path('<int:pk>/RemovePhoto/', RemovePhoto.as_view(), name='photo_unlike'),
    path('accounts/', include('accounts.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
