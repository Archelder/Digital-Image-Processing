import cv2
import matplotlib.pyplot as plt

# open
original_image = cv2.imread("../images/FigP0501.png", flags=0)
size1 = (3, 3)
size2 = (7, 7)
size3 = (9, 9)
size = [3, 7, 9]

target_image = []
target_image.append(cv2.blur(original_image, size1))
target_image.append(cv2.blur(original_image, size2))
target_image.append(cv2.blur(original_image, size3))

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

plt.suptitle("Running Results of Arithmetic Mean Filtering")

plt.tight_layout()

plt.show()
