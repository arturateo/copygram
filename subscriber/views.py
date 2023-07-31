from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from accounts.models import User


# Create your views here.

class SubscriptionView(View):

    def post(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        current_user.subscriber.add(user)
        return redirect("accounts:profile", user.pk)


class UnSubscriptionView(View):

    def post(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        current_user.subscriber.remove(user)
        return redirect("accounts:profile", user.pk)
