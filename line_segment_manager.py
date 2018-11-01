import constants


class LineSegmentManager:

    def __init__(self):
        pass

    def get_segment_direction_relative_to_straight_line(self, segment, compare_to_segment):
        if compare_to_segment.get_slope() is None:
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

        l1_prime = line_segment_a.get_line()
        l2_prime = line_segment_b.get_line()
        r = self.intersection(l1_prime, l2_prime)
        return r

    @staticmethod
    def line(p1, p2):
        a = (p1[1] - p2[1])
        b = (p2[0] - p1[0])
        c = (p1[0] * p2[1] - p2[0] * p1[1])
        return a, b, -c

    @staticmethod
    def intersection(l1, l2):
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

        if point_x_segment < point_x_parent:
            direction = constants.UP
        elif point_x_segment > point_x_parent:
            direction = constants.DOWN
        else:
            direction = constants.INTERSECTS
        return direction

    @staticmethod
    def get_direction_relative_to_point(y_prime, y_segment):
        if y_prime < y_segment:
            return constants.UP
        elif y_prime > y_segment:
            return constants.DOWN
        else:
            return constants.INTERSECTS

    @staticmethod
    def get_segment_position_relative_to_points(first_point_position, second_point_position):
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
