from systems.BaseSystem import BaseSystem
from systems.System2dHenon import System2dHenon
from systems.System1dSimple import System1dSimple
from systems.System2dBall import System2dBall
from systems.System3dChaoticSaddle import System3dChaoticSaddle
from iMath.PointsGenerator import generate_points
from iMath.JungeKevrekidis import JungeKevrekidis
from iMath.Subdivision import Subdivision
from iPlot.iPlot import iPlot

print("0 - One point")
print("1 - One line")
print("2 - Circle")
print("3 - Henon")
print("4 - Chaotic saddle")

which = int(input("Desired system to run: "))

if which == 0:
    system = BaseSystem(0.5)
elif which == 1:
    system = System1dSimple(0.8)
elif which == 2:
    system = System2dBall()
elif which == 3:
    system = System2dHenon()
elif which == 4:
    system = System3dChaoticSaddle()

num_subdivision_step = input("Number of subdivision steps ({0}):".format(system.num_sub_steps))
if len(num_subdivision_step) == 0:
    num_subdivision_step = system.num_sub_steps
else:
    num_subdivision_step = int(num_subdivision_step)
num_jk_points = input("Number of points for JK ({0}):".format(system.num_jk_points))
if len(num_jk_points) == 0:
    num_jk_points = system.num_jk_points
else:
    num_jk_points = int(num_jk_points)
num_jk_steps = input("Number of JK steps ({0}):".format(system.num_jk_steps))
if len(num_jk_steps) == 0:
    num_jk_steps = system.num_jk_steps
else:
    num_jk_steps = int(num_jk_steps)

attractor = Subdivision.do_subdivision(system, system.borders, num_subdivision_step, 10)
x_attractor = attractor.get_points()

points = generate_points(num_jk_points, system.borders)
jk = JungeKevrekidis(system)
final_points = jk.go(points, num_jk_steps)

x_jk = [[] for i in range(system.dimension)]
for i in range(len(final_points)):
    for j in range(system.dimension):
        x_jk[j].append(final_points[i][j])

i_plt = iPlot(system.dimension)
i_plt.add_points(x_attractor, 'ro', 0.1)
i_plt.add_points(x_jk, 'bo', 2.0)
i_plt.show()

