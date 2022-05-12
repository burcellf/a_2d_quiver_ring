

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


plt.rcParams["figure.figsize"] = [9.50, 9.50]
plt.rcParams["figure.autolayout"] = True


# Setting up quivers
ml = 3
x, y = np.mgrid[:2 * np.pi:(10j * ml), :2 * np.pi:(10j * ml)]
u = np.cos(x)
v = np.sin(y)


# defining waving motion
def animate(num, qr, qr1, qr2, x, y):
    
    # u, v, qr for each ring of quivers
    u = np.cos(x * y + num * 0.0251)
    u1 = np.cos(x * y + num * 0.08)
    u2 = np.cos(x * y + num * 0.04)
    
    v = np.sin(x * 3 + num * 0.1)
    v1 = np.sin(x ** 2 + num * 0.1)
    v2 = np.sin(x ** 5 + num * 0.05)
        
    qr.set_UVC(u, v)
    qr1.set_UVC(u1, v1)
    qr2.set_UVC(u2, v2)

    return qr, qr1, qr2


# Rotation
t = np.arange(0, (1000 * ml), (10 / ml))


""" uncomment any of the 5 animation shapes (x & y) to see them """

# ——————————————————————————————————————————————————————————————————————
# Circular arrangement
x = np.cos(t)
y = np.sin(t)

# Double twist (horizontal)
# x = np.cos(t)
# y = np.sin(t * ml)

# Double twist (vertical)
# x = np.cos(t * ml)
# y = np.sin(t)

# Eye
# x = np.cos(t * (ml - 0.0005))
# y = np.sin(t * ml)

# Loop
# x = np.cos(t * (ml - 0.0003))
# y = np.sin(t * (ml - 0.0001))
# ——————————————————————————————————————————————————————————————————————


# Plot
fig, ax = plt.subplots(1, 1, facecolor='black')


# 3 quiver rings and their qualities
qr = ax.quiver(x, y, u, v, headlength=3, headwidth=2, width=.003, color=(0.1, 0.6, 0.9), alpha=0.6)
qr1 = ax.quiver(x, y, u, v, headlength=3, headwidth=2, width=.003, color=(0.6, 0.1, 0.7), alpha=0.6)
qr2 = ax.quiver(x, y, u, v, headlength=3, headwidth=2, width=.003, color=(0.2, 0.6, 0.5), alpha=0.6)

# Axes
lim = 1.4
ax.set(xlim=(-lim, lim), xlabel='X', facecolor='k')
ax.set(ylim=(-lim, lim), ylabel='Yo', facecolor='k')

# Animation
line_ani = animation.FuncAnimation(fig, animate, frames=2000, fargs=(qr, qr1, qr2, x, y), interval=40, blit=False)
plt.show()

