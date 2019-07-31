from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.board.coord import Coord
from .models import IA, Game, Pawn, PawnsType
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
    return HttpResponse(json.dumps(board.get_pawns_and_allowed_moves(game)))

"""
Move pawn from player 1 then play for player 2
"""
@csrf_exempt
def play(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf-8'))
        moved_pawn = Pawn.objects.get(id=params["pawn_id"])
        game = Game.objects.get(id=params["game_id"])
        destination = Coord(params["vertical_coord"], params["horizontal_coord"])
        #check move allowed
        board = Board()
        board.buildBoard(game)
        if board.is_move_allowed(moved_pawn, destination):
            game.strokes_number = game.strokes_number + 1
            game.save()
            #kill pawn if needed
            to_kill = Pawn.objects.filter(vertical_coord=destination.vertical_coord, horizontal_coord=destination.horizontal_coord)
            for killed_pawn in to_kill:
                killed_pawn.deadly_stroke = game.strokes_number
                killed_pawn.save()
            #move pawn
            moved_pawn.vertical_coord = destination.vertical_coord
            moved_pawn.horizontal_coord = destination.horizontal_coord
            moved_pawn.save()
            #move player 2 pawn with ia
            #TODO

        return HttpResponse(json.dumps(board.get_pawns_and_allowed_moves(game)))
    elif request.method == 'OPTIONS':
        return HttpResponse("ok")

