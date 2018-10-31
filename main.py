import numpy as np

from bsp_handler import BSPHandler
from line_segment import LineSegment
from line_segment_manager import LineSegmentManager
from plane import Plane


class Main:
    def __init__(self):
        print("Binary Space Partitioning")
        self.plane = Plane()
        self.line_segment_manager = LineSegmentManager()

    def run(self):
        print("Running main")
        a_segment = LineSegment("A", 6, 4, 7, 4)
        self.plane.add_segment(a_segment)
        b_segment = LineSegment("B", 4, 3, 4, 5)
        self.plane.add_segment(b_segment)
        c_segment = LineSegment("C", 8, 1, 10, 5)
        self.plane.add_segment(c_segment)
        d_segment = LineSegment("D", 5, 1, 2, 5)
        self.line_segment_manager.get_intersection_point(a_segment, d_segment)
        self.plane.add_segment(d_segment)
        random_permutation_segments = np.random.permutation(self.plane.get_line_segments())
        print("Random permutation")
        [print(segment.display()) for segment in random_permutation_segments]
        bsp_handler = BSPHandler(random_permutation_segments)
        bsp_handler.execute()


main = Main()
main.run()
