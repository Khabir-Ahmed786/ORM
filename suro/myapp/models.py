
from django.db import models
from django.contrib import admin
class football_Player (models.Model):
    name=models.CharField(max_length=100)
    height = models.IntegerField()
    age=models.IntegerField()
    weight=models.IntegerField()
    experience = models.IntegerField()

class Playeradmin(admin.ModelAdmin):
    list_display=('name','height','age','weight','experience')
