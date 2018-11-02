from line_segment_manager import LineSegmentManager


class BSPHandler:

    def __init__(self, line_segments):
        self.line_segments = line_segments
        self.line_segment_manager = LineSegmentManager()
        self.node_counter = 0

    def execute(self):
        self.set_node(self.line_segments)
        print("Node counter")
        print(self.node_counter)

    def set_node(self, line_segments):
        self.node_counter = self.node_counter + 1
        root_segment = line_segments[0]
        segments_up, segments_down = self.line_segment_manager.get_segments_directions_relative_to_parent_node(
            root_segment, line_segments[1:])
        if len(segments_up) > 0:
            self.set_node(segments_up)
        if len(segments_down) > 0:
            self.set_node(segments_down)
