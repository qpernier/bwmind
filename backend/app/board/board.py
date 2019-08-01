from app.board.coord import Coord
from app.models import Pawn as Pawn_model
from app.board.pawn import Pawn
import pprint
import copy



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
    def get_pawns_and_allowed_moves(self,game, player):
        pawn_model = Pawn_model()
        pawn_queryset = pawn_model.get_pawns(game)

        self.buildBoard(game, pawn_queryset)
        for pawn_dict in pawn_queryset:
            pawn_dict["allowed_move"] = self.allowed_move(pawn_dict["code"], pawn_dict["owner"],
                                                        pawn_dict["vertical_coord"], pawn_dict["horizontal_coord"],player)
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
      Build the board to know where are each pawns
      """

    def buildBoard(self, game, pawn_queryset=None):
        self.board = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}}
        if pawn_queryset is None:
            pawn_class = Pawn_model()
            pawn_queryset = pawn_class.get_pawns(game)
        for pawn_dict in pawn_queryset:
            self.board[pawn_dict["vertical_coord"]][pawn_dict["horizontal_coord"]] = Pawn(pawn_dict["owner"],
                                                                                          pawn_dict["code"])
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.board)

    """
    List all allowed move for a pawn
    """
    def allowed_move(self, pawn_type, owner, vertical_coord, horizontal_coord, player, check_king_under_attack=True):
        pawn = Pawn(owner, pawn_type)
        allowed_moves = []
        if pawn.owner == "player1" and pawn.pawn_type == "pawn":
            allowed_moves = self._allowed_move_pawn_player1(vertical_coord, horizontal_coord, not check_king_under_attack)
        elif pawn.owner == "player2" and pawn.pawn_type == "pawn":
            allowed_moves = self._allowed_move_pawn_player2(vertical_coord, horizontal_coord, not check_king_under_attack)
        elif pawn.pawn_type == "king":
            allowed_moves = self._allowed_move_king(vertical_coord, horizontal_coord, pawn.owner)
        elif pawn.pawn_type == "queen":
            allowed_moves = self._allowed_move_queen(vertical_coord, horizontal_coord, pawn.owner)
        elif pawn.pawn_type == "bishop":
            allowed_moves = self._allowed_move_bishop(vertical_coord, horizontal_coord, pawn.owner)
        elif pawn.pawn_type == "rook":
            allowed_moves = self._allowed_move_rook(vertical_coord, horizontal_coord, pawn.owner)
        elif pawn.pawn_type == "knight":
            allowed_moves = self._allowed_move_knight(vertical_coord, horizontal_coord, pawn.owner)

        if check_king_under_attack:
            allowed_moves = self._remove_king_under_attack_moves(Coord(vertical_coord, horizontal_coord ),allowed_moves, pawn, player)

        return allowed_moves

    """
    Remove king under attack from allowed moves
    """
    def _remove_king_under_attack_moves(self, initialCoord, allowed_moves, pawn, player):
        safe_allowed_moves = []
        enemy = "player2" if player == "player1" else "player1"
        for move in allowed_moves:
            board = copy.deepcopy(self.board)
            #remove last position
            board[initialCoord.vertical_coord].pop(initialCoord.horizontal_coord)
            #add new position
            board[initialCoord.vertical_coord][initialCoord.horizontal_coord] = pawn
            #process enemy moves
            enemy_moves = []
            for vertical_coord in range(8):
                for horizontal_coord in range(8):
                    if self._is_enemy(Coord(vertical_coord,horizontal_coord), player, board):
                        enemy_pawn = board[vertical_coord][horizontal_coord]
                        enemy_moves.extend(self.allowed_move(enemy_pawn.pawn_type, enemy_pawn.owner, vertical_coord, horizontal_coord, enemy, False))
            kings_coord = self._get_king_coordinate(board, player)
            if kings_coord not in enemy_moves:
                safe_allowed_moves.append(move)

        return safe_allowed_moves

    """
    Return the king coordinate of the player 'player'
    """
    def _get_king_coordinate(self, board, player):
        for vertical_coord in range(8):
            for horizontal_coord in range(8):
                pawn = board[vertical_coord].get(horizontal_coord, None)
                if pawn is not None:
                    if pawn.pawn_type == "king" and pawn.owner == player:
                        return Coord(vertical_coord,horizontal_coord)
        raise Exception("No king found")


    def _allowed_move_pawn_player1(self, vertical_coord, horizontal_coord, disable_no_attack_moves=False):
        allowed_move = []
        if vertical_coord == 7:
            return []
        if self._is_empty(horizontal_coord, vertical_coord+1, self.board) and not disable_no_attack_moves:
            allowed_move.append(Coord(vertical_coord+1, horizontal_coord).to_dict())

        if not self._is_empty(horizontal_coord - 1, vertical_coord+1, self.board) and self.board[vertical_coord+1][horizontal_coord-1].owner == "player2":
            allowed_move.append(Coord(vertical_coord + 1, horizontal_coord-1).to_dict())

        if not self._is_empty(horizontal_coord + 1, vertical_coord+1, self.board) and self.board[vertical_coord+1][horizontal_coord+1].owner == "player2":
            allowed_move.append(Coord(vertical_coord + 1, horizontal_coord+1).to_dict())

        if self._is_empty(horizontal_coord, vertical_coord+1, self.board) and self._is_empty(horizontal_coord, vertical_coord+2, self.board) and vertical_coord == 1 and not disable_no_attack_moves:
            allowed_move.append(Coord(vertical_coord+2, horizontal_coord).to_dict())

        return allowed_move

    def _allowed_move_pawn_player2(self, vertical_coord, horizontal_coord, disable_no_attack_moves=False):
        allowed_move = []
        if vertical_coord == 0:
            return []
        if self._is_empty(horizontal_coord, vertical_coord-1, self.board)and not disable_no_attack_moves:
            allowed_move.append(Coord(vertical_coord-1, horizontal_coord).to_dict())

        if not self._is_empty(horizontal_coord - 1, vertical_coord-1, self.board) and self.board[vertical_coord-1][horizontal_coord-1].owner == "player1":
            allowed_move.append(Coord(vertical_coord - 1, horizontal_coord-1).to_dict())

        if not self._is_empty(horizontal_coord + 1, vertical_coord-1, self.board) and self.board[vertical_coord-1][horizontal_coord+1].owner == "player1":
            allowed_move.append(Coord(vertical_coord - 1, horizontal_coord+1).to_dict())

        if self._is_empty(horizontal_coord, vertical_coord-1, self.board) and self._is_empty(horizontal_coord, vertical_coord-2, self.board) and vertical_coord == 6 and not disable_no_attack_moves:
            allowed_move.append(Coord(vertical_coord-2, horizontal_coord).to_dict())

        return allowed_move

    def _allowed_move_king(self, vertical_coord, horizontal_coord, owner):
        return []
        #TODO

    def _allowed_move_queen(self, vertical_coord, horizontal_coord, owner):
        return []
        #TODO

    def _allowed_move_bishop(self, vertical_coord, horizontal_coord, owner):
        return []
        #TODO

    def _allowed_move_rook(self, vertical_coord, horizontal_coord, owner):
        return []
        #TODO

    def _allowed_move_knight(self, vertical_coord, horizontal_coord, owner):
        allowed_move = []
        new_coord = Coord(vertical_coord + 2, horizontal_coord + 1)
        if self._is_in_board(new_coord) and not self._is_mine(new_coord, owner, self.board):
            allowed_move.append(new_coord.to_dict())
        return allowed_move

    """
    Rturn True if square is empty
    """
    def _is_empty(self, horizontal_coord, vertical_coord, board):
        return horizontal_coord not in board[vertical_coord].keys()

    """
    Return True if coord is in board
    """
    def _is_in_board(self, coord):
        return not (coord.vertical_coord < 0 or coord.vertical_coord > 7 or coord.horizontal_coord < 0 or coord.horizontal_coord > 7)

    """
    Return True if the square is occuped by mine pawn
    """
    def _is_mine(self, coord, player, board):
        if not self._is_in_board(coord):
            return False
        if self._is_empty(coord.horizontal_coord, coord.vertical_coord, board):
            return False
        return board[coord.vertical_coord][coord.horizontal_coord].owner == player

    """
    Return True if the square is occuped by enemy pawn
    """
    def _is_enemy(self, coord, player, board):
        if not self._is_in_board(coord):
            return False
        if self._is_empty(coord.horizontal_coord, coord.vertical_coord, board):
            return False
        return board[coord.vertical_coord][coord.horizontal_coord].owner != player




