import time
import matplotlib.pyplot as plt

from iMath.PointsGenerator import generate_points
from iMath.Search.BaseSearch import BaseSearch
from iMath.Search.SpreadBoxSearch.SpreadBoxSearch import SpreadBoxSearch
from iMath.Search.SearchUsingAllAlgs import SearchUsingAllAlgs

points1 = generate_points(1000, 2)
points2 = generate_points(1000, 2)
ret = SearchUsingAllAlgs.get_best_indexes(points1, points2)
print(SearchUsingAllAlgs.bs_wins, SearchUsingAllAlgs.sbs_wins)

np = [i for i in range(100,6001,200)]
rt1 = [0 for i in range(len(np))]
rt2 = [0 for i in range(len(np))]
for i in range(len(np)):
    for repeat in range(10):
        print("Doing {0} {1}".format(np[i], repeat))
        points1 = generate_points(np[i], 2)
        points2 = generate_points(np[i], 2)

        t0 = time.time()

        bs = BaseSearch(points1)
        r1 = bs.get_closest_points(points2)

        t1 = time.time()

        sbs = SpreadBoxSearch(points1, points2)
        r2 = sbs.get_closest_points(points2)

        t2 = time.time()

        rt1[i] += (t1-t0)/10.0
        rt2[i] += (t2-t1)/10.0

        for j in range(len(r1)):
            assert r1[j] == r2[j]

plt.plot(np, rt1, 'b')
plt.plot(np, rt2, 'g')
plt.show()

plt.plot(np, rt2)
plt.show()
