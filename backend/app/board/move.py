"""
move pawn with pawn_id to coord
"""


class Move:

    def __init__(self, pawn_id, coord):
        self.pawn_id = pawn_id
        self.coord = coord

    def __repr__(self):
        return "pawn id : " + str(self.pawn_id) + " dest_coord : " + str(self.coord)
