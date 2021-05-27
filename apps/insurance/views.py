
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Cliente
from .forms import ClienteForm


#import FormatTexts as ft
import datetime
from datetime import date
#import atualyze_database as atual_db

#_lte - menor ou igual à
#_gte maior ou igual
#qstart 
#qend

# today = datetime.datetime.now()
# implement = str(today)[:10]
# cont_implement = implement.replace('-','')

def home_insurance(request):

    return render(request,'insurance/index-insurance.html')


# def index(request):
#     #print('ok!!!!!!!!!!!')
#     GET = str(dict(request.GET))
#     #x = dict(request.GET)
#     #print('>>>>>>>>>>>>>>>>>>>>', GET[2:9], sorted(x, key=x.get))
#     data_atual = date.today()
#     start_date = data_atual + datetime.timedelta(days=-395)
#     limit_date = data_atual + datetime.timedelta(days=-335)

#     if GET[2:9] == 'option1':
#         start_date = data_atual + datetime.timedelta(days=-370)
#     elif GET[2:9] == 'option2':
#         start_date = data_atual + datetime.timedelta(days=-375)
#     elif GET[2:9] == 'option3':
#         start_date = data_atual + datetime.timedelta(days=-380)
#     elif GET[2:9] == 'option4':
#         start_date = data_atual + datetime.timedelta(days=-395)

#     end_date = limit_date
#     Clientes = Cliente.objects.filter(date_contract__range=(start_date, end_date))
    
#     Cliente_filter = []

#     for i in Clientes:
#         date_calc = i.date_contract - data_atual
#         if date_calc < datetime.timedelta(-365):
#             #print('ok')
#             Cliente_filter.append([i.name, i.policy, i.amount_paid, i.date_contract])

#     length = len(Cliente_filter)

#     status = False

#     return render(request,'insurance/index.html', {'Clientes': Clientes, 'length':length, 'Cliente_filter':Cliente_filter, 'status':status})


@login_required
def ListaCliente(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        Clientes = Cliente.objects.filter(name__icontains=search)
        #Clientes = Cliente.objects.filter(name__icontains=search, user=request.user)
    elif filter:
        Clientes = Cliente.objects.filter(name=filter)
        #Clientes = Cliente.objects.filter(name=filter, user=request.user)
    else:
        tasks_list = Cliente.objects.all().order_by('name')
        #tasks_list = Cliente.filter.objects.all().order_by('name').filter(user=request.user)

        paginator = Paginator(tasks_list, 10)

        page = request.GET.get('page')
        Clientes = paginator.get_page(page)

    #Clientes = Cliente.objects.all().order_by('name')
    length = len(Clientes)
    
    #--------------------------------------------------------------------
    num = 0
    for a in Clientes:

        if a.cpf != '':
            a.cpf = '{}.{}.{}-{}'.format(a.cpf[:3], a.cpf[3:6:], a.cpf[6:9:], a.cpf[9:])

        if a.cnpj != '':
            a.cnpj = '{}.{}.{}/{}-{}'.format(a.cnpj[:2], a.cnpj[2:5:], a.cnpj[5:8:], a.cnpj[8:12], a.cnpj[12:])

        a.amount_paid = ft.format_cpf_cnpj(str(a.amount_paid), num)

        if a.cel1 != '':
            a.cel1 = ft.cel_tel(a.cel1)
        else:
            a.cel1 = ''

        if a.cel2 != '':
            a.cel2 = ft.cel_tel(a.cel2)
        else:
            a.cel2 = ''

        if a.tel1 != '':
            a.tel1 = ft.cel_tel(a.tel1)
        else:
            a.tel1 = ''

        if a.tel2 != '':
            a.tel2 = ft.cel_tel(a.tel2)
        else:
            a.tel2 = ''

        num += 1
    #--------------------------------------------------------------------
    return render(request,'insurance/list-client.html', {'Clientes': Clientes, 'length':length})


@login_required
def VCliente(request):

    Clientes = Cliente.objects.all().order_by('name')

    length = len(Clientes)

    #--------------------------------------------------------------------
    for a in Clientes:

        if a.cpf != '':
            a.cpf = '{}.{}.{}-{}'.format(a.cpf[:3], a.cpf[3:6:], a.cpf[6:9:], a.cpf[9:])

        if a.cnpj != '':
            a.cnpj = '{}.{}.{}/{}-{}'.format(a.cnpj[:2], a.cnpj[2:5:], a.cnpj[5:8:], a.cnpj[8:12], a.cnpj[12:])

        a.amount_paid = ft.format_cpf_cnpj(str(a.amount_paid))

        if a.cel1 != '':
            a.cel1 = ft.cel_tel(a.cel1)
        else:
            a.cel1 = ''

        if a.cel2 != '':
            a.cel2 = ft.cel_tel(a.cel2)
        else:
            a.cel2 = ''

        if a.tel1 != '':
            a.tel1 = ft.cel_tel(a.tel1)
        else:
            a.tel1 = ''

        if a.tel2 != '':
            a.tel2 = ft.cel_tel(a.tel2)
        else:
            a.tel2 = ''
    #--------------------------------------------------------------------

    return render(request,'insurance/v-cliente.html', {'Clientes': Clientes, 'length':length})

@login_required
def EditSegur(request, id):

    data_atual = date.today()

    Clientes = Cliente.objects.all()
    length = len(Clientes)

    task = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=task)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=task)

        if(form.is_valid()):
            if task.policy == '0':
                task.policy = '{}000000000000{}'.format(data_atual, length)
            task.save()
            return redirect('/')
        else:
            return render(request,'insurance/edit-seguros.html', {'form': form, 'task': task})

    else:
        return render(request,'insurance/edit-seguros.html', {'form': form, 'task': task})


@login_required
def NewSegur(request):

    Clientes = Cliente.objects.all()
    length = len(Clientes)

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            if task.policy == '0':
                task.policy = '{}00000000000000000{}'.format(cont_implement, length)
            task.save()
            return redirect('/')
    else:
        form = ClienteForm()
        return render(request, 'insurance/new-segur.html', {'form': form})


def DeleteSegur(request, id):
    Clientes = get_object_or_404(Cliente, pk=id)
    Clientes.delete()

    messages.info(request, 'Atividade deletada com sucesso!')

    return redirect('/lista_cliente')

def DeleteConfirm(request, id):

    Clientes = Cliente.objects.filter(id=id)

    return render(request, 'insurance/delet-confirm.html',{ 'id':id, 'Clientes':Clientes})


def DB_Atualyze(request):

    atual_db.DbDb()
    status = True
    return render(request, 'insurance/index.html',{'status':status})















#from datetime import datetime
#from datetime import date #https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=CjwKCAjwmv-DBhAMEiwA7xYrd2WUEVO6sTelrXq66VW5WpOmYO4qk54RT1cSawBVflHBk_WbjclXEhoCC4wQAvD_BwE
#https://www.schoolofnet.com/forum/topico/filtro-de-busca-por-data-inicial-e-data-final-7565

#https://qastack.com.br/programming/629551/how-to-query-as-group-by-in-django