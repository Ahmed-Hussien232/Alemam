from django.contrib import admin
from .models import Login, PrintOrder, Payments, Come_in
# Register your models here.

admin.site.register(Login)
admin.site.register(PrintOrder)
admin.site.register(Payments)
admin.site.register(Come_in)