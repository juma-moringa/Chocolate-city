from myhood.models import Neighbourhood
from myhood.forms import NewNeighbourHoodForm, ProfileForm, SignUpForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form})  

@login_required(login_url='/accounts/login/')
def create_new_neighbourhood(request):
    if request.method == 'POST':
        form = NewNeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = request.user
            neighbourhood.save()
            messages.success(request, 
            '''
            You have succesfully created a Neighbourhood.
            You can now proceed and join the new Neighbourhood.
            ''')
            return redirect('index')
    else:
        form = NewNeighbourHoodForm()
    return render(request, 'mynewhood.html', {'form':form})   


@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        user_profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if  user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('home')
    else:
        user_profile_form = ProfileForm(instance=request.user)
    return render(request, 'profile.html',{"user_profile_form": user_profile_form})    