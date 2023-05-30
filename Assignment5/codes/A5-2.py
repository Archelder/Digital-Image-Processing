import cv2
import matplotlib.pyplot as plt

# open
original_image = cv2.imread("../images/FigP0934.png", flags=0)
target_image = []

middle_size = (50, 50)
middle_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, middle_size)
target_image.append(cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, middle_element))

large_size = (100, 100)
large_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, large_size)
target_image.append(cv2.morphologyEx(target_image[0], cv2.MORPH_OPEN, large_element))

cut_size = (10, 10)
element = cv2.getStructuringElement(cv2.MORPH_RECT, cut_size)
target_image.append(cv2.morphologyEx(target_image[1], cv2.MORPH_GRADIENT, element))

target_image.append(cv2.bitwise_or(original_image, target_image[2]))

# display the results
fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(10, 2))
ax = axs[0]
ax.imshow(original_image, cmap='gray'), ax.set_title(f"original image"), ax.set_xticks([]), ax.set_yticks([])
for i in range(4):
    ax = axs[i + 1]
    ax.imshow(target_image[i], 'gray')
    ax.set_title(f"Step {i + 1}")
    ax.set_xticks([]), ax.set_yticks([])

plt.suptitle("Running Results of Textural segmentation")
plt.tight_layout()

# save
# output = f'../images/Textural segmentation.jpg'
# plt.savefig(output)

plt.show()
