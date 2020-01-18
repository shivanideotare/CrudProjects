from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    disp = ['sname', 'scity', 'sid']

admin.site.register(Student,StudentAdmin)
