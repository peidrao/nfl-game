from django.shortcuts import render
from rest_framework import views
from game.models import Match, Season
from team.models import Team, Conferency


class SeasonCreateView(views.APIView):

    def post(self, request):
