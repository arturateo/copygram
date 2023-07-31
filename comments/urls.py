from django.urls import path
from comments.views import CommentCreate, CommentDetailCreate

app_name = 'comments'

urlpatterns = [
    path('create_comments/<int:pk>/', CommentCreate.as_view(), name="create_comments"),
    path('create_detail_comments/<int:pk>/', CommentDetailCreate.as_view(), name="create_detail"),
]
