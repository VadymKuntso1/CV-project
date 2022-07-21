from django.shortcuts import render
from .models import Table

def index(request):
    list1 = Table.objects.all()
    return render(request,'dbproject/index.html',{'list1':list1})

def new(request):
    return render(request,'dbproject/new.html')


