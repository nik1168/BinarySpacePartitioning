from line_segment import LineSegment


class SegmentMapper:
    def __init__(self):
        pass

    @staticmethod
    def map_file_to_tasks(file):
        """
        Read file and map to line segments list
        :return: array of line segment
        """
        line_segments_list = []
        with open(file, 'r') as f:
            for line in f:
                elements = line.split(",")
                if len(elements) == 5:
                    line_segment = LineSegment(str(elements[0]), float(elements[1]), float(elements[2]),
                                               float(elements[3]),
                                               int(elements[4]))
                    line_segments_list.append(line_segment)
        return line_segments_list
