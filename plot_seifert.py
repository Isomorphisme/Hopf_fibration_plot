import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def color_grad(debut, fin, steps, current):
	c = float(current)/steps
	return ((fin[0]*c + (1-c)*debut[0])/255., (fin[1]*c + (1-c)*debut[1])/255., (fin[2]*c + (1-c)*debut[2])/255.)


fig = plt.figure()
ax = fig.gca(projection='3d')

i = 0
for phi in np.linspace(0, np.pi * 0.5, 70):
	theta = np.linspace(0, 2*np.pi, 200)

	bigfactor = 1 / (np.sqrt(2) - np.cos(theta+phi))

	x = bigfactor * np.sin(theta+phi)
	y = bigfactor * np.cos(theta)
	z = bigfactor * np.sin(theta)

	if i%69 == 0:
		ax.plot(x, y, z, color="red", linewidth=3)
	else :
		ax.plot(x, y, z, color=color_grad((59,255,170),(99,83,128),70,i))
	i += 1

plt.axis('off')
plt.show()
