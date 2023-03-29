from django.db import models
class about_fun(models.Model):
    
    title=models.CharField(max_length=50)
    contant=models.TextField()

# Create your models here.