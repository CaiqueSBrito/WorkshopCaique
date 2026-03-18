from django.contrib.auth.models import Group, User
from rest_framework import serializers

from meuapp.models import Pokemon

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["pokemon_id", "name", "types", "sprite_url", "hp", "attack", "defense", "speed", "captured_at"]
        
    def validateHP(hp):
        if hp <= 0:
            raise ValidationError("HP abaixo de 0")
        return hp