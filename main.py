import numpy as np

from plane import Plane
from line_segment import LineSegment


class Main:
    def __init__(self):
        print("Binary Space Partitioning")
        self.plane = Plane()

    def run(self):
        print("Running main")
        a_segment = LineSegment("A", 4, 3, 6, 3)
        print("Slope of a_segment", a_segment.get_slope())
        self.plane.add_segment(a_segment)
        b_segment = LineSegment("B", 4, 2, 4, 4)
        print("Slope of b_segment", b_segment.get_slope())
        self.plane.add_segment(b_segment)
        c_segment = LineSegment("C", 6, 1, 8, 5)
        print("Slope of c_segment", c_segment.get_slope())
        self.plane.add_segment(c_segment)
        d_segment = LineSegment("D", 3, 1, 1, 5)
        print("Slope of d_segment", d_segment.get_slope())
        self.plane.add_segment(d_segment)
        self.plane.print_segments()
        random_permutation = np.random.permutation(len(self.plane.get_line_segments()))
        print("Random permutation: ", random_permutation)


main = Main()
main.run()
