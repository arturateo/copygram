from django.urls import path
from publications.views import PublicationsList, PublicationCreate

urlpatterns = [
    path('', PublicationsList.as_view(), name='publications'),
    path('publication_create/', PublicationCreate.as_view(), name='publication_create'),
]
