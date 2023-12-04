from rest_framework import serializers 
from mangas.models import Manga
 
 
class MangaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Manga
        fields = ('id',
                  'name',
                  'onEmision',
                  'currentChapter',
                  'lastChapter',
                  'autor')
        