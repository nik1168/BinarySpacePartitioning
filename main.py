import numpy as np

from plane import Plane
from line_segment import LineSegment
from bsp_handler import BSPHandler
from line_segment_manager import LineSegmentManager


class Main:
    def __init__(self):
        print("Binary Space Partitioning")
        self.plane = Plane()
        self.line_segment_manager = LineSegmentManager()

    def run(self):
        print("Running main")
        a_segment = LineSegment("A", 1, 2, 5, 4)
        print("Slope of a_segment", a_segment.get_slope())
        a_segment.print_straight_line()
        self.plane.add_segment(a_segment)
        b_segment = LineSegment("B", 2, 0, 2, 1)
        print("Slope of b_segment", b_segment.get_slope())
        b_direction_relative_to_a = self.line_segment_manager.get_segment_direction_relative_to_straight_line(b_segment,
                                                                                                              a_segment)
        print("b_direction_relative_to_a", b_direction_relative_to_a)
        self.plane.add_segment(b_segment)
        c_segment = LineSegment("C", 6, 1, 8, 5)
        print("Slope of c_segment", c_segment.get_slope())
        self.plane.add_segment(c_segment)
        d_segment = LineSegment("D", 3, 1, 1, 5)
        print("Slope of d_segment", d_segment.get_slope())
        self.plane.add_segment(d_segment)
        self.plane.print_segments()
        random_permutation_segments = np.random.permutation(self.plane.get_line_segments())
        print("Random permutation: ", random_permutation_segments)
        bsp_handler = BSPHandler(random_permutation_segments)
        bsp_handler.execute()


main = Main()
main.run()
