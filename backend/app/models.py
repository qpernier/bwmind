from django.db import models
from django.contrib.auth.models import User

class IA(models.Model):
    name = models.CharField(max_length=200,unique = True)
    code = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

class Stats(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fk_ia = models.ForeignKey(IA, on_delete=models.CASCADE, blank=True, null=True)
    win = models.IntegerField(default=0)
    game = models.IntegerField(default=0)

class Game(models.Model):
    fk_user1 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user1')
    fk_ia1 = models.ForeignKey(IA, on_delete=models.CASCADE, blank=True, null=True, related_name='ia1')
    fk_user2 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user2')
    fk_ia2 = models.ForeignKey(IA, on_delete=models.CASCADE, blank=True, null=True, related_name='ia2')
    strokes_number = models.IntegerField(default=0)
    ended = models.BooleanField(default=False)

class PawnsType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

class Pawns(models.Model):
    OWNER_CHOICES = [("player1", "player1"), ("player2", "player2")]
    fk_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    fk_pawns_type = models.ForeignKey(PawnsType, on_delete=models.CASCADE)
    owner = models.CharField(max_length=10, choices=OWNER_CHOICES,)
    vertical_coord = models.IntegerField()
    horizontal_coord = models.IntegerField()
    deadly_stroke = models.IntegerField(blank=True, null=True)
