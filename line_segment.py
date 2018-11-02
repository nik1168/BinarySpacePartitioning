from math import hypot

from point import Point


class LineSegment:
    def __init__(self, identifier, x_begin, y_begin, x_end, y_end):
        self.identifier = identifier
        self.start_point = Point(x_begin, y_begin)
        self.end_point = Point(x_end, y_end)

    def get_identifier(self):
        return self.identifier

    def get_length(self):
        return hypot(self.end_point.get_x() - self.start_point.get_x(), self.end_point.get_y() -
                     self.start_point.get_y())

    def get_slope(self):
        if float(self.end_point.get_x()) == float(self.start_point.get_x()):
            return None
        else:
            return (float((self.end_point.get_y() - self.start_point.get_y()) / (
                    self.end_point.get_x() - self.start_point.get_x())))

    def get_displacement(self):
        return self.start_point.get_y() - (self.get_slope() * self.start_point.get_x())

    def print_straight_line(self):
        print("Line Solution is y = {m}x + {b}".format(m=self.get_slope(), b=self.get_displacement()))

    def get_line(self):
        a = (self.start_point.get_y() - self.end_point.get_y())
        b = (self.end_point.get_x() - self.start_point.get_x())
        c = (self.start_point.get_x() * self.end_point.get_y() - self.end_point.get_x() * self.start_point.get_y())
        return a, b, -c

    def get_y_based_on_x(self, x):
        if self.get_slope() is None:
            return x
        return (self.get_slope() * x) + self.get_displacement()

    def display(self):
        return "line segment: " + self.identifier + " Init Point:" + self.start_point.display() + " End Point: " + self.end_point.display()
