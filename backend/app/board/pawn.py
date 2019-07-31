class Pawn():
    def __init__(self, owner, pawn_type):
        self.owner = owner
        self.pawn_type = pawn_type

    def __str__(self):
        return "owner : " + self.owner + " type : " + self.pawn_type

    def get_owner(self):
        return self.owner

    def get_pawn_type(self):
        return self.pawn_type
