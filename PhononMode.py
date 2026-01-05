import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ---------------- Parameters ----------------

N = 121
stride = 10
t_base_acoustic = np.linspace(0, 3 * np.pi, N)
t_base_optical  = np.linspace(0, 12 * np.pi, N)

omega_acoustic = 1.0
omega_optical = 1.5
A_long_acoustic = 0.3
A_long_optical = 0.3*4


# ---------------- Physics helpers ----------------

def longitudinal_positions_acoustic(t):
    distance = (np.cos(t) + 1) / N * 3 * np.pi
    x = t.copy()
    x[1:] = np.cumsum(distance[:-1]) + x[0]
    return x

def longitudinal_positions_optical(t):
    distance = (np.cos(t) + 1) / N * 12 * np.pi
    x = t.copy()
    x[1:] = np.cumsum(distance[:-1]) + x[0]
    return x

# ---------------- Plot helpers ----------------

def draw_plane(ax, x0, y0, z0, size=1.0, n=15, alpha=0.3):
    y = np.linspace(y0, y0 - size, n)
    z = np.linspace(z0 - size, z0 + size, n)
    Y, Z = np.meshgrid(y, z)
    X = np.full_like(Y, x0)
    ax.plot_surface(X, Y, Z, color="blue", alpha=alpha)


def style_axis(ax, azim=120):
    ax.view_init(elev=20, azim=azim)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(True)

# ---------------- Animation factory ----------------

def make_animation(mode, omega, filename, frames=100):

    fig, axs = plt.subplots(
        1, 3, figsize=(18, 6), subplot_kw={"projection": "3d"}
    )

    titles = [
        "Transversal mode 1",
        "Transversal mode 2",
        "Longitudinal mode",
    ]



    fig.suptitle(f"{mode.capitalize()} phonon", fontsize=20)

    def update(frame):
        phase = omega * frame * 0.08
        t_base = t_base_acoustic if mode == "acoustic" else t_base_optical
        t = t_base + phase

        for ax in axs:
            ax.cla()
        for ax, title in zip(axs, titles):
            ax.set_title(title, fontsize=16)
        for ax in axs:
            ax.set_xlim(phase, t_base[-1]+phase)
            ax.set_ylim(-1.5, 1.5)
            ax.set_zlim(-1.5, 1.5)

        # ---------- Transversal 1 ----------
        x = t
        y = np.cos(t)
        z = np.zeros_like(t)

        axs[0].plot(x, y, z, color="orange")
        axs[0].scatter(x[::stride], y[::stride], z[::stride], color="red")

        for i in range(0, N, stride):
            draw_plane(axs[0], x[i], y[i], z[i])

        # ---------- Transversal 2 ----------
        x2 = t
        y2 = np.zeros_like(t)
        z2 = np.cos(t)

        axs[1].plot(x2, y2, z2, color="orange")
        axs[1].scatter(x2[::stride], y2[::stride], z2[::stride], color="red")

        for i in range(0, N, stride):
            draw_plane(axs[1], x2[i], y2[i], z2[i])

        # ---------- Longitudinal ----------
        if mode == "acoustic":
            longitudinal_positions = longitudinal_positions_acoustic
        else:
            longitudinal_positions = longitudinal_positions_optical
        x3 = longitudinal_positions(t)
        A_long = A_long_acoustic if mode == "acoustic" else A_long_optical
        x3 = x3 + A_long * np.cos(t)

        y3 = np.zeros_like(x3)
        z3 = np.zeros_like(x3)

        axs[2].scatter(x3[::stride], y3[::stride], z3[::stride], color="red")

        for i in range(0, N, stride):
            draw_plane(axs[2], x3[i], y3[i], z3[i])

        style_axis(axs[0])
        style_axis(axs[1])
        style_axis(axs[2], azim=100)

    anim = FuncAnimation(fig, update, frames=frames, interval=60)

    anim.save(
        filename,
        writer=PillowWriter(fps=20)
    )

    plt.close(fig)

# ---------------- Run both ----------------

make_animation(
    mode="acoustic",
    omega=omega_acoustic,
    filename="phonon_acoustic.gif"
)

make_animation(
    mode="optical",
    omega=omega_optical,
    filename="phonon_optical.gif"
)


