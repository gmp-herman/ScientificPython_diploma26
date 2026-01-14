
import numpy as np
import matplotlib.pyplot as plt

field=np.genfromtxt("gun.txt").transpose()
plt.axis([0, 10, 0, 1])

def run(field):
    neighbors = (np.roll(field, 1, 0) + np.roll(field, 1, 1) + np.roll(field, -1, 0) + np.roll(field, -1, 1) + np.roll(np.roll(field, 1, 0), 1, 1) + np.roll(np.roll(field, 1, 0), -1, 1) + np.roll(np.roll(field, -1, 0), 1, 1) + np.roll(np.roll(field, -1, 0), -1, 1))

    new_field = np.zeros_like(field)
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if neighbors[i, j] == 3:
                new_field[i, j] = 1
            elif field[i, j] == 1 and neighbors[i, j] == 2:
                new_field[i, j] = 1
            else:
                new_field[i, j] = 0
                
    return new_field


plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(field, cmap="binary")
ax.axis("off")


for _ in range(500):
    field = run(field)
    img.set_data(field)
    plt.pause(0.1)

plt.ioff()
plt.show()
