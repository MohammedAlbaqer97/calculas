import matplotlib.pyplot as plt
import numpy as np
#spicfide domin
n = 10
#number of vactores
k=20
#make mish grid
x,y = np.meshgrid(np.linspace(-n,n,k),np.linspace(-n,n,k))
R = np.sqrt((x)** 2 + (y) ** 2)
# T = np.arctan2(y,x)
a,b,m,n = 3,3,4,3
u,v = -2*y,2*x
plt.quiver(x,y,u,v,R)
plt.show()
