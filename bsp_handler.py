from line_segment_manager import LineSegmentManager


class BSPHandler:

    def __init__(self, line_segments):
        self.line_segments = line_segments
        self.line_segment_manager = LineSegmentManager()
        self.node_counter = 0

    def execute(self):
        self.set_cell(self.line_segments)
        print("Cell counter")
        print(self.node_counter)

    def set_cell(self, line_segments):
        self.node_counter = self.node_counter + 1
        root_segment = line_segments[0]
        print("Segment to extend: ")
        print(root_segment.display())
        segments_up, segments_down = self.line_segment_manager.get_segments_directions_relative_to_parent_node(
            root_segment, line_segments[1:])
        print("Segments front: ")
        [print(segment.display()) for segment in segments_up]
        print("Segments back: ")
        [print(segment.display()) for segment in segments_down]
        if len(segments_up) > 0:
            self.set_cell(segments_up)
        if len(segments_down) > 0:
            self.set_cell(segments_down)
