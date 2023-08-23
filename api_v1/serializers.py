from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from publications.models import Publications


class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = "__all__"
        read_only_fields = ("id", "author", "created_at", "updated_at")