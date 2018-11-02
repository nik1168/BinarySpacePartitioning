import itertools
import math
import os
import sys

from bsp_handler import BSPHandler
from plane import Plane
from segment_mapper import SegmentMapper


class Main:
    def __init__(self):
        print("Binary Space Partitioning")
        self.segment_mapper = SegmentMapper()
        self.plane = Plane()

    def run(self):
        """
        Add segments to plane and run algorithm with all possible permutations of the set of segments
        """
        print('Number of arguments:', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))

        if len(sys.argv) > 1:
            file_name = sys.argv[1]
            if os.path.exists(file_name):
                segments = self.segment_mapper.map_file_to_tasks(file_name)
                self.add_segments_to_plane(segments)
                n = len(self.plane.get_line_segments())
                all_possible_permutation = list(
                    itertools.permutations(self.plane.get_line_segments()))
                segment_node_counter_array = []
                for i, permutation in enumerate(all_possible_permutation):
                    print("Permutation: ", i + 1)
                    [print(segment.display()) for segment in permutation]
                    bsp_handler = BSPHandler(permutation)
                    bsp_handler.execute()  # Execute algorithm
                    segment_node_counter_array.append(bsp_handler.node_counter)
                print("All possible permutations length: ", len(all_possible_permutation))
                print("max number of nodes: ", max(segment_node_counter_array))
                print("min number of nodes: ", min(segment_node_counter_array))
                upper_bound = n * math.log2(n)
                print("Upper bound: ", upper_bound)

            else:
                print("File not found")

    def add_segments_to_plane(self, segments):
        for segment in segments:
            self.plane.add_segment(segment)


main = Main()
main.run()
