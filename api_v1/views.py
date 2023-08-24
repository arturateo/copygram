from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.permissions import IsAuthor
from api_v1.serializers import PublicationsSerializer, CommentsSerializer
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

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method == "POST":
            return [IsAuthenticated()]
        elif self.request.method is ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthor()]
        return super().get_permissions()

    @action(methods=["POST"], detail=True, url_path="likes", url_name="get_likes")
    def add_like(self, request, *args, **kwargs):
        publications = self.get_object()
        publications.like.add(request.user)
        return Response({"likes": publications.get_total_like()})

    @action(methods=["DELETE"], detail=True, url_path="unlikes", url_name="un_likes")
    def delete_like(self, request, *args, **kwargs):
        publications = self.get_object()
        publications.like.remove(request.user)
        return Response({"likes": publications.get_total_like()})


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
