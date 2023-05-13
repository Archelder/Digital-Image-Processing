import cv2
import matplotlib.pyplot as plt
import numpy as np


def harmonic_mean_filter(img, ksize):
    h, w = img.shape[:2]
    order = ksize * ksize
    pad = int((ksize - 1) / 2)
    # pad the image using `np.pad()` whose effect can also be produced by`cv2.copyMakeBorder()`
    padded = np.pad(img, pad, 'symmetric')
    filtered = np.zeros(img.shape)
    for i in range(pad, pad + h):
        for j in range(pad, pad + w):
            s = np.sum(1 / (1e10 + padded[i - pad:i + pad, j - pad:j + pad]))
            filtered[i - pad][j - pad] = order / s
    return filtered


# read the original image
original_image = cv2.imread("../images/FigP0501.png", flags=0)
ksize = [3, 7, 9]

filtered_image = []
for size in ksize:
    filtered_image.append(harmonic_mean_filter(original_image, size))

# display the results# display the results
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(10, 4))

ax = axs[0]
ax.imshow(original_image, cmap='gray')
ax.set_title(f"original image")
ax.set_xticks([])
ax.set_yticks([])

for i in range(3):
    ax = axs[i + 1]
    ax.imshow(filtered_image[i], cmap='gray')
    ax.set_title(fr"${ksize[i]}\times${ksize[i]} HMF")
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Running Results of Harmonic Mean Filtering")

plt.tight_layout()

plt.show()
