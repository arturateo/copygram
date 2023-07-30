# Generated by Django 4.2.2 on 2023-07-30 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0004_alter_publications_author_alter_publications_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]