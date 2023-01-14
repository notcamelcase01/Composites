import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import animation

def plot_grid(x,y, ax=None,li=1, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x,y), axis=2)
    segs2 = segs1.transpose(1,0,2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.set_xlim([-li,li])
    ax.set_ylim([-li,li])

f = lambda x,y,t: (x+t*0.25*(18+6*y),y+t*0.25*(14+2*y))

fig, ax = plt.subplots()
grid_x,grid_y = np.meshgrid(np.linspace(-10,10,20),np.linspace(-10,10,20))
plot_grid(grid_x,grid_y, ax=ax,  color="lightgrey")

def update(i):
    ax.clear()
    print(i)
    distx, disty = f(grid_x,grid_y,i)
    plot_grid(grid_x, grid_y, ax=ax, color="lightgrey")
    plot_grid(distx, disty, ax=ax,li = 6, color="C0")

update(0) #plot the original data

anipath = np.arange(0,.1,.0005,dtype = float)
ani = animation.FuncAnimation(fig, update, frames=anipath, interval = 1,repeat = False)

FFwriter = animation.FFMpegWriter(fps=60)
ani.save('animation.mp4', writer=FFwriter)
