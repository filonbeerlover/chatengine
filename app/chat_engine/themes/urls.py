from django.urls import path, include
from . views import ThemesList, ThemeCreate, ThemeDelete, ThemeUpdate

app_name = "themes"

urlpatterns = [    
    path('create/',ThemeCreate.as_view(),name = 'create_theme'),
    path('delete/<pk>/',ThemeDelete.as_view(),name='delete_theme'),
    path('update/<pk>/',ThemeUpdate.as_view(),name='update_theme')
    path('',ThemesList.as_view(),name='themes_list'),
]