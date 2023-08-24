from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from comments.models import Comments
from publications.models import Publications


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]


class AuthorLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id"]


class CommentsSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        request = self.context['request']
        kwargs['comment_author'] = request.user
        super().save(**kwargs)

    class Meta:
        model = Comments
        fields = ['id', 'comment_author', 'publications', 'summary', 'create_date', 'update_date']
        read_only_fields = ("id", "comment_author", 'publications' "create_date", "update_date")


class PublicationsSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer(read_only=True)
    comments = CommentsSerializer(many=True, source='publications')
    like = SerializerMethodField()

    def save(self, **kwargs):
        request = self.context['request']
        kwargs['author'] = request.user
        super().save(**kwargs)

    class Meta:
        model = Publications
        fields = ['id', 'author', 'discriptions', 'photo', 'like', 'comments', 'create_date', 'update_date']
        read_only_fields = ("id", "author", 'like', 'comments', "create_date", "update_date")

    def get_like(self, instance):
        return instance.like.all().count()
