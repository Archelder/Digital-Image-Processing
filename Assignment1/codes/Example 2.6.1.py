import cv2
import matplotlib.pyplot as plot
import numpy as np

# Load the original image as gray.
original_img = cv2.imread('../images/Fig0227(a)(washington_infrared).png', flags=0)

# Generate one 8-bit ndarray with all element values of 1111_1110B as the same shape as the original image,
# set its data type to np.uint8.
set_zero_ndarray = np.ones(original_img.shape, dtype=np.uint8) * 0b1111_1110

# Conduct bitwisen and operation, assign the result to variable set_img.
set_img = cv2.bitwise_and(original_img, set_zero_ndarray)

diff_img = (original_img - set_img) * 0b1111_1111

# Display the results.
plot.subplot(131), plot.imshow(original_img, cmap='gray'), plot.title('original image'), plot.axis('off')
plot.subplot(132), plot.imshow(set_img, cmap='gray'), plot.title('set zero image'), plot.axis('off')
plot.subplot(133), plot.imshow(diff_img, cmap='gray'), plot.title('differences image'), plot.axis('off')
plot.savefig('../images/Result Example 2.6.1.png')
plot.show()
