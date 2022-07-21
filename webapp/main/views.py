from django.shortcuts import render
class Table:
    id = 0
    name = ''
    def __init__(self,id,name):
        self.id = id
        self.name = name
# Create your views here.
def index(request):
    return render(request,'main/index.html',{'title':'CV'})

def about(request):
    return render(request,'main/about.html')
def message(request):
    return render(request, 'main/message.html')

def table(request):
    list1 = []
    list1.append(Table(1,'first'))
    list1.append(Table(2, 'seccond'))
    list1.append(Table(3, 'third'))
    list1.append(Table(4, 'forth'))
    list1.append(Table(5, 'fifth'))

    table={
        'tables':list1
    }
    return render(request,'main/table.html',table)