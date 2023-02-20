from http.client import HTTPResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


from team.models import Conferency
from user.models import Profile


class HomeView(generic.TemplateView):
    template_name: str = 'initial.html'


class LoginView(generic.View):
    template_name: str = 'login.html'

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email and not password:
            return render(request, self.template_name, {'errors': 'Email and password are blank'})

        if Profile.objects.filter(email=email).exists():
            profile = Profile.objects.get(email=email)
            if profile.check_password(password):
                login(request, profile)
                if profile.has_team:
                    return HttpResponseRedirect(reverse("account"))
                return HttpResponseRedirect(reverse("conferences"))



    def get(self, request) -> HTTPResponse:
        return render(request, self.template_name, {})


class AccountView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name: str = 'account.html'


class ConferencesView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name: str = 'conferences.html'

    def get(self, request) -> HTTPResponse:
        confereces = Conferency.objects.all()
        return render(request, self.template_name, {'conferences': confereces})
