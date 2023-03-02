from django.contrib import admin
from .models import Empleado,Novedades,Familia

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Familia)
admin.site.register(Novedades)