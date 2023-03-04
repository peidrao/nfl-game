from django.urls import path

from team.views import (
    ConferencesView,
    SelectTeamView,
    ConferecyByIDView,
    TeamsByConferenceView,
)


urlpatterns = [
    path("api/select_team/", SelectTeamView.as_view(), name="select_team"),
    path("conference/<id>", ConferecyByIDView.as_view(), name="conference_details"),
    path("conferences/", ConferencesView.as_view(), name="conferences"),
    path(
        "conferences/<int:conference_id>/teams/",
        TeamsByConferenceView.as_view(),
        name="teams_list",
    ),
]
