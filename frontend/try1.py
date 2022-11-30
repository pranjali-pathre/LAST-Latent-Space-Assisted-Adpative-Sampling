import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
import pickle
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


data_all = []
for nn in range(0, 4):
    file_name ='/home/pranjali/Documents/2022-Monsoon/DataDrivenDrugDiscovery/Project2/LAST/LAST/results/results/1ake_r' + str(nn) + '_latents.pkl'
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
    data = np.array(data)
    print(data.shape)
    data_all.append(data)

fig, ax = plt.subplots()
marker_size = 10

def animate(i):
    fig.clear()
    ax = fig.add_subplot(111)
    s = ax.scatter(data_all[i][:, 0], data_all[i][:, 1], s=marker_size)

plt.grid(b=None)
ani = animation.FuncAnimation(fig, animate, interval=1000, frames=range(4))

ani.save('animation.gif', writer='pillow')