from django.urls import path
from jokesapp.views import index


urlpatterns = [
    path('', index)
]
