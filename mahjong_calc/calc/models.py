from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20)
    played = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

class Result(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Game(models.Model):
    players = models.ManyToManyField(Result, related_name='games', blank=True)
