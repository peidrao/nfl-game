from django.urls import path

from user.views import AccountView


urlspatterns = [
    path("account/", AccountView.as_view(), name="account"),
]
