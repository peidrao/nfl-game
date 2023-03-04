from django.views import generic
from django.shortcuts import render

from rest_framework import views, status
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin


from team.models import Conference, Division, Team
from user.models import Profile, TeamProfile


class SelectTeamView(views.APIView):
    queryset = Team.objects.all()

    def post(self, request):
        team_id = request.data.get("teamID")
        try:
            team = self.queryset.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if Profile.objects.filter(has_team=True).exists():
            return Response(
                {"message": "Profile already has a team"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        profile = request.user
        profile.has_team = True
        profile.save()

        TeamProfile.objects.create(team=team, profile=profile)
        return Response(
            {"message": "The team was selected"}, status=status.HTTP_201_CREATED
        )


class ConferecyByIDView(generic.DetailView):
    template_name = "conference_teams.html"

    def get(self, request, id):
        divisions = Division.objects.filter(conference_id=id)
        return render(request, self.template_name, {"divisions": divisions})


class ConferencesView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/login/"
    template_name: str = "conferences.html"

    def get(self, request):
        confereces = Conference.objects.all()
        return render(request, self.template_name, {"conferences": confereces})


class TeamsByConferenceView(LoginRequiredMixin, generic.View):
    login_url = "/login/"
    template_name: str = "teams.html"

    def get(self, request, conference_id):
        teams = Team.objects.filter(division__conference_id=conference_id)
        return render(request, self.template_name, {"teams": teams})
