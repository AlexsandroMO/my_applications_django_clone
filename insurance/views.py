from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from apps.funcionarios.models import 


@login_required
def home(request):
    return render(request,'insurance/index.html')