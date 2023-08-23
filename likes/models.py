from django.db import models

# Create your models here.
# class LikedUsers(models.Model):
#     liked_count = models.IntegerField(default=0),
#     post = models.ForeignKey(Post, related_name='likedusers', on_delete=models.CASCADE),
#     user = models.ForeignKey(User, related_name='likedusers', on_delete=models.CASCADE),