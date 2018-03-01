from numpy import heaviside as H
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# def params
A = -6
T_1 = 0.7
T_2 = 0.8
L = 5

fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-10, 10))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    t = np.linspace(0, 5, 1000)
    scale_parameter = 3
    # arg left -> right wave
    arg_lw = t - i * 0.01 - scale_parameter
    # arg right -> left wave
    arg_rw = t + i * 0.01 + scale_parameter
    y = (A / T_1 * (arg_lw) * (H(arg_lw, 0) - H(arg_lw - T_1, 0)) + A / (T_2 - T_1) * (
        T_2 - arg_lw) * (H(arg_lw - T_1, 0) - H(arg_lw - T_2, 0))) - (
        (A / (T_2 - T_1) * (arg_rw - 2 * L + T_2)) * (
            H(arg_rw - 2 * L + T_2, 0) - H(arg_rw - 2 * L + T_1, 0)) + (A / T_1 * (-(arg_rw) + 2 * L)) * (
            (H(arg_rw - 2 * L + T_1, 0)) - H(arg_rw - 2 * L, 0)))
    line.set_data(t, y)
    return line,


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=600, interval=40, blit=True)
# anim.save('basic_animation.mp4', fps=50, dpi=200,
#           extra_args=['-vcodec', 'libx264'])
plt.show()
