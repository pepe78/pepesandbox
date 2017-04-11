import sys


class Box:
    corners = None
    borders = None
    already_processed_index = None
    active_points = None
    neighbours = None
    max_dist_all = sys.float_info.max

    def __init__(self):
        self.already_processed_index = {}
        self.active_points = []

    def set(self, corners, neighbours, borders):
        self.corners = corners
        self.neighbours = neighbours
        self.borders = borders

    def insert_point(self, point, point_index, force=True):
        if force:
            if point_index in self.already_processed_index:
                return
        self.already_processed_index[point_index] = True

        min_dist = 0
        for i in range(len(self.borders)):
            if point[i] < self.borders[i][0]:
                qq = self.borders[i][0]-point[i]
                min_dist += qq * qq
            else:
                if point[i] > self.borders[i][1]:
                    qq = self.borders[i][1] - point[i]
                    min_dist += qq * qq

        max_dist = -sys.float_info.max
        for i in range(len(self.corners)):
            tmp_max = Box.get_distance(point, self.corners[i])
            if tmp_max > max_dist:
                max_dist = tmp_max

        if (len(self.active_points) == 0) or (min_dist <= self.max_dist_all * 1.01):
            if self.max_dist_all > max_dist:
                self.max_dist_all = max_dist
            where = 0
            while where < len(self.active_points):
                if min_dist < self.active_points[where][1]:
                    break
                where += 1
            self.active_points.insert(where, [point_index, min_dist, max_dist])
            if where == 0:
                for i in range(1, len(self.active_points)):
                    if self.active_points[i][1] > self.max_dist_all * 1.01:
                        self.active_points = self.active_points[0:i]
                        break
            for neighbour in self.neighbours:
                neighbour.insert_point(point, point_index)

    @staticmethod
    def get_distance(p1, p2):
        ret = 0.0
        for i in range(len(p1)):
            tmp = p1[i] - p2[i]
            ret += tmp * tmp

        return ret