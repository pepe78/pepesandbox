import sys

from iMath.LMBFGS import LMBFGS


# https://arxiv.org/abs/1610.04843
# Oliver Junge, Ioannis G. Kevrekidis
# On the sighting of unicorns: a variational approach to computing invariant sets in dynamical systems
def JungeKevrekidis(system, points, max_rounds=sys.int_info.max):
    epsilon = 1.0e-10
    num_points = len(points)
    lmbfgs = LMBFGS()
    evalu = system.evaluate(points)
    r = 0
    while True:
        points, step_size = lmbfgs.make_step(system, points)
        new_evalu = system.evaluate(points)
        print("{0} {1} {2} {3}".format(r, step_size, (evalu - new_evalu) / evalu, new_evalu / num_points))

        if (evalu - new_evalu) / evalu < epsilon or new_evalu / num_points < epsilon or r == max_rounds:
            break
        evalu = new_evalu
        r += 1

    return points
