from django.urls import path

from .views import webhook

urlpatterns = [
    path(
        "webhooks/wallets_africa/aDshFhJjmIalgxCmXSj/",
         webhook,
         name = "webhook"
    ),
]