import constants


class LineSegmentManager:

    def __init__(self):
        pass

    def get_segment_direction_relative_to_straight_line(self, segment, compare_to_segment):
        y_prime_start = compare_to_segment.get_y_based_on_x(segment.start_point.get_x())
        y_prime_end = compare_to_segment.get_y_based_on_x(segment.end_point.get_x())
        first_point_position = self.get_direction_relative_to_point(y_prime_start, segment.start_point.get_y())
        second_point_position = self.get_direction_relative_to_point(y_prime_end, segment.end_point.get_y())
        direction_of_segment = self.get_segment_position_relative_to_points(first_point_position, second_point_position)
        print("First point direction: ", first_point_position)
        print("Second point direction: ", second_point_position)
        print("direction_of_segment: ", direction_of_segment)
        return direction_of_segment

    def get_direction_relative_to_point(self, y_prime, y_segment):
        if y_prime < y_segment:
            return constants.UP
        elif y_prime > y_segment:
            return constants.DOWN
        else:
            return constants.INTERSECTS

    def get_segment_position_relative_to_points(self, first_point_position, second_point_position):
        if first_point_position == constants.UP and second_point_position == constants.UP:
            return constants.UP
        elif first_point_position == constants.DOWN and second_point_position == constants.DOWN:
            return constants.DOWN
        else:
            return constants.INTERSECTS
