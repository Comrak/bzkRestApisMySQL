from django.db import models

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=55, blank=False, default='')
    onEmision = models.BooleanField(default=False,blank=False)
    currentChapter = models.IntegerField(blank=False,default=0)
    lastChapter = models.IntegerField(blank=False,default=0)
    autor = models.CharField(max_length=200,blank=False, default='')

