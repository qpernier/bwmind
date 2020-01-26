"""
Move from initial coord to dest coord
"""
from app.board.move import Move
from app.models import Pawn


class ShadowMove:


    def __str__(self):
        return "initial_coord : " + str(self.initial_coord) + " dest_coord : " + str(self.dest_coord)

    def __repr__(self):
        return "initial_coord : " + str(self.initial_coord) + " dest_coord : " + str(self.dest_coord)

    def __init__(self, initial_coord, dest_coord):
        self.initial_coord = initial_coord
        self.dest_coord = dest_coord

    def get_initial_coord(self):
        return self.initial_coord

    def get_dest_coord(self):
        return self.dest_coord

    """
    Return Move object from shadowMove
    """
    def to_move(self, game):
        pawns = Pawn.objects.filter(vertical_coord=self.initial_coord.vertical_coord ,horizontal_coord=self.initial_coord.horizontal_coord,fk_game=game)
        return Move(pawns[0].id, self.dest_coord)
