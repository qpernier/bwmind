from app.board.board import Board
from app.models import IA as IA_model
from app.IA.random import Random


class IA():

    def __init__(self, game, player):
        self.game = game
        self.ia_model = game.fk_ia2
        self.player = player
        if self.ia_model.code == "random":
            self.ia = Random()

    def play(self):
        board = Board()
        board.buildBoard(self.game)
        return self.ia.play(self.game, board, self.player)

