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
        self.test1()
        # self.test_example()

        random_permutation_segments = np.random.permutation(self.plane.get_line_segments())
        print("Random permutation")
        [print(segment.display()) for segment in random_permutation_segments]
        bsp_handler = BSPHandler(self.plane.get_line_segments())
        bsp_handler.execute()

    def test1(self):
        a_segment = LineSegment("A", 6, 4, 7, 4)
        b_segment = LineSegment("B", 4, 3, 4, 5)
        c_segment = LineSegment("C", 8, 1, 10, 5)
        d_segment = LineSegment("D", 5, 1, 2, 5)
        self.plane.add_segment(a_segment)
        self.plane.add_segment(d_segment)
        self.plane.add_segment(b_segment)
        self.plane.add_segment(c_segment)

    def test_example(self):
        a_segment = LineSegment("A", 6, 4, 7, 4)
        b_segment = LineSegment("B", 4, 3, 4, 5)
        c_segment = LineSegment("C", 8, 1, 10, 5)
        d_segment = LineSegment("D", 5, 1, 2, 5)
        self.plane.add_segment(a_segment)
        self.plane.add_segment(b_segment)
        self.plane.add_segment(c_segment)
        self.plane.add_segment(d_segment)

    def test2(self):
        a_segment = LineSegment("A", 2, 1, 4, 3)
        b_segment = LineSegment("B", 6, 0, 5, 2)
        c_segment = LineSegment("C", 4, 6, 8, 2)
        d_segment = LineSegment("D", 6, 6, 7, 10)
        e_segment = LineSegment("E", 8, 4, 10, 5)
        f_segment = LineSegment("F", 10, 3, 12, 2)
        g_segment = LineSegment("G", 10, 8, 11, 12)
        h_segment = LineSegment("H", 0, 0, 4, 1)

        self.plane.add_segment(a_segment)
        self.plane.add_segment(b_segment)
        self.plane.add_segment(c_segment)
        self.plane.add_segment(d_segment)
        self.plane.add_segment(e_segment)
        self.plane.add_segment(f_segment)
        self.plane.add_segment(g_segment)
        self.plane.add_segment(h_segment)


main = Main()
main.run()
