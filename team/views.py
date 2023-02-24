from django.views import generic

from rest_framework import generics, views, status
from rest_framework.response import Response

from team.models import Conferency, Team
from user.models import Profile, TeamProfile


class SelectTeamView(views.APIView):
    queryset = Team.objects.all()

    def post(self, request):
        team_id = request.data.get('teamID')
        try:
            team = self.queryset.get(id=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)

        if Profile.objects.filter(has_team=True).exists():
            return Response({'message': 'Profile already has a team'}, status=status.HTTP_400_BAD_REQUEST)

        profile = request.user
        profile.has_team =  True
        profile.save()

        TeamProfile.objects.create(team=team, profile=profile)
        return Response({'message': 'The team was selected'}, status=status.HTTP_201_CREATED)
