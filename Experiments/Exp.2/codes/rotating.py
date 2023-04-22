import cv2
import matplotlib.pyplot as plt

original_img = cv2.imread("../images/Fig0236(a)(letter_T).tif")
img_h, img_w = original_img.shape[:2]
centre = (img_w / 2, img_h / 2)
rotation_matrix = cv2.getRotationMatrix2D(center=centre, angle=-30, scale=1)

interpolation = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC]
interpolation_text = ["nearest", "bilinear", "bicubic"]
rotated_img = []
for i in range(3):
    rotated_img.append(cv2.warpAffine(original_img, rotation_matrix, (img_w, img_h), flags=interpolation[i]))

fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(10, 4), num="Rotitated")
fig.suptitle("Rotated Results", fontsize=15)
axs[0].imshow(original_img, cmap='gray'), axs[0].axis('off'), axs[0].set_title(f"original")
for i in range(3):
    ax = axs.flat[i + 1]
    ax.imshow(rotated_img[i], cmap='gray')
    ax.axis('off')
    ax.set_title(f"{interpolation_text[i]}")

top = 280
bottom = top + 27
left = 160
right = left + 21
cropped_img = []
zoomed_img = []
for img in rotated_img:
    cropped_img.append(img[top:bottom, left:right])
for img in cropped_img:
    zoomed_img.append(cv2.resize(img, dsize=(img_w, img_h), interpolation=cv2.INTER_CUBIC))
cropped_img.append(original_img[top:bottom, left:right])

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 4), num="Rotitated (zoom)")
fig.suptitle("Rotated Results", fontsize=15)
for i in range(3):
    ax = axs.flat[i]
    ax.imshow(cropped_img[i], cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{interpolation_text[i]}")

plt.tight_layout()
plt.show()
