from django.urls import path, include
from . views import themes_list

urlpatterns = [
    path('',themes_list),
]