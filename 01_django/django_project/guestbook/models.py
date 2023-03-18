from django.db import models

# Create your models here.

class GuestBookModel(models.Model) :
    writer = models.CharField(max_length=100)
    content = models.TextField()
    
    