from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import PhotoViewSet, AlbumViewSet

app_name = 'api'

api_router = DefaultRouter()
api_router.register('photo', PhotoViewSet)
api_router.register('album', AlbumViewSet)


urlpatterns = [
    path('', include(api_router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')
]