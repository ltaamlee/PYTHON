import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-3*np.pi,0,300)
y1=1.5 * np.sin(x1)
plt.plot(x1,y1,'r--',label='y = 1.5sin(x) with x in [-3pi; 0]',linewidth=2)

theta=np.linspace(0,2*np.pi,500)
r=2 + np.cos(10*theta)+2*np.sin(5*theta)
plt.plot(r*np.cos(theta), r*np.sin(theta),'g-',label='r = 2 + cos(10theta) + 2sin(5theta)',linewidth=2)

x2=np.linspace(0,3*np.pi,300)
y2=1.5*np.sin(x2)
plt.plot(x2,y2,'b--',label='y = 1.5sin(x) with x in [0; 3pi]',linewidth=2)

plt.legend(loc='upper right')
plt.xticks(np.arange(-10,11,2.5)) 
plt.yticks(range(-6, 7, 2))
plt.grid()

plt.show()
