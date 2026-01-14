
import numpy as np
import matplotlib.pyplot as plt

field=np.genfromtxt("ships.txt").transpose()
plt.axis([0, 10, 0, 1])

def run(field):
    rows, cols = field.shape
    new_field = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):

            neighbors = 0

            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:

                    if k == 0 and l == 0:
                        continue 

                    ni = i + k
                    nj = j + l

                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbors += field[ni, nj]

            if neighbors == 3:
                new_field[i, j] = 1
            elif field[i, j] == 1 and neighbors == 2:
                new_field[i, j] = 1
            else:
                new_field[i, j] = 0

    return new_field

plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(field, cmap="binary")
ax.axis("off")

for _ in range(200):
    field = run(field)
    img.set_data(field)
    plt.pause(0.1)

plt.ioff()
plt.show()
