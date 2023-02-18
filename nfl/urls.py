
from django.contrib import admin
from django.urls import path, include

from index.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
]
