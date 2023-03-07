from django.urls import path

from user.views import AccountView, StartSeasonView


urlpatterns = [
    path("account/", AccountView.as_view(), name="account"),
    path("season/start/", StartSeasonView.as_view(), name="start_season"),
]
