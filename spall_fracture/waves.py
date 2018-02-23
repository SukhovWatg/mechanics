from numpy import heaviside as H
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# def params
A = 6
T_1 = 0.5
T_2 = 1
T_0 = -T_1 - T_2
L = 5

fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-10, 10))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    t = np.linspace(0, 5, 1000)

    # arg right wave
    arg_rw = t - T_0 - 0.01 * i

    # arg left wave
    arg_lw = t - 2 * L + 0.01 * i

    y = -(A / T_1 * arg_rw * (H(arg_rw, 0) - H(arg_rw - T_1, 0)) + (-A / T_2 * arg_rw + A + A * T_1 / T_2) * (H(arg_rw - T_1, 0) - H(arg_rw - T_1 - T_2, 0))) + \
        (A / T_1 * arg_lw * (H(arg_lw, 0) - H(arg_lw - T_1, 0)) + (-A / T_2 *
                                                                   arg_lw + A + A * T_1 / T_2) * (H(arg_lw - T_1, 0) - H(arg_lw - T_1 - T_2, 0)))
    line.set_data(t, y)
    return line,


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=700, interval=10, blit=True)
# anim.save('basic_animation.mp4', fps=50, dpi=200,
#           extra_args=['-vcodec', 'libx264'])
plt.show()
