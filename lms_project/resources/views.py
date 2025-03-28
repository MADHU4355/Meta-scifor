from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Folder, Resource
from .serializers import FolderSerializer, ResourceSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
#from django.views.decorators.csrf import csrf_exempt


@permission_classes([AllowAny])
class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)
    
#@csrf_exempt
@permission_classes([AllowAny])
class FolderListView(APIView):
    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class FolderDetailView(APIView):
    def get(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([AllowAny])
class ResourceListView(APIView):
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class ResourceDetailView(APIView):
    def get(self, request, pk):
        resource = get_object_or_404(Resource, pk=pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    def put(self, request, pk):
        resource = get_object_or_404(Resource, pk=pk)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        resource = get_object_or_404(Resource, pk=pk)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
