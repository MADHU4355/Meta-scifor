from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('folders/', views.FolderListView.as_view(), name='folder_list'),
    path('folders/<int:pk>/', views.FolderDetailView.as_view(), name='folder_detail'),
    path('resources/', views.ResourceListView.as_view(), name='resource_list'),
    path('resources/<int:pk>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]













"""from django.urls import path
from . import views

urlpatterns = [

    path('folders/', views.FolderListView.as_view(), name='folder_list'),
    path('folders/create/', views.FolderCreateView.as_view(), name='folder_create'),
    path('folders/<int:pk>/', views.FolderDetailView.as_view(), name='folder_detail'),
    path('folders/<int:pk>/edit/', views.FolderUpdateView.as_view(), name='folder_edit'),
    path('folders/<int:pk>/delete/', views.FolderDeleteView.as_view(), name='folder_delete'),
    path('resources/', views.ResourceListView.as_view(), name='resource_list'),
    path('resources/create/', views.ResourceCreateView.as_view(), name='resource_create'),
    path('resources/<int:pk>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('resources/<int:pk>/edit/', views.ResourceUpdateView.as_view(), name='resource_edit'),
    path('resources/<int:pk>/delete/', views.ResourceDeleteView.as_view(), name='resource_delete'),
]
"""