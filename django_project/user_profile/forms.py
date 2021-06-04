from django.forms import ModelForm
from .models import Order, Profile

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['user','service','payment_method']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo', 'age', 'email']