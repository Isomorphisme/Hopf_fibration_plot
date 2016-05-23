import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def color_grad(debut, fin, steps, current):
	c = float(current)/steps
	return ((fin[0]*c + (1-c)*debut[0])/255., (fin[1]*c + (1-c)*debut[1])/255., (fin[2]*c + (1-c)*debut[2])/255.)


gradients = [[(255,223,163),(90,128,79)], [(255,145,143),(32,43,128)], [(168,255,233),(111,128,69)], [(151,255,5),(128,0,0)], [(255,212,18),(128,95,5)], [(25,182,255),(128,87,112,1)]]
steps_list = [80,70,60,50,40,30]
#phirange_list = [(np.pi*0.5, 1.5*np.pi), (0.2*np.pi, 1.8*np.pi)]
phirange_list = [(0, np.pi*2)]*len(steps_list)

fig = plt.figure()
ax = fig.gca(projection='3d')

j = 0
for r in np.linspace(0,1,6):
	i = 0
	cstep = steps_list[j]
	phimin = phirange_list[j][0]
	phimax = phirange_list[j][1]
	for phi in np.linspace(phimin, phimax, cstep):

		theta = np.linspace(0, 2*np.pi, 800)

		bigfactor = 1/(1+(np.sqrt((1+np.sqrt(1-r**2))/2))*np.cos(theta))

		x = bigfactor * np.sqrt((1+np.sqrt(1-r**2))/2) * np.sin(theta)
		y = bigfactor * r/(np.sqrt(2)*np.sqrt(1+np.sqrt(1-r**2))) * np.cos(theta-phi)
		z = bigfactor * r/(np.sqrt(2)*np.sqrt(1+np.sqrt(1-r**2))) * np.sin(theta-phi)

		colour = color_grad(gradients[j][0], gradients[j][1], cstep, i)

		ax.plot(x, y, z, color=colour, linewidth=1.5)
		i +=1
	j += 1

plt.axis('off')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()