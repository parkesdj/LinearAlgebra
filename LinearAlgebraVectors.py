import numpy as np
import matplotlib.pyplot as plt

plt.axis([-3, 3, -3, 3])
v = np.array([0, 2.5, -2.5, 0, 0, -2.5, 2.5, 0])
x = [0, 0, 0, 0]
y = [2.5, 0, -2.5, 0]


plt.plot([0, v[0]], [0, v[1]])
plt.plot([0, v[2]], [0, v[3]])
plt.plot([0, v[4]], [0, v[5]])
plt.plot([0, v[6]], [0, v[7]])

plt.plot(x, y)

plt.show()
