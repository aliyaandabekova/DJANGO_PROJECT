from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register([Service,Master,Certificates])
# admin.site.register(Master)