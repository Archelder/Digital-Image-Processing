import cv2
import numpy as np
import matplotlib.pyplot as plt


def geometric_mean_filter(img, ksize):
    h, w = img.shape[:2]
    expo = 1 / (ksize * ksize)
    pad = int((ksize - 1) / 2)
    # pad the image using `cv2.copyMakeBorder()` whose effect can also be produced by`np.pad()`
    padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, borderType=cv2.BORDER_REFLECT_101)
    filtered = np.zeros(img.shape)
    for i in range(pad, pad + h):
        for j in range(pad, pad + w):
            prod = np.prod(padded[i - pad:i + pad, j - pad:j + pad])
            filtered[i - pad][j - pad] = np.power(prod, expo)
    return filtered


def GMF(img, ksize):
    return geometric_mean_filter(img, ksize)


kernel_size = [3, 7, 9]

# read the original image
original_image = cv2.imread("../images/FigP0501.png", flags=0)

filtered_img = []

# apply filters with different kernel sizes respectively
for ksize in kernel_size:
    filtered_img.append(GMF(original_image, ksize))

# display the results
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(10, 4))
ax = axs[0]
ax.imshow(original_image, cmap='gray'), ax.set_title(f"original image"), ax.set_xticks([]), ax.set_yticks([])
for i in range(3):
    ax = axs[i + 1]
    ax.imshow(filtered_img[i], 'gray')
    ax.set_title(fr"${kernel_size[i]}\times${kernel_size[i]} GMF")
    ax.set_xticks([]), ax.set_yticks([])

plt.suptitle("Running Results of Geometric Mean Filtering")

plt.tight_layout()

plt.show()
