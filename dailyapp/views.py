from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  
#messages notifications imported to user letting them know they are logged out or in.
from django.contrib import messages 
from .forms import SignUpForm


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def user_login(request):
    #check to see if logging in is enabled
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authentication method
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('login')
        else:
            messages.success(request, "Failed attempted! Please try again later, thank-you!")
            return redirect('login')
    else:
        return render(request, 'user_login.html', {})
    
def user_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #have the user sign-in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are now successfully logged into the system!")
            return redirect('register')
        form = SignUpForm()
        return render(request, 'user_register.html', { 'form': form })
    
def home(request):
    return render(request, 'home.html', {})

def newaccount(request):
    return render(request, "newaccount.html", {})

def useraccount(request):
    return render(request, "useraccount.html", {})



twitter = [
        {'id': 1, 'post': 'Learning Django!'},
        {'id': 2, 'post': 'Learning JavaScript!'},
        {'id': 3, 'post': 'learning PHP!'},
        {'id': 4, 'post': 'learning Python!'},
        {'id': 5, 'post': 'learning React!'},
        {'id': 6, 'post': 'learning Laravel!'},
        {'id': 7, 'post': 'learning node.js!'},
        {'id': 8, 'post': 'learning Express.js!'},
        {'id': 9, 'post': 'learning BootStrap!'},
        {'id': 10, 'post': 'learning Tailwind.js!'},
        {'id': 11, 'post': 'learning MySQL!'},
        {'id': 12, 'post': 'learning SQLite3!'},
        {'id': 13, 'post': 'learning Github!'},
        {'id': 15, 'post': 'learning HTML5!'},
        {'id': 16, 'post': 'learning CSS3!'},
        {'id': 17, 'post': 'Learning Full-Stack Development!'},
        {'id': 18, 'post': 'learning Front-End Development!'},
        {'id': 19, 'post': 'learning Back-End Development!'},
        {'id': 20, 'post': 'Learning Mobile Development!'},
        {'id': 21, 'post': 'Learning DevOps!'},
        {'id': 22, 'post': 'learning Data Engineering!'},
        {'id': 23, 'post': 'learning Machine Learning!'},
        {'id': 24, 'post': 'learning Platform Development!'},
        {'id': 25, 'post': 'learning Embedded Systems!'},
    ]

def posting(request):
    context = {'twitter': twitter}
    return render(request, "posting.html", context)
