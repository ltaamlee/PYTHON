from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

# -0.3*x**2 - 0.3*y**2 + z**2 = 1
x=np.linspace(-5,5,400)
y=np.linspace(-5,5,400)

X,Y = np.meshgrid(x,y)

z_neg=-np.sqrt(1 + 0.3*X**2 + 0.3*Y**2)
z_pos=np.sqrt(1 + 0.3*X**2 + 0.3*Y**2)

ax=plt.axes(projection='3d')
normal=Normalize(vmin=-5, vmax=5)

surf1=ax.plot_surface(X, Y, z_neg, cmap='jet', norm=normal)
surf2=ax.plot_surface(X, Y, z_pos, cmap='jet', norm=normal)

plt.colorbar(surf1, ax=ax, shrink=0.5, aspect=20, pad=0.1)

ax.set_title("Hyperboloid")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")

plt.show()