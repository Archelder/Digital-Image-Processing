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
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), num="Spatial Under-sampling")
fig.suptitle("Spatial Under-sampling", fontsize=15)

# display the original image in the first subplot
axs[0, 0].imshow(original_img, cmap='gray')
axs[0, 0].axis('off')
axs[0, 0].set_title(f"{ORIGINAL_DPI} dpi")

# display each reduced image in a separate subplot
i = 0
for ax in axs.flat[1:]:
    ax.imshow(reduced_img[i], cmap='gray')
    ax.set_title(f"{target_dpi[i]} dpi")
    ax.axis('off')
    i += 1
del i

# create a list to store the cropped images
cropped_img = []
zoomed_img = []

# define the coordinates of the region of interest to be cropped (the center half of the image)
top = img_h // 4
bottom = img_h // 2
left = img_w // 4
right = img_w // 2

# perform the same cropping and downsizing on each image, and save the resulting images in lists
for img in reduced_img:
    zoomed_img.append(cv2.resize(img, dsize=(img_w, img_h)))
cropped_img.append(original_img[top:bottom, left:right])
for img in zoomed_img:
    cropped_img.append(img[top:bottom, left:right])

# create a second figure with subplots to display the cropped images side-by-side
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), num="Spatial Under-sampling (zoom)")
fig.suptitle("Spatial Under-sampling (zoom)", fontsize=15)

# display the original cropped image in the first subplot
axs[0, 0].imshow(cropped_img[0], cmap='gray')
axs[0, 0].axis('off')
axs[0, 0].set_title(f"{ORIGINAL_DPI} dpi")

# display each cropped and reduced image in a separate subplot
i = 0
for ax in axs.flat[1:]:
    ax.imshow(cropped_img[i], cmap='gray')
    ax.set_title(f"{target_dpi[i]} dpi")
    ax.axis('off')
    i += 1
del i

# adjust the spacing between subplots and display the figures
plt.tight_layout()
plt.show()
