import numpy as np
import matplotlib.pyplot as plt
import math

plt.axis([-3, 3, -3, 3])
v = np.array([0, 2.5, -2.5, 0, 0, -2.5, 2.5, 0])

plt.plot([0, v[0]], [0, v[1]])
plt.plot([0, v[2]], [0, v[3]])
plt.plot([0, v[4]], [0, v[5]])
plt.plot([0, v[6]], [0, v[7]])
plt.plot([0, 2.5], [0, 2])
plt.plot([0, -2.5], [0, 2])
plt.plot([0, -2.5], [0, -2])
plt.plot([0, 2.5], [0, -2])

hyp = math.sqrt(2.5**2 + 2**2)
print(hyp)

plt.show()


