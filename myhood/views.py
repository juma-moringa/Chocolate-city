from myhood.models import Business, Neighbourhood, Post, Profile
from myhood.forms import NewBusinessForm, NewNeighbourHoodForm, PostForm, ProfileForm, SignUpForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    myhoods = Neighbourhood.objects.all()
    myhoods = myhoods[::-1]
    return render(request,'index.html',{'myhoods': myhoods})

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
            neighbourhood.admin = request.user
            neighbourhood.save()
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

@login_required(login_url='/accounts/login/')
def join_neighbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def leave_neighbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')


@login_required(login_url='/accounts/login/')
def create_post(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighbourhood = neighbourhood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

@login_required(login_url='/accounts/login/')
def create_business(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    if request.method == 'POST':
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.neighbourhood = neighbourhood
            biz.user = request.user.profile
            biz.save()
            return redirect('single-hood', id)
    else:
        form =NewBusinessForm()
    return render(request, 'business.html', {'form': form})

  

@login_required(login_url='/accounts/login/')
def single_neighbourhood(request,id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood_id=id)
    posts = Post.objects.filter(neighbourhood=neighbourhood)
    if request.method == 'POST':
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            bizform = form.save(commit=False)
            bizform.neighbourhood = neighbourhood
            bizform.user = request.user.profile
            bizform.save()
            return redirect('single-hood', id)
    else:
        form = NewBusinessForm()
    return render(request, 'hood_details.html', { 'posts': posts,'neighbourhood': neighbourhood,'form':form ,'business':business})


@login_required(login_url='/accounts/login/')
def search_business(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        found_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"found_businesses":found_businesses,"message":message})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
