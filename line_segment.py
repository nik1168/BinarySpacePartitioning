from point import Point
from math import hypot


class LineSegment:
    def __init__(self, identifier, x_begin, x_end, y_begin, y_end):
        self.identifier = identifier
        self.start_point = Point(x_begin, x_end)
        self.end_point = Point(y_begin, y_end)

    def get_length(self):
        return hypot(self.end_point.get_x() - self.start_point.get_x(), self.end_point.get_y() -
                     self.start_point.get_y())

    def get_slope(self):
        if self.end_point.get_x() == self.start_point.get_x():
            return None
        else:
            return (float((self.end_point.get_y() - self.start_point.get_y()) / (
                    self.end_point.get_x() - self.start_point.get_x())))

    def get_displacement(self):
        return self.start_point.get_y() - (self.get_slope() * self.start_point.get_x())

    def print_straight_line(self):
        print("Line Solution is y = {m}x + {b}".format(m=self.get_slope(), b=self.get_displacement()))

    def get_y_based_on_x(self, x):
        return (self.get_slope() * x) + self.get_displacement()

    def display(self):
        return "line segment: " + self.identifier + " Init:" + self.start_point.display() + " End: " + self.end_point.display()
