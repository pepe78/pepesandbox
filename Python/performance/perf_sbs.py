import time
import matplotlib.pyplot as plt

from iMath.PointsGenerator import generate_points
from iMath.Search.BaseSearch import BaseSearch
from iMath.Search.SpreadBoxSearch.SpreadBoxSearch import SpreadBoxSearch
# from iMath.Search.SearchUsingAllAlgs import SearchUsingAllAlgs

# points1 = generate_points(1000, 2)
# points2 = generate_points(1000, 2)
# ret = SearchUsingAllAlgs.get_best_indexes(points1, points2)
# print(SearchUsingAllAlgs.bs_wins, SearchUsingAllAlgs.sbs_wins)

dimension = 2
num_experiments = 10
np = [i for i in range(100,1201,200)]

# dimension = 3
# num_experiments = 1
# np = [27000]
# for 3-dimensional experiment - works even for higher dimension,
# but to see speed up - need to go to longer lists
# 950s for BS
# 220s for SBS

rt1 = [0 for i in range(len(np))]
rt2 = [0 for i in range(len(np))]
for i in range(len(np)):
    for repeat in range(num_experiments):
        print("Doing {0} {1}".format(np[i], repeat))
        points1 = generate_points(np[i], dimension)
        points2 = generate_points(np[i], dimension)

        t0 = time.time()

        bs = BaseSearch(points1)
        r1 = bs.get_closest_points(points2)

        t1 = time.time()

        sbs = SpreadBoxSearch(points1, points2)
        r2 = sbs.get_closest_points(points2)

        t2 = time.time()

        rt1[i] += (t1-t0)/num_experiments
        rt2[i] += (t2-t1)/num_experiments

        for j in range(len(r1)):
            assert r1[j] == r2[j]

print(np)
print(rt1)
print(rt2)
plt.plot(np, rt1, 'b')
plt.plot(np, rt2, 'g')
plt.show()

plt.plot(np, rt2)
plt.show()
