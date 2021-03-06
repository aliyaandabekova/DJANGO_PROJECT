from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Service,Master
from .forms import RegisterForm
from .services import profileCreate,checkExpiredCertificate

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def services(request):
    services = Service.objects.all()
    return render(request,'service.html',{'services':services})

def masters(request):
    masters = Master.objects.all()
    return render(request, 'master.html',{'masters':masters})

def register_page(request):
    form = RegisterForm()
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            profileCreate(form.cleaned_data,form.instance)
    return render(request,'register.html',{'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')

def master_detail(request,master_id):
    try:
        master = Master.objects.get(id=master_id)
        services = master.services.all()
        certificates = master.certificates_set.filter(status='active')
        checkExpiredCertificate(certificates)

    except Master.DoesNotExist:
        return HttpResponse('404')
    return render(request,'master_detail.html',{'master':master,
                                                'services':services,
                                                'certificates':certificates,})