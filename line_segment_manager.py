import constants
from line_segment import LineSegment


class LineSegmentManager:

    def __init__(self):
        pass

    def get_segment_direction_relative_to_straight_line(self, segment, compare_to_segment):
        """
        Return line segment orientation relative to a straight line
        :param segment: LineSegment
        :param compare_to_segment:  LineSegment
        :return: direction_of_segment : String <"up", "down", "intersects">
        """
        if compare_to_segment.get_slope() is None:  # Check if line is vertical
            first_point_position = self.get_vertical_line_position(segment.start_point.get_x(),
                                                                   compare_to_segment.start_point.get_x())
            second_point_position = self.get_vertical_line_position(segment.end_point.get_x(),
                                                                    compare_to_segment.end_point.get_x())
        else:
            y_prime_start = compare_to_segment.get_y_based_on_x(segment.start_point.get_x())
            y_prime_end = compare_to_segment.get_y_based_on_x(segment.end_point.get_x())
            first_point_position = self.get_direction_relative_to_point(y_prime_start, segment.start_point.get_y())
            second_point_position = self.get_direction_relative_to_point(y_prime_end, segment.end_point.get_y())
        direction_of_segment = self.get_segment_position_relative_to_points(first_point_position, second_point_position)
        return direction_of_segment

    def get_intersection_point(self, line_segment_a, line_segment_b):
        """
        Check intersection point of two line segments
        :param line_segment_a:
        :param line_segment_b:
        :return: r
        """
        l1_prime = line_segment_a.get_line()
        l2_prime = line_segment_b.get_line()
        r = self.intersection(l1_prime, l2_prime)
        return r

    @staticmethod
    def intersection(l1, l2):
        """
        Gets intersection of two lines
        :param l1:
        :param l2:
        :return:
        """
        d = l1[0] * l2[1] - l1[1] * l2[0]
        dx = l1[2] * l2[1] - l1[1] * l2[2]
        dy = l1[0] * l2[2] - l1[2] * l2[0]
        if d != 0:
            x = dx / d
            y = dy / d
            return x, y
        else:
            return False

    @staticmethod
    def get_vertical_line_position(point_x_segment, point_x_parent):
        """
        Gets the position of a vertical line_segment relative to another line_segment
        :param point_x_segment:
        :param point_x_parent:
        :return:
        """
        if point_x_segment < point_x_parent:
            direction = constants.UP
        elif point_x_segment > point_x_parent:
            direction = constants.DOWN
        else:
            direction = constants.INTERSECTS
        return direction

    @staticmethod
    def get_direction_relative_to_point(y_prime, y_segment):
        """
        Get orientation of point relative to a segment
        :param y_prime: float
        :param y_segment: float
        :return: orientation : string <"up", "down", "intersects">
        """
        if y_prime < y_segment:
            return constants.UP
        elif y_prime > y_segment:
            return constants.DOWN
        else:
            return constants.INTERSECTS

    @staticmethod
    def get_segment_position_relative_to_points(first_point_position, second_point_position):
        """
        Gets segment positions based on the criteria of a line segment
        :param first_point_position:
        :param second_point_position:
        :return:
        """
        if first_point_position == constants.UP and second_point_position == constants.UP:
            return constants.UP
        elif first_point_position == constants.DOWN and second_point_position == constants.DOWN:
            return constants.DOWN
        elif first_point_position == constants.DOWN and second_point_position == constants.INTERSECTS:
            return constants.DOWN
        elif first_point_position == constants.UP and second_point_position == constants.INTERSECTS:
            return constants.UP
        elif first_point_position == constants.INTERSECTS and second_point_position == constants.DOWN:
            return constants.DOWN
        elif first_point_position == constants.INTERSECTS and second_point_position == constants.UP:
            return constants.UP
        else:
            return constants.INTERSECTS

    def get_segments_directions_relative_to_parent_node(self, parent_segment, segments):
        """
        Returns segments directions relative to a parent cell
        :param parent_segment: LineSegment
        :param segments: Array<LineSegment>
        :return: segments_up, segments_down
        """
        segments_up = []
        segments_down = []
        for segment in segments:
            direction = self.get_segment_direction_relative_to_straight_line(
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
        """
        Split a segment in two based on intersection point of a previous segment
        :param segment_intersect:
        :param parent_segment:
        :return:
        """
        x_intersection, y_intersection = self.get_intersection_point(segment_intersect,
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
