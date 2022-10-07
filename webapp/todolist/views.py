from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponse

def registration(request):
    error = 'dddd'
    error=''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = 'Invalid values'
    else:
        form = UserForm()
        return render(request,'todolist/registration.html',{'form':form,'error':error,'tittle':'Registration'})

def index(request):
    print('123')
    error = 'dddd'
    form = UserForm()
    userAc = request.session.get('kvscv_user', 'None')

    if(userAc=='None'):
        return render(request,'todolist/login.html', {'form': form, 'tittle': 'Log In','err':error})
    else:
        return render(request,'todolist/index.html', {'asd':userAc})

def login(request):
    error = 'dddd1'
    """
    try:
        del request.session['kvscv_user']
    except(KeyError):
        pass
        """
    if request.method == 'POST':

        form = UserForm(request.POST)
        if form.is_valid():
            Login = request.POST['login']
            Password = request.POST['password']
            form = UserForm(request.POST)
            searchinguser = authenticate(request, Login = Login, Password = Password)
            if searchinguser is not None:
                login(request,searchinguser)
                request.session['kvscv_user'] = str(form.cleaned_data['login'])
                return render(request,'todolist/index.html', {'asd':request.session['kvscv_user']})
            else:
                form = UserForm()
                error='restarrt'
                return render(request, 'todolist/login.html', {'form': form, 'tittle': 'Log In','err':error})
    else:
        if request.session.get('kvscv_user', 'none') == 'none':
            form = UserForm()
            return render(request, 'todolist/login.html', {'form': form, 'tittle': 'Log In'})
        else:
            return redirect('index', {'asd':request.session['kvscv_user']})

    return HttpResponse("return this string")
def unlogin(request):
    try:
        del request.session['kvscv_user']
    except(KeyError):
        pass
    form = UserForm()
    data = {
        'form': form
    }
    return render(request, 'todolist/login.html', {'form': form, 'tittle': 'Log In'})



