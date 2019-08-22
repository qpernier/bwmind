from django.db import models
from django.contrib.auth.models import User
from django.db import connection
import pprint


class IA(models.Model):
    name = models.CharField(max_length=200,unique = True)
    code = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

class Stat(models.Model):
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

class Pawn(models.Model):
    OWNER_CHOICES = [("player1", "player1"), ("player2", "player2")]
    fk_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    fk_pawns_type = models.ForeignKey(PawnsType, on_delete=models.CASCADE)
    owner = models.CharField(max_length=10, choices=OWNER_CHOICES,)
    vertical_coord = models.IntegerField()
    horizontal_coord = models.IntegerField()
    deadly_stroke = models.IntegerField(blank=True, null=True)

    def get_pawns(self, game):

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT p.id, owner, vertical_coord, horizontal_coord, deadly_stroke, fk_game_id, fk_pawns_type_id, name,code FROM app_pawn as p JOIN app_pawnstype as pt ON pt.id = p.fk_pawns_type_id WHERE p.fk_game_id = %s and p.deadly_stroke IS NULL",
                [game.id])
            return self.dictfetchall(cursor)


    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    """
    Move a pawn and if needed kill the destination pawn
    """
    @staticmethod
    def move_pawn_and_kill_if_needed(move, strokes_number):
        # kill pawn if needed
        to_kill = Pawn.objects.filter(vertical_coord=move.coord.vertical_coord,
                                      horizontal_coord=move.coord.horizontal_coord)
        for killed_pawn in to_kill:
            killed_pawn.deadly_stroke = strokes_number
            killed_pawn.save()
        # move pawn
        moved_pawn = Pawn.objects.get(id=move.pawn_id)
        moved_pawn.vertical_coord = move.coord.vertical_coord
        moved_pawn.horizontal_coord = move.coord.horizontal_coord
        moved_pawn.save()


