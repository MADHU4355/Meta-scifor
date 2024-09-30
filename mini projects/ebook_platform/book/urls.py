from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('upload/ebook/', upload_ebook, name='upload_ebook'),
    path('upload/poster/', upload_poster, name='upload_poster'),
    path('uploaded/', uploaded_list, name='uploaded_list'),
    path('ebook/<int:id>/', ebook_detail, name='ebook_detail'),
    path('poster/<int:id>/', poster_detail, name='poster_detail'),
    path('download/<int:id>/', download, name='download'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('reset-password/', reset_password, name='reset_password'),
    path('forget-password/', forget_password, name='forget_password'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('index/', index, name='index'),
    path('nectar-of-devotion', nectar_of_devotion, name='nectar_of_devotion'),
    path('upload/business-card/', upload_business_card, name='upload_business_card'),
    #path('create-ebook/', create_ebook_and_poster, name='create_ebook'),
]


























"""from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('upload-ebook/', upload_ebook, name='upload_ebook'),
    path('upload-poster/', upload_poster, name='upload_poster'),
    path('download/', download, name='download'),
    path('change-password/', change_password, name='change_password'),
    path('reset-password/', reset_password, name='reset_password'),
    path('forget-password/', forget_password, name='forget_password'),
    path('about/', about, name='about'),
    path('create-account/', create_account, name='create_account'),
]
"""