import constants
from line_segment import LineSegment
from line_segment_manager import LineSegmentManager


class BSPHandler:
    def __init__(self, line_segments):
        self.line_segments = line_segments
        self.line_segment_manager = LineSegmentManager()
        self.node_counter = 0

    def execute(self):
        print("Executing algorithm ")
        self.handle_list(self.line_segments)
        print("Node counter")
        print(self.node_counter)

    def handle_list(self, line_segments):
        self.node_counter = self.node_counter + 1
        root_segment = line_segments[0]
        segments_up, segments_down = self.get_segments_directions_relative_to_parent_node(
            root_segment, line_segments[1:])
        if len(segments_up) > 0:
            self.handle_list(segments_up)
        if len(segments_down) > 0:
            self.handle_list(segments_down)

    def get_segments_directions_relative_to_parent_node(self, parent_segment, segments):
        segments_up = []
        segments_down = []
        for segment in segments:
            direction = self.line_segment_manager.get_segment_direction_relative_to_straight_line(
                segment,
                parent_segment)
            if direction == constants.UP:
                segments_up.append(segment)
            elif direction == constants.DOWN:
                segments_down.append(segment)
            else:
                segment_up_intersection, segment_down_intersection = self.split_intersection_into_segment(segment,
                                                                                                          parent_segment)
                segments_up.append(segment_up_intersection)
                segments_down.append(segment_down_intersection)
        return segments_up, segments_down

    def split_intersection_into_segment(self, segment_intersect, parent_segment):
        x_intersection, y_intersection = self.line_segment_manager.get_intersection_point(segment_intersect,
                                                                                          parent_segment)
        segment_up_intersection = LineSegment(segment_intersect.get_identifier() + "1", x_intersection,
                                              y_intersection,
                                              segment_intersect.end_point.get_x(),
                                              segment_intersect.end_point.get_y())
        segment_down_intersection = LineSegment(segment_intersect.get_identifier() + "2",
                                                segment_intersect.start_point.get_x(),
                                                segment_intersect.start_point.get_y(), x_intersection,
                                                y_intersection)
        return segment_up_intersection, segment_down_intersection
