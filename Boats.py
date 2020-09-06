class Boats:
    def __init__(self, name, block_size, x, y, xstart, ystart, angle, array):
        self.name = name
        self.block_size = block_size
        self.x = x
        self.y = y
        self.xstart = xstart
        self.ystart = ystart
        self.angle = angle
        self.array = array



    # Override
    def __str__(self):
        return "Theoph's boat, located at " + str(self.x) + "," + str(self.y)

    def __repr__(self):
        return self.__str__()