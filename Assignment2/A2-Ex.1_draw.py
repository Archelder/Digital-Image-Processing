import numpy as np
import matplotlib.pyplot as plt


def contrast_stretch(k, intensity_levels,):
    r = np.linspace(0, L)



k = 100


E = 10
r = np.linspace(0, 255, 1000, endpoint=True)
s = 1 / (1 + np.power((k / r), E))

plt.plot(s)
plt.ylim(0, 1)

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.show()
