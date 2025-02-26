from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app.forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def manageUser(request):
    users = Users.objects.all()
    context = {
        'users':users
    }
    return render(request, 'admin/manageUser.html', context)

def manageCompany(request):
    companies = Companies.objects.all().select_related('user')
    users_without_companies = Users.objects.filter(~Q(companies__isnull=False))
    
    form = CompanyForm()
    context = {
        'companies':companies,
        'users':users_without_companies,
        'form':form
    }
    return render(request, 'admin/manageCompany.html', context)

def dashboard(request):
    
    return render(request, 'dashboard.html')

def login_(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            msg = 'Incorrect data, please try again'
            return render(request, 'auth/login.html', {'msg':msg})
    else:
        return render(request, 'auth/login.html')
    

#Fetch
def createUser(request):
    form = UserForm(request.POST)
    if form.is_valid():
        client = form.save(commit=False)
        client.is_active = True
        client.save()
        return JsonResponse({'success': True, 'message': 'Usuario creado correctamente'})
    else:
        # Si el formulario no es válido, devolvemos los errores en formato JSON
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
@csrf_exempt
def toggleUserStatus(request, user_id):
    try:
        user = Users.objects.get(id=user_id)
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'errors':e}, status=400)

def createCompany(request):
    form = CompanyForm(request.POST)
    if form.is_valid():
        company = form.save(commit=False)
        company.balance = 10
        company.save()
        return JsonResponse({'success': True, 'message': 'Compañia creado correctamente'})
    else:
        # Si el formulario no es válido, devolvemos los errores en formato JSON
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)