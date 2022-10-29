import pickle
from django.shortcuts import redirect, render
from django.shortcuts import render
from .models import WordLan,Words
#from ..lang.models import Word
from.config import current_lang as current_lang





class Table:
    id = 0
    name = ''
    def __init__(self,id,name):
        self.id = id
        self.name = name

# Create your views here.
def index(request):


    if request.session.get('langkvs', 'None') == 'None':
        request.session['langkvs'] = 'eng'
    lang = request.session.get('langkvs', 'None')
    words1 = WordLan.objects.values_list('eng')
    words = Words()

    if lang == 'eng':
        words1 = WordLan.objects.values_list('eng')
    else:
        words1 = WordLan.objects.values_list('ua')

    words.contact = str(words1[0])
    words.contact = words.contact[2:-3]
    words.Experience = str(words1[1])
    words.Experience = words.Experience[2:-3]
    words.exp1=str(words1[2])
    words.exp1 = words.exp1[2:-3]
    words.aboutme = str(words1[3])
    words.aboutme = words.aboutme[2:-3]
    words.ab1 = str(words1[4])
    words.ab1 = words.ab1[2:-3]
    words.Education  = str(words1[5])
    words.Education = words.Education[2:-3]
    words.edt = str(words1[6])
    words.edt = words.edt[2:-3]
    words.ed1 = str(words1[7])
    words.ed1 = words.ed1[2:-3]
    words.ed2 = str(words1[8])
    words.ed2 = words.ed2[2:-3]
    words.Skills = str(words1[9])
    words.Skills = words.Skills[2:-3]
    words.sk1 = str(words1[10])
    words.sk1 = words.sk1[2:-3]
    words.sk2 = str(words1[11])
    words.sk2 = words.sk2[2:-3]
    words.sk3 = str(words1[12])
    words.sk3 = words.sk3[2:-3]
    words.sk4 = str(words1[13])
    words.sk4 = words.sk4[2:-3]
    words.Stack = str(words1[14])
    words.Stack = words.Stack[2:-3]
    words.age = str(words1[15])
    words.age = words.age[2:-3]
    words.lang = str(words1[16])
    words.lang = words.lang[2:-3]
    return render(request,'main/index.html',{'title':'CV', 'words':words})

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

def switcher(request):
    if request.session.get('langkvs', 'None') == 'eng':
        request.session['langkvs'] = 'ua'
    else:
        request.session['langkvs'] = 'eng'
    return redirect('/')
