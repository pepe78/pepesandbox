import matplotlib.pyplot as plt

from systems.System2dHenon import System2dHenon
from iMath.PointsGenerator import generate_points
from iMath.JG import JungeKevrekidis

system = System2dHenon()

num_points = 100
points = generate_points(num_points, system.get_dimension(), -2.0, 2.0)
points = JungeKevrekidis(system, points)

x = []
y = []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])
plt.plot(x, y, 'bo', markersize=0.3)
plt.show()

