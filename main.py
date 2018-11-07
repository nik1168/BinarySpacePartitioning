import itertools
import os
import sys
from fractions import Fraction

from bsp_handler import BSPHandler
from plane import Plane
from segment_mapper import SegmentMapper


class Main:
    def __init__(self):
        """
        Init Main class with plane and segment mapper
        """
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
                segments = self.segment_mapper.map_file_to_tasks(file_name)  # Get segments from text file
                self.add_segments_to_plane(segments)  # Add segments to the plane
                n = len(self.plane.get_line_segments())  # Get length of segments
                all_possible_permutation = list(
                    itertools.permutations(self.plane.get_line_segments()))  # Get All Possible permutations of segments
                segment_node_counter_array = []  # Array declared for counting the cells of each set of segments

                for i, permutation in enumerate(all_possible_permutation):
                    print("Permutation: ", i + 1)
                    [print(segment.display()) for segment in permutation]
                    bsp_handler = BSPHandler(permutation)  # Instance a new BSP handler object with a permutation
                    bsp_handler.execute()  # Execute algorithm
                    segment_node_counter_array.append(bsp_handler.node_counter)

                print("All possible permutations length: ", len(all_possible_permutation))
                print("max number of cells: ", max(segment_node_counter_array))
                print("min number of cells: ", min(segment_node_counter_array))
                harmonic_number = lambda n: sum(Fraction(1, d) for d in range(1, n + 1))  # Get harmonic number

                upper_bound = float(n + ((2 * n) * (harmonic_number(n))))
                print("Upper bound: ", upper_bound)

            else:
                print("File not found")

    def add_segments_to_plane(self, segments):
        for segment in segments:
            self.plane.add_segment(segment)


main = Main()
main.run()
