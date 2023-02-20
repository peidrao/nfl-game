
from django.urls import path

from index.views import HomeView, LoginView, AccountView, ConferencesView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('account/', AccountView.as_view(), name='account'),
    path('conferences/', ConferencesView.as_view(), name='conferences'),
]
