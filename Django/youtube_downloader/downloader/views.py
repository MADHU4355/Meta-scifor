from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import User
from django.contrib import messages
from .models import FavoriteVideo
from django.http import HttpResponse
import yt_dlp
from pytube import YouTube
import os
from django.http import JsonResponse
from django.views import View
from yt_dlp import YoutubeDL


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'signup.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': "Username already taken."})

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

"""def download_video(request):
    if request.method == 'POST':
        #link = request.POST['link']
        url = request.POST.get('url')
        print(f"Received URL: {url}")


        ydl_opts ={
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'D:\ytdownloader\%(title)s.%(ext)s',
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download = True)
            return HttpResponse(f"successfully downloaded: {info_dict['title']}")
    return render(request,'download_video.html')"""

def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print(f"Received URL: {url}")

        # Validate the URL
        if not url:
            return JsonResponse({'error': 'No URL provided'}, status=400)
        if not isinstance(url, str) or not url.startswith('http'):
            return JsonResponse({'error': 'Invalid URL'}, status=400)

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': r'D:\ytdownloader\%(title)s.%(ext)s',  # Use raw string to avoid escape issues
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                return HttpResponse(f"Successfully downloaded: {info_dict['title']}")
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'download_video.html')


"""def download_success(request):
    video = "Sample Video"  # Replace with actual video title if available
    return render(request, 'download_success.html', {'video': video})
"""

def download_success(request):
    # Assuming you store the video path in session or some form of storage
    video_path = "path/to/downloads/your_video.mp4"
    return render(request, 'download_success.html', {'video_path': video_path})


def download_error(request):
    error = "An error occurred."  # Replace with actual error message
    return render(request, 'download_error.html', {'error': error})

def fav_video(request):
    if request.user.is_authenticated:
        favorites = FavoriteVideo.objects.filter(user=request.user)
        return render(request, 'fav_video.html', {'favorites': favorites})
    else:
        return redirect('login')

def remove_favorite(request, video_id):
    if request.user.is_authenticated:
        FavoriteVideo.objects.filter(id=video_id, user=request.user).delete()
    return redirect('fav_video')















"""from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, VideoURLForm
from pytube import YouTube

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('download_video')
    else:
        form = SignUpForm()
    return render(request, 'downloader/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('download_video')
    else:
        form = LoginForm()
    return render(request, 'downloader/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def download_video(request):
    if request.method == 'POST':
        form = VideoURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                stream.download()  # Downloads to the current directory
                return render(request, 'downloader/download_success.html', {'video': yt.title})
            except Exception as e:
                return render(request, 'downloader/download_error.html', {'error': str(e)})
    else:
        form = VideoURLForm()
    return render(request, 'downloader/download_video.html', {'form': form})
"""