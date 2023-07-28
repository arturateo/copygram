from urllib.parse import urlencode

from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView

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

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        # if self.search_value:
        #     queryset = queryset.filter(author__icontains=self.search_value)
        return queryset


class PublicationCreate(CreateView):
    model = Publications
    form_class = PublicationsForm
    template_name = 'publications/publication_create.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.author = self.request.user
        project.save()
        return redirect("publications")
        # , pk=project.pk)

    def get_success_url(self):
        return reverse("publications:home")
        # , kwargs={"pk": self.object.pk})


class PublicationDetail(DetailView):
    model = Publications
    template_name = 'publications/publications_detail.html'
    context_object_name = 'publication'
