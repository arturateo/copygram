from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, ProfileView
from comments.views import CommentCreate

app_name = 'comments'

urlpatterns = [
    path('create_comments/<int:pk>/', CommentCreate.as_view(), name="create_comments"),
]

