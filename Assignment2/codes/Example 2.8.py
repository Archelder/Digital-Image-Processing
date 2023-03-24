import cv2
import numpy as np
import matplotlib.pyplot as plot

original_img = cv2.imread('../images/Fig0232(a)(partial_body_scan).png')
complement_img = cv2.bitwise_not(original_img)

# Generate a constant image whose size is same as the original image, and the value of its elements is 3 times the mean
# intensity of the original image.
constant_img = np.ones(shape=original_img.shape, dtype=np.uint8) * 3 * np.int8(np.mean(original_img))

# Generate the union of the original image and the constant image.
union_img = cv2.max(original_img, constant_img)

# Display the results.
plot.subplot(131), plot.imshow(original_img, cmap='gray'), plot.title('original image'), plot.axis('off')
plot.subplot(132), plot.imshow(complement_img, cmap='gray'), plot.title('complement image'), plot.axis('off')
plot.subplot(133), plot.imshow(union_img, cmap='gray'), plot.title('union image'), plot.axis('off')
plot.savefig('../images/Result Example 2.8.png')
plot.show()
