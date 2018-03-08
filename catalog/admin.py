from django.contrib import admin

# Register your models here.
from .models import Kafedra,Student, Prepod

admin.site.register(Kafedra)
admin.site.register(Student)
admin.site.register(Prepod)
