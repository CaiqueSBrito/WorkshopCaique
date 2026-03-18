from django.db import models
import requests

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
