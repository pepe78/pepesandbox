import sys

from iMath.Search.BaseSearch import BaseSearch


class Box:
    corners = None
    borders = None
    already_processed_index = None
    active_points = None
    neighbours = None
    max_dist_all = sys.float_info.max
    allow_minor_numerical_inaccuracy = 1.0001

    def __init__(self):
        self.already_processed_index = {}
        self.active_points = []

    def set(self, corners, neighbours, borders):
        self.corners = corners
        self.neighbours = neighbours
        self.borders = borders

    def insert_point(self, point, point_index, list_to_process):
        self.already_processed_index[point_index] = True
        min_dist = self.get_min_dist(point)
        max_dist = self.get_max_dist(point)
        if (len(self.active_points) == 0) or \
                (min_dist <= self.max_dist_all * self.allow_minor_numerical_inaccuracy):
            if self.max_dist_all > max_dist:
                self.max_dist_all = max_dist
            where = Box.find_position(min_dist, self.active_points, 0, len(self.active_points))
            self.active_points.insert(where, [point_index, min_dist, max_dist])
            if where == 0:
                upto = Box.find_position(
                    self.max_dist_all * self.allow_minor_numerical_inaccuracy,
                    self.active_points,
                    0,
                    len(self.active_points))
                self.active_points = self.active_points[0:upto]
            for neighbour in self.neighbours:
                if point_index not in neighbour.already_processed_index:
                    list_to_process.append([point_index, neighbour])

    def get_max_dist(self, point):
        max_dist = -sys.float_info.max
        for i in range(len(self.corners)):
            tmp_max = BaseSearch.get_distance(point, self.corners[i])
            if tmp_max > max_dist:
                max_dist = tmp_max
        return max_dist

    def get_min_dist(self, point):
        min_dist = 0
        for i in range(len(self.borders)):
            if point[i] < self.borders[i][0]:
                qq = self.borders[i][0] - point[i]
                min_dist += qq * qq
            else:
                if point[i] > self.borders[i][1]:
                    qq = self.borders[i][1] - point[i]
                    min_dist += qq * qq
        return min_dist

    @staticmethod
    def find_position(val, active_points, s_pos, e_pos):
        if s_pos == e_pos:
            return s_pos
        m_pos = (s_pos + e_pos) // 2
        if m_pos == s_pos:
            if val < active_points[m_pos][1]:
                return m_pos
            return m_pos + 1
        if val < active_points[m_pos][1]:
            return Box.find_position(val, active_points, s_pos, m_pos)
        return Box.find_position(val, active_points, m_pos, e_pos)
