from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


status_choices = [('public', 'публичная'), ('private', 'приватная')]


class Photo(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='подпись')
    author = models.ForeignKey(
        get_user_model(),
        blank=True,
        null=True,
        related_name='photo_author',
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(
        upload_to='avatars',
        null=False,
        blank=False,
        verbose_name='Картинка продукта'
    )
    album = models.ForeignKey('webapp.Album', blank=False, null=False,  related_name='album_photos', on_delete=models.CASCADE, verbose_name='Альбом к фотографии')
    status = models.CharField(max_length=50,
                              null=False,
                              blank=False,
                              choices=status_choices,
                              default='public', verbose_name='статус')

    class Meta:
        db_table = 'photo'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.title


class Album(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(
        get_user_model(),
        related_name='album_author',
        blank=True,
        null=True,
        verbose_name='Автор альбома',
        on_delete=models.CASCADE
    )
    data = models.DateField(null=False, blank=False)

    class Meta:
        db_table = 'album'
        verbose_name = 'Альбомы'
        verbose_name_plural = 'Альбом'

    def __str__(self):
        return self.title

class PhotoUser(BaseModel):
    photo = models.ForeignKey("webapp.Photo", on_delete=models.CASCADE, related_name="PhotoUser")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="PhotoUser")

    class Meta:
        verbose_name = 'Избранное(фото)'
        verbose_name_plural = 'Избранные(фото)'

    def str(self):
        return "Id photo: {}. User: {}".format(self.photo_id, self.user)


class AlbumUser(BaseModel):
    album = models.ForeignKey("webapp.Album", on_delete=models.CASCADE, related_name="AlbumUser")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="AlbumUser")

    class Meta:
        verbose_name = 'Избранное(альбом)'
        verbose_name_plural = 'Избранные(альбом)'

    def str(self):
        return "Id album: {}. User: {}".format(self.album_id, self.user)

