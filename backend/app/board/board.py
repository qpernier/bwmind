class Board():
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
        pawns.append({"pawns_type": "king", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 3})
        pawns.append({"pawns_type": "queen", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 4})
        pawns.append({"pawns_type": "bishop", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 2})
        pawns.append({"pawns_type": "bishop", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 5})
        pawns.append({"pawns_type": "knight", "owner": "player2", "vertical_coord": 7, "horizontal_coord": 4})
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