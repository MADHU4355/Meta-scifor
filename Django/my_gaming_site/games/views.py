from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm
from .models import Score

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def number_guessing(request):
    return render(request, 'number_guessing.html')

@login_required
def tic_tac_toe(request):
    return render(request, 'tic_tac_toe.html')

@login_required
def snake_game(request):
    return render(request, 'snake_game.html')

@login_required
def peak_game(request):
    return render(request, 'peak_game.html')

@login_required
def game_2048(request):
    return render(request, 'game_2048.html')
