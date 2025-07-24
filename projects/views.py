#?  Import necessary modules
from django.shortcuts import render
from . import models

#? Class to handle the Projects page view
def projects_list_view(request):
    projects_list = models.Project.objects.all()
    context = {
        'projects': projects_list
    }
    return render(request, 'projects/project_list.html', context)           #* Projects the template to render
