import itertools
import math

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
        # self.test_segments_1()
        self.test_segments_4()
        print("All possible permutations")
        n = len(self.plane.get_line_segments())
        all_possible_permutation = list(itertools.permutations(self.plane.get_line_segments()))
        counter_array = []
        for i, permutation in enumerate(all_possible_permutation):
            print("Permutation: ", i)
            [print(segment.display()) for segment in permutation]
            bsp_handler = BSPHandler(permutation)
            bsp_handler.execute()
            counter_array.append(bsp_handler.node_counter)
        print("max number of nodes: ", max(counter_array))
        print("min number of nodes: ", min(counter_array))
        upper_bound = n * math.log2(n)
        print("Upper bound: ", upper_bound)

    def test_segments_1(self):
        a_segment = LineSegment("A", 6, 4, 7, 4)
        b_segment = LineSegment("B", 4, 3, 4, 5)
        c_segment = LineSegment("C", 8, 1, 10, 5)
        d_segment = LineSegment("D", 5, 1, 2, 5)
        self.plane.add_segment(a_segment)
        self.plane.add_segment(d_segment)
        self.plane.add_segment(b_segment)
        self.plane.add_segment(c_segment)

    def test_segments_2(self):
        a_segment = LineSegment("A", 6, 4, 7, 4)
        b_segment = LineSegment("B", 4, 3, 4, 5)
        c_segment = LineSegment("C", 8, 1, 10, 5)
        d_segment = LineSegment("D", 5, 1, 2, 5)
        self.plane.add_segment(a_segment)
        self.plane.add_segment(b_segment)
        self.plane.add_segment(c_segment)
        self.plane.add_segment(d_segment)

    def test_segments_3(self):
        a_segment = LineSegment("A", 2, 1, 4, 3)
        b_segment = LineSegment("B", 6, 0, 5, 2)
        c_segment = LineSegment("C", 4, 6, 8, 2)
        d_segment = LineSegment("D", 6, 6, 7, 10)
        e_segment = LineSegment("E", 8, 4, 10, 5)
        f_segment = LineSegment("F", 10, 3, 12, 2)
        g_segment = LineSegment("G", 10, 8, 11, 12)
        h_segment = LineSegment("H", 0, 0, 4, 1)

        self.plane.add_segment(f_segment)
        self.plane.add_segment(a_segment)
        self.plane.add_segment(d_segment)
        self.plane.add_segment(c_segment)
        self.plane.add_segment(b_segment)
        self.plane.add_segment(e_segment)
        self.plane.add_segment(g_segment)
        self.plane.add_segment(h_segment)

    def test_segments_4(self):
        a_segment = LineSegment("A", 4, 1, 1, 4)
        b_segment = LineSegment("B", 5, 5, 8, 5)
        c_segment = LineSegment("C", 8, 7, 10, 10)
        d_segment = LineSegment("D", 11, 8, 14, 8)
        e_segment = LineSegment("E", 10, 4, 12, 7)
        f_segment = LineSegment("F", 6, 6, 4, 10)
        g_segment = LineSegment("G", 7, 2, 9, 3)
        h_segment = LineSegment("H", 13, 3, 13, 6)

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
