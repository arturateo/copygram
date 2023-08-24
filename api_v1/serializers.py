from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from publications.models import Publications


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]


class AuthorLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id"]


class PublicationsSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer(read_only=True)
    like = SerializerMethodField()

    def save(self, **kwargs):
        request = self.context['request']
        kwargs['author'] = request.user
        super().save(**kwargs)

    class Meta:
        model = Publications
        fields = ['id', 'author', 'discriptions', 'photo', 'like', 'create_date', 'update_date']
        read_only_fields = ("id", "author", 'like', "create_date", "update_date")

    def get_like(self, instance):
        return instance.like.all().count()
