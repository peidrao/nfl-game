from django.urls import path

from index.views import (
    HomeView,
    LoginView,
    AccountView,
    ConferencesView,
    TeamsListView,
    LogoutView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("account/", AccountView.as_view(), name="account"),
    path("conferences/", ConferencesView.as_view(), name="conferences"),
    path(
        "conferences/<int:conference_id>/teams/",
        TeamsListView.as_view(),
        name="teams_list",
    ),
]
