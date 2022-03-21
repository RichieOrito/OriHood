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

@login_required(login_url='login')
def hood(request):

    current_user = request.user
    hood = current_user.profile.hood

    title = 'hood'
    context = {
        'title': title,
        'hood': hood,
    }

    return render(request, 'hood/neighborhood.html', context)

@login_required(login_url='login')
def profile(request):

    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        change_hood_form = ChangeHoodForm(request.POST, request.FILES, instance=request.user.profile)
        if edit_profile_form.is_valid():
            edit_profile_form.instance.user = request.user
            edit_profile_form.save()

            redirect('profile')
        elif change_hood_form.is_valid():
            change_hood_form.save()

            redirect('profile')

    else:
        edit_profile_form = EditProfileForm()
        change_hood_form = ChangeHoodForm()

    title = 'Profile'
    context = {
        'title': title,
        'edit_profile_form': edit_profile_form,
        'change_hood_form':change_hood_form,
    }

    return render(request, 'hood/profile.html', context)

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUserForm()
        title = 'New Account'

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form': form, 'title': title}
    return render(request, 'auth/register.html', context)

