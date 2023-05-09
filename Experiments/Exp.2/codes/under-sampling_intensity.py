# import necessary libraries
import cv2
import matplotlib.pyplot as plt

# read in the original image in grayscale
original_img = cv2.imread("../images/Fig0221(a)(ctskull-256).tif", flags=0)

# the number of gray levels of the original image
ORIGINAL_GRAY_LEVELS = 256

# define a list of target gray levels to which we will reduce the image
target_gray_levels = [128, 64, 32, 16, 8, 4, 2]

# create an empty list to store the reduced images
reduced_img = []

# loop over each target gray level
for levels in target_gray_levels:
    # calculate the scaling factor for this level
    alpha = ((levels - 1) / (ORIGINAL_GRAY_LEVELS - 1))

    # reduce the image to the target gray level and append it to the list of reduced images
    reduced_img.append(cv2.convertScaleAbs(original_img, alpha=alpha))

# display the original image with 256 gray levels and the reduced images with the specified number of gray levels
plt.subplots(2, 4, figsize=(14.4, 8.64))
plt.subplot(241), plt.imshow(original_img, cmap='gray'), plt.title("256 levels"), plt.axis('off')
for i in range(7):
    plt.subplot(242 + i), plt.imshow(reduced_img[i], cmap='gray'), \
        plt.title(f"{target_gray_levels[i]} levels"), plt.axis('off')
plt.suptitle("Intensity Under-sampling", fontsize=20)
plt.show()
