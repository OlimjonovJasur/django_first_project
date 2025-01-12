from django.urls import path

from olcha.views import home

urlpatterns = [
    path('home/', home, name='home'),
]
