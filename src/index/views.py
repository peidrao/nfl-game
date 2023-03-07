from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views import generic
from django.urls import reverse

from user.models import Profile


class HomeView(generic.TemplateView):
    template_name: str = "initial.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("account")
        return redirect("")


class LoginView(generic.View):
    template_name: str = "login.html"

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email and not password:
            return render(
                request, self.template_name, {"errors": "Email and password are blank"}
            )

        if Profile.objects.filter(email=email).exists():
            profile = Profile.objects.get(email=email)
            if profile.check_password(password):
                login(request, profile)
                if profile.has_team:
                    return HttpResponseRedirect(reverse("account"))
                return HttpResponseRedirect(reverse("conferences"))

    def get(self, request):
        return render(request, self.template_name, {})


class LogoutView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = "index"

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)
