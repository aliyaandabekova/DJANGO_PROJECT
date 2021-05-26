from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile,Order
from .forms import OrderForm

def profile_page(request):
    print(request.user)
    try:
        profile = Profile.objects.get(user=request.user)
    except (Profile.DoesNotExist,TypeError):
        return HttpResponse('404')
    return render(request,'profile.html',{'profile':profile})

def order_page(request):
    user = request.user
    form = OrderForm(initial={'user':user})
    if request.method == "POST":
        form =OrderForm(request.POST, initial={'user':user})
        if form.is_valid():
            form.save()
    return render(request, 'order.html', {'form':form})