from django.db import models


# Create your models here.
class Publications(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='author',
                               verbose_name='Автор')
    discriptions = models.TextField(null=True, blank=True, max_length=300, verbose_name='Описание публикации')
    photo = models.ImageField(null=False, blank=False, upload_to='publications', verbose_name='Фото публикации')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'publications'
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.discriptions}'