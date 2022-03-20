from django.shortcuts import render, redirect

# Create your views here.

def index(request):

    return render(request, 'hood/index.html')

def login_user():

    return render(request, 'auth/login.html', context)

def logout_user():
    
    return redirect('index')
