""""
Basic IA assess just next move
"""
from app.IA.common_ia import CommonIA


class Basic:

    def play(self, game, board, player):
        common_ia = CommonIA()
        score = -1000
        shadowMove = None
        #process moves
        next_moves = board.get_allowed_moves(player)
        #for each moves assess player score
        for next_move in next_moves:
            sonBoard = board.get_son(next_move)
            current_score = common_ia.assessment(sonBoard, player)
            if current_score > score:
                score = current_score
                shadowMove = next_move
        if shadowMove is None:
            raise Exception("No move allowed")
        return shadowMove.to_move(game)
