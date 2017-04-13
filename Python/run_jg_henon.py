import matplotlib.pyplot as plt

from systems.System2dHenon import System2dHenon
from iMath.PointsGenerator import generate_points
from iMath.JungeKevrekidis import JungeKevrekidis
from iMath.Subdivision import Subdivision

system = System2dHenon()
borders = [[-1.5, 1.5], [-0.5, 0.5]]

attractor = Subdivision.do_subdivision(system, borders, 10)

num_points = 1000
points = generate_points(num_points, borders)
points = JungeKevrekidis(system, points, 1000)

attractor.plot()
x = []
y = []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])
plt.plot(x, y, 'bo', markersize=0.6)
plt.xlim(borders[0])
plt.ylim(borders[1])
plt.show()
