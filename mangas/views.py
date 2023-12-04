from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from mangas.models import Manga
from mangas.serializers import MangaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def manga_list(request):
    # GET list of Mangas, POST a new Manga, DELETE all Mangas
    if request.method == 'GET':
        mangas = Manga.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            mangas = mangas.filter(name__icontains=name)

        autor = request.GET.get('autor', None)
        if autor is not None:
            mangas = mangas.filter(autor__icontains=autor)
        
        mangas_serializer = MangaSerializer(mangas, many=True)
        return JsonResponse(mangas_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        manga_data = JSONParser().parse(request)
        mangas_serializer = MangaSerializer(data=manga_data)
        if mangas_serializer.is_valid():
            mangas_serializer.save()
            return JsonResponse(mangas_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(mangas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Manga.objects.all().delete()
        return Response({'message': '{} Mangas were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def manga_detail(request, pk):
    # find Manga by pk (id)
    try: 
        manga = Manga.objects.get(pk=pk) 
    except Manga.DoesNotExist: 
        return JsonResponse({'message': 'The Manga does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
 
    # GET / PUT / DELETE Manga
    if request.method == 'GET': 
        manga_serializer = MangaSerializer(manga) 
        return JsonResponse(manga_serializer.data)
    elif request.method == 'PUT': 
        manga_data = JSONParser().parse(request) 
        manga_serializer = MangaSerializer(manga, data=manga_data) 
        if manga_serializer.is_valid(): 
            manga_serializer.save() 
            return JsonResponse(manga_serializer.data) 
        return JsonResponse(manga_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        manga.delete() 
        return Response({'message': 'Manga was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
        
@api_view(['GET'])
def manga_list_published(request):
    mangas = Manga.objects.filter(published=True)
        
    if request.method == 'GET': 
        mangas_serializer = MangaSerializer(mangas, many=True)
        return JsonResponse(mangas_serializer.data, safe=False)
    
