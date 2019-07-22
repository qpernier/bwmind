from django.shortcuts import render
from .models import IA,Game, Pawn, PawnsType
from .board.board import Board
from django.http import HttpResponse
from django.db import connection
from django.core import serializers
import json


"""
Get All ias
"""
def ias(request):
    return HttpResponse(serializers.serialize("json", IA.objects.all()))

"""
Create a new game
"""
def new_game(request):
    ia = IA.objects.get(code=request.GET.get('iaCode', ''))
    game = Game(fk_ia2=ia)
    game.save()

    board = Board()
    for pawn in board.initialPosition():
        pawns_type = PawnsType.objects.get(code=pawn["pawns_type"])
        pawn = Pawn(fk_game=game ,
                     fk_pawns_type=pawns_type,
                     owner=pawn["owner"],
                     vertical_coord=pawn["vertical_coord"],
                     horizontal_coord=pawn["horizontal_coord"])
        pawn.save()

    res = []

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM app_pawn as p JOIN app_pawnstype as pt ON pt.id = p.fk_pawns_type_id WHERE p.fk_game_id = %s ", [game.id])
        res = dictfetchall(cursor)

    return HttpResponse(json.dumps( res ))

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

