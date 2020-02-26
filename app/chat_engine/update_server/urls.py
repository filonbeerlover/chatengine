from django.urls import path
from . views import UpdateServer

urlpatterns = [    
    path('',UpdateServer.as_view())
]
