from systems.BaseSystem import BaseSystem
from systems.System2dHenon import System2dHenon
from systems.System1dSimple import System1dSimple
from systems.System2dBall import System2dBall
from systems.System3dChaoticSaddle import System3dChaoticSaddle
from iMath.PointsGenerator import generate_points
from iMath.JungeKevrekidis import JungeKevrekidis
from iMath.Subdivision import Subdivision
from iPlot.iPlot import iPlot

#system = BaseSystem(0.5)
#system = System2dHenon()
#system = System1dSimple(0.8)
#system = System2dBall()
system = System3dChaoticSaddle()

attractor = Subdivision.do_subdivision(system, system.borders, 9)
x_attractor = attractor.get_points()

num_points = 1000
points = generate_points(num_points, system.borders)
final_points = JungeKevrekidis(system, points, 1000)

x_jk = [[] for i in range(system.dimension)]
for i in range(len(final_points)):
    for j in range(system.dimension):
        x_jk[j].append(final_points[i][j])

i_plt = iPlot(system.dimension)
i_plt.add_points(x_attractor, 'ro', 0.1)
i_plt.add_points(x_jk, 'bo', 2.0)
i_plt.show()

