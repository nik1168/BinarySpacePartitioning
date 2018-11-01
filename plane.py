class Plane:

    def __init__(self):
        self.line_segments = []

    def add_segment(self, line_segment):
        self.line_segments.append(line_segment)

    def print_segments(self):
        for line_segment in self.line_segments:
            print(line_segment.display())

    def get_line_segments(self):
        return self.line_segments
