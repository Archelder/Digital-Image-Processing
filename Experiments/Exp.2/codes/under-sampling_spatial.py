# import OpenCV and Matplotlib libraries
import cv2
import matplotlib.pyplot as plt

# read the original image from file and define its DPI
original_img = cv2.imread("../images/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif", flags=0)
ORIGINAL_DPI = 1250

# get the height and width of the original image
img_h, img_w = original_img.shape

# define a list of target DPI values to which the image will be under-sampled
target_dpi = [300, 150, 72]

# calculate the resize ratio for each target DPI value
resize_ratio = []
for i in target_dpi:
    resize_ratio.append((i / ORIGINAL_DPI))

# create a list to store the reduced images
reduced_img = []
for ratio in resize_ratio:
    # apply the resize ratio to the original image using OpenCV's resize method
    reduced_img.append(cv2.resize(original_img, dsize=None, fx=ratio, fy=ratio))

# create a figure with subplots to display the original image and the reduced images side-by-side
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 10), num="Spatial Under-sampling")
fig.suptitle("Spatial Under-sampling", fontsize=15)

# display the original image in the first subplot
ax = axs[0, 0]
ax.imshow(original_img, cmap='gray')
ax.set_title(f"{ORIGINAL_DPI} dpi")
ax.set_xticks([])
ax.set_yticks([])

# display each reduced image in a separate subplot
for i in range(3):
    ax = axs.flat[i + 1]
    ax.imshow(reduced_img[i], cmap='gray')
    ax.set_title(f"{target_dpi[i]} dpi")
    ax.set_xticks([])
    ax.set_yticks([])

# define the coordinates of the region of interest to be cropped
top = int(img_h * 3 / 5)
bottom = int(img_h * 0.9)
left = int(img_w * 3 / 5)
right = int(img_w * 0.9)

cropped_img = [original_img[top:bottom, left:right]]
for img in reduced_img:
    h, w = img.shape[:2]
    top = int(h * 3 / 5)
    bottom = int(h * 0.9)
    left = int(w * 3 / 5)
    right = int(w * 0.9)
    cropped_img.append(img[top:bottom, left:right])

# create a second figure with subplots to display the cropped images side-by-side
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 10), num="Spatial Under-sampling (zoom)")
fig.suptitle("Spatial Under-sampling (zoom)", fontsize=15)

# display the original cropped image in the first subplot
ax = axs[0, 0]
ax.imshow(cropped_img[0], cmap='gray')
ax.set_title(f"{ORIGINAL_DPI} dpi")
ax.set_xticks([])
ax.set_yticks([])

# display each cropped and reduced image in a separate subplot
for i in range(3):
    ax = axs.flat[1 + i]
    ax.imshow(cropped_img[i + 1], cmap='gray')
    ax.set_title(f"{target_dpi[i]} dpi")
    ax.set_xticks([])
    ax.set_yticks([])

# adjust the spacing between subplots and display the figures
plt.tight_layout()
plt.show()
