from django.shortcuts import render
from .models import IA,Game, Pawn, PawnsType
from .board.board import Board
from django.http import HttpResponse
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

    pawn_class = Pawn()

    pawn_queryset = pawn_class.get_pawns(game)

    board.buildBoard(game)
    for pawn_dict in pawn_queryset:
        pawn_dict["allowed_move"] = board.allowed_move(pawn_dict["code"], pawn_dict["owner"], pawn_dict["vertical_coord"], pawn_dict["horizontal_coord"])
    return HttpResponse(json.dumps(pawn_queryset))

