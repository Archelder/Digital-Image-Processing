import cv2
import matplotlib.pyplot as plt
import numpy as np

# open
original_image = cv2.imread("../images/FigP0501.png", flags=0)
image_height = original_image.shape[0]
image_width = original_image.shape[1]


def Geometric(m):
    height = int((m - 1) / 2)
    width = int((m - 1) / 2)
    pad = np.pad(original_image.copy(), ((height, m - height - 1), (width, m - width - 1)), mode="edge")
    target = original_image.copy()
    for i in range(height, image_height + height):
        for j in range(width, image_width + width):
            s = np.prod(pad[i - height:i + height + 1, j - width:j + width + 1])
            target[i - height][j - width] = pow(s, 1 / (m * m))
    return target


size = [3, 7, 9]

target_image = []
for i in size:
    target_image.append(Geometric(i))

# show
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(10, 4))

ax = axs[0]
ax.imshow(original_image, cmap='gray')
ax.set_title(f"original image")
ax.set_xticks([])
ax.set_yticks([])

for i in range(3):
    ax = axs[i + 1]
    ax.imshow(target_image[i], cmap='gray')
    ax.set_title(fr"${size[i]}\times${size[i]}")
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Running Results of Geometric Mean Filtering")

plt.tight_layout()

plt.show()
