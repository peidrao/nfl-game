
from django.urls import path

from game.views import SeasonCreateView


urlpatterns = [
    path('season/start', SeasonCreateView.as_view(), name='season_start'),
]
