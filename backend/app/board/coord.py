class Coord():
    def __init__(self, vertical_coord, horizontal_coord):
        self.vertical_coord = vertical_coord
        self.horizontal_coord = horizontal_coord

    def __eq__(self, other):
        return self.vertical_coord == other.vertical_coord and self.horizontal_coord == other.horizontal_coord

    def to_dict(self):
        return {"vertical_coord": self.vertical_coord, "horizontal_coord": self.horizontal_coord}