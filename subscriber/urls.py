from django.urls import path

from subscriber.views import SubscriptionView, UnSubscriptionView

app_name = 'subscription'

urlpatterns = [
    path('add/<int:pk>', SubscriptionView.as_view(), name='subscription'),
    path('delete/<int:pk>', UnSubscriptionView.as_view(), name='unsubscription'),
]
