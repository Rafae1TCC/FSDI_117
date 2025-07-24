#? Import necessary modules
from django.urls import path
from .views import (
    projects_list_view,
)

#? URL patterns for the Portfolio app
urlpatterns = [
    path('projects/', projects_list_view, name='project_list'),         #* Projects page URL pattern
]