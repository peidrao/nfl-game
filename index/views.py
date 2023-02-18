from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name: str = 'initial.html'


class LoginView(generic.TemplateView):
    template_name: str = 'login.html'
