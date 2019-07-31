from app.board.coord import Coord
from app.models import Pawn as Pawn_model
from app.board.pawn import Pawn
import pprint



class Board():
    board = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {} }

    def initialPosition(self):
        pawns=[]
        pawns.append({"pawns_type": "king", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 4})
        pawns.append({"pawns_type": "queen", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 3})
        pawns.append({"pawns_type": "bishop", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 2})
        pawns.append({"pawns_type": "bishop", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 5})
        pawns.append({"pawns_type": "knight", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 1})
        pawns.append({"pawns_type": "knight", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 6})
        pawns.append({"pawns_type": "rook", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 0})
        pawns.append({"pawns_type": "rook", "owner": "player1", "vertical_coord": 0, "horizontal_coord": 7})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 0})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 1})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 2})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 3})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 4})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 5})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 6})
        pawns.append({"pawns_type": "pawn", "owner": "player1", "vertical_coord": 1, "horizontal_coord": 7})
        pawns.append({"pawns_type": "king", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 4})
        pawns.append({"pawns_type": "queen", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 3})
        pawns.append({"pawns_type": "bishop", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 2})
        pawns.append({"pawns_type": "bishop", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 5})
        pawns.append({"pawns_type": "knight", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 1})
        pawns.append({"pawns_type": "knight", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 6})
        pawns.append({"pawns_type": "rook", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 0})
        pawns.append({"pawns_type": "rook", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 7})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 0})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 1})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 2})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 3})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 4})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 5})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 6})
        pawns.append({"pawns_type": "pawn", "owner": "player2", "vertical_coord": 6, "horizontal_coord": 7})
        return pawns

    """
    Get pawns and allowed moves for a game
    """
    def get_pawns_and_allowed_moves(self,game):
        pawn_model = Pawn_model()
        pawn_queryset = pawn_model.get_pawns(game)

        self.buildBoard(game, pawn_queryset)
        for pawn_dict in pawn_queryset:
            pawn_dict["allowed_move"] = self.allowed_move(pawn_dict["code"], pawn_dict["owner"],
                                                        pawn_dict["vertical_coord"], pawn_dict["horizontal_coord"])
        return pawn_queryset

    """
    Return True if the move is allowed
    """
    def is_move_allowed(self, pawn, destination):
        allowed_moves = self.allowed_move(pawn.fk_pawns_type.code, pawn.owner, pawn.vertical_coord, pawn.horizontal_coord)
        for allowed_move in allowed_moves:
            allowed_move_coord = Coord(allowed_move["vertical_coord"], allowed_move["horizontal_coord"])
            if allowed_move_coord == destination:
                return True
        return False

    """
    List all allowed move for a pawn
    """
    def allowed_move(self, pawn_type, owner, vertical_coord, horizontal_coord):
        pawn = Pawn(owner, pawn_type)
        if pawn.owner == "player1" and pawn.pawn_type == "pawn":
            return self._allowed_move_pawn_player1(vertical_coord, horizontal_coord)

    def buildBoard(self, game, pawn_queryset=None):
        self.board = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}}
        if pawn_queryset is None:
            pawn_class = Pawn_model()
            pawn_queryset = pawn_class.get_pawns(game)
        for pawn_dict in pawn_queryset:
            self.board[pawn_dict["vertical_coord"]][pawn_dict["horizontal_coord"]] = Pawn(pawn_dict["owner"],
                                                                                          pawn_dict["code"])

    def _allowed_move_pawn_player1(self, vertical_coord, horizontal_coord):
        pp = pprint.PrettyPrinter(indent=4)
        allowed_move = []
        if vertical_coord == 7:
            return []
        if self._is_empty(horizontal_coord, vertical_coord+1):
            allowed_move.append(Coord(vertical_coord+1, horizontal_coord).to_dict())

        if not self._is_empty(horizontal_coord - 1, vertical_coord+1) and self.board[vertical_coord+1][horizontal_coord-1].owner == "player2":
            allowed_move.append(Coord(vertical_coord + 1, horizontal_coord-1).to_dict())

        if not self._is_empty(horizontal_coord + 1, vertical_coord+1) and self.board[vertical_coord+1][horizontal_coord+1].owner == "player2":
            allowed_move.append(Coord(vertical_coord + 1, horizontal_coord+1).to_dict())

        if self._is_empty(horizontal_coord, vertical_coord+1) and self._is_empty(horizontal_coord, vertical_coord+2) and vertical_coord == 1:
            allowed_move.append(Coord(vertical_coord+2, horizontal_coord).to_dict())

        pp.pprint(allowed_move)
        return allowed_move

    """
    Rturn True if square is empty
    """
    def _is_empty(self, horizontal_coord, vertical_coord):
        return horizontal_coord not in self.board[vertical_coord].keys()





