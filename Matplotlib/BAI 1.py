import numpy as np
import matplotlib.pyplot as plt

def polynomial(x):
    return 3*x**5 + 20*x**4 - 10*x**3 - 240*x**2 - 250*x + 200

x=np.linspace(-15, 15, 400)
y=polynomial(x)

plt.plot(x,y,'r-.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fifth Degree Polynomial')

plt.xlim(-6, 4)
plt.ylim(-1200, 400)
plt.show()
