from django.urls import path
from app.api.views.user import ProfileCreateView

from app.views.index import HomeView, LoginView, LogoutView
from app.views.conference import (
    ConferecyByIDView,
    ConferencesView,
    TeamsByConferenceView,
)
from app.views.user import AccountView, StartSeasonView


urlpatterns = [
    # Home
    path("", HomeView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Conference
    path("conference/<id>", ConferecyByIDView.as_view(), name="conference_details"),
    path("conferences/", ConferencesView.as_view(), name="conferences"),
    path(
        "conferences/<int:conference_id>/teams/",
        TeamsByConferenceView.as_view(),
        name="teams_list",
    ),
    # User
    path("account/", AccountView.as_view(), name="account"),
    path("season/start/", StartSeasonView.as_view(), name="start_season"),
    path("api/profile/", ProfileCreateView.as_view(), name="profile"),
]
