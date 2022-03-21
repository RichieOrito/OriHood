from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from .forms import CreateUserForm, NewPostForm, NewBusinessForm, EditProfileForm, ChangeHoodForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'hood/index.html')

@login_required(login_url='login')
def feed(request):
    current_user = request.user.profile
    posts = models.post.objects.filter(hood=current_user.hood)

    if request.method == 'POST':
        new_post_form = NewPostForm(request.POST)
        if new_post_form.is_valid():
            new_post_form.instance.user = current_user
            new_post_form.instance.hood =current_user.hood
            new_post_form.save()

            return redirect('feed')
    else:
        new_post_form = NewPostForm()

    title = 'Feed'
    context = {
        'title': title,
        'posts': posts,
        'new_post_form': new_post_form,
    }

    return render(request, 'hood/feed.html',context)

@login_required(login_url='login')
def businesses(request):
    current_user = request.user.profile

    if request.method == 'POST':
        new_business_form = NewBusinessForm(request.POST)
        if new_business_form.is_valid():
            new_business_form.instance.user = current_user
            new_business_form.instance.hood = current_user.hood
            new_business_form.save()

            return redirect('businesses')
    else:
        new_business_form = NewBusinessForm()

    businesses = models.Business.objects.filter(neighborhood=current_user.hood)

    title = 'Businesses'
    context = {
        'title': title,
        'businesses':businesses,
        'new_business_form':new_business_form,
    }

    return render(request, 'hood/businesses.html', context)

