import sys
import time

from iMath.SpreadBoxSearch.SpreadBoxSearch import SpreadBoxSearch


class BaseSystem:
    param = 1
    dimension = 1

# for other systems, implement only these methods
# -----------------------------------------------
    def __init__(self, param):
        self.param = param
        self.dimension = 1
        return

    def map_point(self, x):
        return [self.param * x[0]]

    def get_partial(self, x):
        return [[self.param]]
# -----------------------------------------------

    def map_points(self, x):
        ret = [[] for i in range(len(x))]
        for i in range(len(x)):
            ret[i] = self.map_point(x[i])

        return ret

    def get_partials(self, x):
        ret = [[] for i in range(len(x))]
        for i in range(len(x)):
            ret[i] = self.get_partial(x[i])

        return ret

    def get_dimension(self):
        return self.dimension

    def evaluate(self, x):
        ret = 0.0
        num_points = len(x)
        fx = self.map_points(x)

        #m0 = time.time()
        #sbs_fx = SpreadBoxSearch(fx, x)
        #for i in range(num_points):
        #    #which = BaseSystem.closest_point(x[i], fx)
        #    which = sbs_fx.get_closest_point(x[i])
        #    #assert which == which2
        #    for j in range(self.dimension):
        #        dif = x[i][j] - fx[which][j]
        #        ret += dif * dif
        #m1 = time.time()
        #sbs_fx = SpreadBoxSearch(fx, x)
        for i in range(num_points):
            which = BaseSystem.closest_point(x[i], fx)
            for j in range(self.dimension):
                dif = x[i][j] - fx[which][j]
                ret += dif * dif
        #m2 = time.time()

        for i in range(num_points):
            which = BaseSystem.closest_point(fx[i], x)
            for j in range(self.dimension):
                dif = x[which][j] - fx[i][j]
                ret += dif * dif

        return ret

    def get_derivatives(self, x):
        num_points = len(x)
        ret = [[] for i in range(len(x))]
        for i in range(num_points):
            ret[i] = [0 for j in range(self.dimension)]

        fx = self.map_points(x)
        dx = self.get_partials(x)

        for i in range(num_points):
            which = BaseSystem.closest_point(x[i], fx)
            for j in range(self.dimension):
                dif = x[i][j] - fx[which][j]
                ret[i][j] += dif * 2.0
                for k in range(self.dimension):
                    ret[which][k] -= dif * dx[which][j][k] * 2.0

        for i in range(num_points):
            which = BaseSystem.closest_point(fx[i], x)
            for j in range(self.dimension):
                dif = x[which][j] - fx[i][j]
                ret[which][j] += dif * 2.0
                for k in range(self.dimension):
                    ret[i][k] -= dif * dx[i][j][k] * 2.0

        return ret

    def move(self, x, dx, step):
        num_points = len(x)
        ret = [[] for i in range(num_points)]
        for i in range(num_points):
            ret[i] = [x[i][j] for j in range(self.dimension)]
        for i in range(num_points):
            for j in range(self.dimension):
                ret[i][j] -= step * dx[i][j]

        return ret

    @staticmethod
    def closest_point(p, pv):
        which = -1
        min_dist = sys.float_info.max
        for i in range(len(pv)):
            tmp = BaseSystem.get_distance(p, pv[i])
            if tmp < min_dist:
                min_dist = tmp
                which = i

        return which

    @staticmethod
    def get_distance(p1, p2):
        ret = 0.0
        for i in range(len(p1)):
            tmp = p1[i] - p2[i]
            ret += tmp * tmp

        return ret
