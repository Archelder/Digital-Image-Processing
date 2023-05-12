import cv2
import matplotlib.pyplot as plt

#open
original_image=cv2.imread("../images/FigP0501.png",flags=0)
size=(3,3)

target_image=cv2.blur(original_image,size)

fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))

ax = axs[0, 0]
ax.imshow(target_image, cmap='gray')
ax.set_title(f"3*3")
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()

plt.show()