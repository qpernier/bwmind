import pprint
import random

from app.board.move import Move
from app.board.coord import Coord


class Random:

    def play(self, game, board, player):
        pawns = board.get_pawns_and_allowed_moves(game, player)
        #remove ennemy pawns

        allowed_moves = []
        while len(allowed_moves) < 1:
            moved_pawn = pawns[random.randrange(len(pawns))]
            if moved_pawn["owner"] == player:
                allowed_moves = moved_pawn["allowed_move"]
        destination_coord = allowed_moves[random.randrange(len(allowed_moves))]
        return Move(moved_pawn["id"], Coord(destination_coord["vertical_coord"], destination_coord["horizontal_coord"]))
