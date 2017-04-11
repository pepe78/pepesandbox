import random


def generate_points(num_points,
                    dimension,
                    interval_min=-1.0,
                    interval_max=1.0):
    random.seed()

    ret = []
    for i in range(num_points):
        tmp = [interval_min + (interval_max - interval_min) * random.random()
               for j in range(dimension)]
        ret.append(tmp)

    return ret
