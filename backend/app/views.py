from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.board.coord import Coord

from app.board.move import Move

from app.IA import IA
from .models import Game, Pawn, PawnsType, IA as IA_model
from .board.board import Board
from django.http import HttpResponse
from django.core import serializers
import json


"""
Get All ias
"""
def ias(request):
    return HttpResponse(serializers.serialize("json", IA_model.objects.all()))

"""
Create a new game
"""
def new_game(request):
    ia = IA_model.objects.get(code=request.GET.get('iaCode', ''))
    game = Game(fk_ia2=ia)
    game.save()
    board = Board()
    for pawn in board.initial_position():
        pawns_type = PawnsType.objects.get(code=pawn["pawns_type"])
        pawn = Pawn(fk_game=game,
                     fk_pawns_type=pawns_type,
                     owner=pawn["owner"],
                     vertical_coord=pawn["vertical_coord"],
                     horizontal_coord=pawn["horizontal_coord"])
        pawn.save()
    return HttpResponse(json.dumps(board.get_pawns_and_allowed_moves(game, "player1")), content_type='application/json')

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
        move = Move(params["pawn_id"], destination)
        #check move allowed
        board = Board()
        board.buildBoard(game)
        if board.is_move_allowed(moved_pawn, destination, "player1"):
            game.strokes_number = game.strokes_number + 1
            game.save()
            Pawn.move_pawn_and_kill_if_needed(move, game.strokes_number)
            # control check mat
            board.buildBoard(game)
            check_mate = board.is_check_mate_or_draw("player2")
            if check_mate == "checkmate":
                return HttpResponse(json.dumps("player1"))
            if check_mate == "draw":
                return HttpResponse(json.dumps("draw"))
            #move player 2 pawn with ia
            ia = IA(game, "player2")
            ia_move = ia.play()
            Pawn.move_pawn_and_kill_if_needed(ia_move, game.strokes_number)
            # control check mat
            check_mate = board.is_check_mate_or_draw("player1")
            if check_mate == "checkmate":
                return HttpResponse(json.dumps("player2"))
            if check_mate == "draw":
                return HttpResponse(json.dumps("draw"))
        return HttpResponse(json.dumps(board.get_pawns_and_allowed_moves(game, "player1")))
    elif request.method == 'OPTIONS':
        return HttpResponse("ok")

