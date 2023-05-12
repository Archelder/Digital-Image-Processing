import cv2
import matplotlib.pyplot as plt
import numpy as np

# open
original_image = cv2.imread("../images/FigP0501.png", flags=0)
size = [3, 7, 9]
type = []
for i in size:
    type.append(np.ones((i, i), np.float32) / (i * i))

target_image = []
for i in type:
    target_image.append(cv2.filter2D(original_image, -1, i))

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

plt.suptitle("Running Results of Harmonic Mean Filtering")

plt.tight_layout()

plt.show()
