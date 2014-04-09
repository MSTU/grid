import numpy as np
from scipy.optimize import fmin, basinhopping


# objective function
def f(vector):
	x = vector[0]
	y = vector[1]
	return (1-(x**2+y**3))*np.exp(-(x**2+y**2)/2)

x0 = 0
y0 = 1
np.random.seed(2112)
global_result = basinhopping(f, np.array([x0, y0]))
result = fmin(f, global_result['x'])
print result

# plot the function
x = np.arange(-3,3,0.1)
y = np.arange(-3,3,0.1)
XY = np.meshgrid(x, y)
Z = f(XY)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XY[0], XY[1], Z, rstride=1, cstride=1,
					   cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()