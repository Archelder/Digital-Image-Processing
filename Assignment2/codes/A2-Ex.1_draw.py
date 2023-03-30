import numpy as np
import matplotlib.pyplot as plt


def contrast_stretch(slope: int, L: int = 256):
    """
    :param slope: E, control the slope of the function as it transitions from low to high intensity values
    :param L: the number of intensity levels
    :return: s
    """
    m = L / 4
    E = slope
    r = np.linspace(start=0, stop=L, num=1000)
    s = 1 / (1 + np.power((m / r), E))
    return s


ls_E = [0, 5, 10, 20, 50, 100]
s = []
for i in ls_E:
    s.append(contrast_stretch(i))

for i in range(len(ls_E)):
    plt.plot(s[i], label=f'E={ls_E[i]}')

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.ylim(0, 1.01)
plt.xlim(0, 500)
plt.legend(loc='best', frameon=True)
plt.title('Figure: a family of transformations as a function of E\n'
          r'$ s = \frac{1}{1 + (\dfrac{m}{r})^E} $')
plt.savefig('../images/ansfig_A2-Ex.1(b).png')
plt.show()
