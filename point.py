class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def display(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def get_x(self):
        return float(self.x)

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return float(self.y)

    def set_y(self, y):
        self.y = y
