from __future__ import unicode_literals
from django.db import models

# Create your models here.

class importData(models.Model):

   url_data = models.CharField(max_length = 100)
   url_target = models.CharField(max_length = 100)

   class Meta:
       verbose_name = "importData"
       verbose_name_plural = "importDatas"

class trainData(models.Model):

    feature0 = models.CharField(max_length= 50)
    feature1 = models.CharField(max_length= 50)
    feature2 = models.CharField(max_length= 50)
    feature3 = models.CharField(max_length= 50)
    feature4 = models.CharField(max_length= 50)
    feature5 = models.CharField(max_length= 50)
    feature6 = models.CharField(max_length= 50)
    feature7 = models.CharField(max_length= 50)
    feature8 = models.CharField(max_length= 50)
    feature9 = models.CharField(max_length= 50)

    class Meta:
        verbose_name = "trainData"
        verbose_name_plural = "trainDatas"
