from systems.ContinuousSystem3dRossler import ContinuousSystem3dRossler
from iMath.Subdivision import Subdivision
from iPlot.iPlot import iPlot

system = ContinuousSystem3dRossler()
num_subdivision_step = 9

attractor = Subdivision.do_subdivision(system, system.borders, num_subdivision_step, 10)
x_attractor = attractor.get_points()

i_plt = iPlot(system.dimension)
i_plt.add_points(x_attractor, 'ro', 0.2)
i_plt.show()
