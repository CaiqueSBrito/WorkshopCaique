from django.db import models
import requests

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)

class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.TextField()
    types = models.JSONField()
    sprite_url = models.ImageField(upload_to='pokemon/')
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    captured_at = models.TextField()

    class Meta:
        ordering = ['pokemon_id']        