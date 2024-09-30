from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('download_video/', views.download_video, name='download_video'),
    path('download_success/', views.download_success, name='download_success'),
    path('download_error/', views.download_error, name='download_error'),
    path('fav_video/', views.fav_video, name='fav_video'),
    path('remove_favorite/<int:video_id>/', views.remove_favorite, name='remove_favorite'),
]
