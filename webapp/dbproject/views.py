from django.shortcuts import render,redirect
from .models import Table
from .forms import TableForm
from django.http import HttpResponse

def index(request):
    error=''
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Uncorrect message'

    form = TableForm()
    data = {
        'form': form
    }
    list1 = Table.objects.all()
    return render(request,'dbproject/index.html',{'list1':list1,'form':form,'error':error})

def new(request):
    return render(request,'dbproject/new.html')

def removeTable(request,pk):
    form = Table()
    record = Table.objects.get(id=pk)
    record.delete()
    return redirect(index)


def getlist():
    list1 = Table.objects.all()
    list = ''
    for i in list1:
        list += f"{i.id} : {i.name}\n"
    return list