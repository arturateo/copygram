from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.serializers import PublicationsSerializer
from comments.models import Comments
from publications.models import Publications


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class PublicationsViewSet(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer


# class CommentsViewSet(viewsets.ModelViewSet):
#     queryset = Comments.objects.all()
    # serializer_class = CommentsSerializer
