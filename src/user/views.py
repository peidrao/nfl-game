from http.client import HTTPResponse
from django.shortcuts import render
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from game.models import Match, Season
from team.models import Team
from user.models import GameWeek, SeasonProfile


class AccountView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/login/"
    template_name: str = "account/account.html"

    def get(self, request) -> HTTPResponse:
        context = {}
        try:
            team = request.user.teamprofile_set.all().first().team
            context["team"] = team
            context["teams"] = Team.objects.filter(division=team.division)
            context["matches"] = Match.objects.filter(Q(Q(home=team) | Q(away=team)))
            context["is_start"] = request.user.is_start
        except Exception as e:
            print(e)
        return render(request, self.template_name, context)


class StartSeasonView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        profile = request.user
        profile.is_start = True
        profile.save()
        team = profile.teamprofile_set.last()
        season = Season.objects.last()
        season_profile = SeasonProfile.objects.create(team=team, season=season)
        match = Match.objects.get(
            Q(Q(week__name="Week 1") & Q(Q(home=team.team) | Q(away=team.team)))
        )
        GameWeek.objects.create(season=season_profile, match=match)
        return Response({"message": "Season was created"}, status=status.HTTP_200_OK)
