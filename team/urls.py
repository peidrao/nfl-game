
from django.urls import path

from team.views import SelectTeamView


urlpatterns = [
    path('api/select_team/', SelectTeamView.as_view(), name='select_team'),
]
