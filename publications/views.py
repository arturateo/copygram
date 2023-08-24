from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView

from comments.forms import CreateCommentForm
from comments.models import Comments
from publications.forms.publications_form import PublicationsForm
from publications.forms.search_form import SearchForm
from publications.models import Publications
from django.urls import reverse, reverse_lazy


# Create your views here.
class PublicationsList(ListView):
    model = Publications
    template_name = 'publications/publications_list.html'
    context_object_name = 'publications'
    ordering = ("-create_date",)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.user.is_authenticated:
            response.set_cookie('token', request.user.auth_token.key)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["comments"] = Comments.objects.all().order_by('-create_date')
        context["form"] = CreateCommentForm
        context["search_form"] = self.form
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)



class PublicationCreate(LoginRequiredMixin, CreateView):
    model = Publications
    form_class = PublicationsForm
    template_name = 'publications/publication_create.html'

    def form_valid(self, form):
        publications = form.save(commit=False)
        publications.author = self.request.user
        publications.save()
        return redirect("publications:publication_detail", pk=publications.pk)

    def get_success_url(self):
        return reverse("publications:publication_detail", kwargs={"pk": self.object.pk})


class PublicationDetail(DetailView):
    model = Publications
    template_name = 'publications/publications_detail.html'
    context_object_name = 'publication'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = CreateCommentForm
        context["comments"] = Comments.objects.all().order_by('-create_date')
        return context
