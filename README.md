# Ex02 Django ORM Web Application
## Date: 13/9/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```

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



from django.contrib import admin
from .models import football_Player,Playeradmin
admin.site.register(football_Player,Playeradmin)
```

## OUTPUT
![Alt text](suro/123.jpg)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
