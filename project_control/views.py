from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from apps.funcionarios.models import 


@login_required
def home_project(request):
    return render(request,'project_control/index.html')