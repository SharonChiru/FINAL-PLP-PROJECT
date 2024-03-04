from django.contrib import admin

# Register your models here.
from .models import Category,Vendor
admin.site.register([Category,Vendor])