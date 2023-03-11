from http.client import HTTPResponse
from django.shortcuts import render
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.domain.models.match import Match, GameMatchWeek
from app.domain.models.season import Season, SeasonProfile
from app.domain.models.team import Team


class AccountView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/login/"
    template_name: str = "account/account.html"

    def get(self, request) -> HTTPResponse:
        context = {}
        try:
            profile = request.user.teamprofile_set.all().first()
            context["team"] = profile.team
            query = Q(Q(home=profile.team) | Q(away=profile.team))
            context["teams"] = Team.objects.filter(division=profile.team.division)
            context["matches"] = Match.objects.filter(query)
            context["is_start"] = request.user.is_start
            context["match"] = GameMatchWeek.objects.filter(
                season=profile.seasonprofile_set.last()
            ).last()
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
        GameMatchWeek.objects.create(season=season_profile, match=match)
        return Response({"message": "Season was created"}, status=status.HTTP_200_OK)
