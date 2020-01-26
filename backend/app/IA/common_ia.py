"""
IA utility class
"""
class CommonIA:

    values = {
        "pawn" : 1.0,
        "knight" : 3.2,
        "bishop" : 3.33,
        "rook" : 5.1,
        "queen" : 8.8,
        "king": 400
        }

    """
    Assess the current score of the player
    """
    def assessment(self, board, player):
        value = 0
        board_dict = board.get_board()
        for vertical_coord in board_dict:
            for horizontal_coord in board_dict[vertical_coord]:
                pawn = board_dict[vertical_coord][horizontal_coord]
                if pawn.get_owner() == player:
                    value = value + self.values[pawn.get_pawn_type()]
                else:
                    value = value - self.values[pawn.get_pawn_type()]
        return value