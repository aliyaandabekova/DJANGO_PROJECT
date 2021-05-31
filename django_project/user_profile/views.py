from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile,Order
from .forms import OrderForm
from .services import incrementOrdetCount, countMoney
from spa.models import Service

def profile_page(request):
    print(request.user)
    try:
        profile = Profile.objects.get(user=request.user)
    except (Profile.DoesNotExist,TypeError):
        return HttpResponse('404')
    return render(request,'profile.html',{'profile':profile})

def order_page(request, service_id):
    service = Service.objects.get(id=service_id)
    user = request.user
    form = OrderForm(initial={'user':user,'service':service})
    if request.method == "POST":
        form = OrderForm(request.POST, initial={'user':user,'service':service})
        if form.is_valid():
            incrementOrdetCount(user.profile)
            countMoney(user.profile, form.instance)
            form.save()
    return render(request, 'order.html', {'form':form})


def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'my_orders.html',{'orders':orders})


def delete_order(request,order_id):
    try:
        order = Order.objects.get(user=request.user,id=order_id)
    except Order.DoesNotExist:
        #TODO
        return HttpResponse('?')
    if request.method == 'POST':
        order.delete()
    return render(request,'delete_order.html')