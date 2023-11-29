import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy


def Custom_plot(t,inz):
    x = t
    y = np.cos(t)
    z = np.zeros_like(t)
    v=10
    x2 = t
    y2 = np.zeros_like(t)
    z2 = np.cos(t)

    x3 = copy.deepcopy(t)
    distance = (np.cos(x3)+1)/121*3*np.pi
    #print(sum(distance))
    for i,x3i in enumerate(x3):
        if i==len(x3)-1:break
        x3[i+1]=x3[i]+distance[i]

    y3 = np.zeros_like(x3)
    z3 = np.zeros_like(x3)




    # Create a figure with three subplots side by side
    fig, axs = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})
    fig.suptitle("Acoustic Phonon Modes")

    # Plot the sine wave in the first subplot
    axs[0].plot(x, y, z, color="orange",label='Sine Wave')
    axs[0].scatter(x[::v], y[::v], z[::v], color='red', label='Points on the Line')
    axs[0].set_title('longitudinal mode 1')

    for xi, yi, zi in zip(x[::v], y[::v], z[::v]):
        z_plane = np.linspace(zi - 1, zi + 1, 10)
        y_plane = np.linspace(yi , yi - 1, 10)
        Z_plane, Y_plane = np.meshgrid(z_plane, y_plane)
        X_plane = np.zeros_like(Z_plane) + xi
        axs[0].plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color='blue')



    axs[1].plot(x2, y2, z2, color="orange", label='Sine Wave')
    axs[1].scatter(x2[::v], y2[::v], z2[::v], color='red', label='Points on the Line')
    axs[1].set_title('longitudinal mode 2')

    for xi, yi, zi in zip(x2[::v], y2[::v], z2[::v]):
        z_plane = np.linspace(zi -1, zi + 1, 100)
        y_plane = np.linspace(yi , yi - 1, 100)
        Z_plane, Y_plane = np.meshgrid(z_plane, y_plane)
        X_plane = np.zeros_like(Y_plane) + xi
        axs[1].plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color='blue')



    axs[2].scatter(x3[::v], y3[::v], z3[::v], color='red', label='Points on the Line')
    axs[2].set_title('transversal mode')

    for xi, yi, zi in zip(x3[::v], y3[::v], z3[::v]):
        z_plane = np.linspace(-1, + 1, 100)
        y_plane = np.linspace(-1, + 1, 100)
        Z_plane, Y_plane = np.meshgrid(z_plane, y_plane)
        X_plane = np.zeros_like(Y_plane) + xi
        axs[2].plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color='blue')

    # Set the default camera angle
    for ax in axs:
        ax.view_init(elev=20, azim=120)
        ax.set_xticks([])  # Remove x-axis ticks
        ax.set_yticks([])  # Remove y-axis ticks
        ax.set_zticks([]) 
        #ax.set_xlabel('X-axis')
        #ax.set_ylabel('Y-axis')
        #ax.set_zlabel('Z-axis')
        ax.grid(True)

    axs[2].view_init(elev=20, azim=100)
    # Adjust layout
    #plt.tight_layout()
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    # Show the plot
    plt.savefig("gif/phonons"+str(inz)+".png")
    plt.close()
    #plt.show()






if __name__ == '__main__':
    for i in range(99,200):
        inc=i*np.pi/100
        print(inc)
        t = np.linspace(inc, 3 * np.pi+inc, 121)
        Custom_plot(t,i)