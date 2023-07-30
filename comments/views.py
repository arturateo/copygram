from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from accounts.models import User
from comments.forms import CreateCommentForm
from publications.models import Publications


class CommentCreate(LoginRequiredMixin, CreateView):
    template_name = 'comments/comments_create.html'
    form_class = CreateCommentForm

    def form_valid(self, form):
        comment_author = self.request.user
        publications = get_object_or_404(Publications, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.comment_author = comment_author
        comment.publications = publications
        comment.save()
        return redirect("publications:home")
