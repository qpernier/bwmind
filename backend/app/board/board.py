from app.board.coord import Coord
from app.models import Pawn as Pawn_model
from app.board.pawn import Pawn



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

    def allowed_move(self, pawn_type, owner, vertical_coord, horizontal_coord):
        pawn = Pawn(owner,pawn_type)
        if pawn.owner == "player1" and pawn.pawn_type == "pawn":
            return self._allowed_move_pawn_player1(pawn, vertical_coord, horizontal_coord)


    def buildBoard(self, game):
        pawn_class = Pawn_model()
        for pawn_dict in pawn_class.get_pawns(game):
            self.board[pawn_dict["vertical_coord"]][pawn_dict["horizontal_coord"]] = Pawn(pawn_dict["owner"],
                                                                                          pawn_dict["code"])
    def _allowed_move_pawn_player1(self, pawn, vertical_coord, horizontal_coord):
        print("test")
        allowed_move = []
        if vertical_coord == 7:
            print("test1")
            return []
        if horizontal_coord not in self.board[vertical_coord+1].keys():
            print("test2")
            allowed_move.append(Coord(vertical_coord+1, horizontal_coord).to_dict())

        if horizontal_coord-1 in self.board[vertical_coord+1].keys() and self.board[vertical_coord+1][horizontal_coord-1] == "player2":
            print("test3")
            allowed_move.append(Coord(vertical_coord + 1, horizontal_coord-1).to_dict())

        if horizontal_coord+1 in self.board[vertical_coord+1].keys() and self.board[vertical_coord+1][horizontal_coord+1] == "player2":
            print("test4")
            allowed_move.append(Coord(vertical_coord + 1, horizontal_coord+1).to_dict())

        return allowed_move





