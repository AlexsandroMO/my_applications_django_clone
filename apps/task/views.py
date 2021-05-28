from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from apps.funcionarios.models import 


#@login_required
def home(request):
    oficial_name = 'Development Environment'
    return render(request,'task/index.html', {'oficial_name':oficial_name})