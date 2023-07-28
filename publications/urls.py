from django.urls import path
from publications.views import PublicationsList, PublicationCreate, PublicationDetail

app_name = 'publications'


urlpatterns = [
    path('', PublicationsList.as_view(), name='home'),
    path('publication_create/', PublicationCreate.as_view(), name='publication_create'),
    path('publication_detail/<int:pk>', PublicationDetail.as_view(), name='publication_detail'),
]
