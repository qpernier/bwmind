class Coord():
    def __init__(self, vertical_coord, horizontal_coord):
        self.vertical_coord = vertical_coord
        self.horizontal_coord = horizontal_coord

    def to_dict(self):
        return {"vertical_coord": self.vertical_coord, "horizontal_coord": self.horizontal_coord}