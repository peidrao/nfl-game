from http.client import HTTPResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from team.models import Team


class AccountView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/login/"
    template_name: str = "account/account.html"

    def get(self, request) -> HTTPResponse:
        context = {}
        try:
            team = request.user.teamprofile_set.all().first().team
            context["team"] = team
            context["teams"] = Team.objects.filter(division=team.division)
        except Exception as e:
            print(e)
        return render(request, self.template_name, context)
