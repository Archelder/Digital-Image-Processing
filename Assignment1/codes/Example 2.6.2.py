import cv2
import matplotlib.pyplot as plot
import numpy as np

mask_img = cv2.imread('../images/Fig0228(a)(angiography_mask_image).png', flags=0)
live_img = cv2.imread('../images/Fig0228(b)(angiography_live_image).png', flags=0)

# Obtain the differences between mask image and live image, using function cv2.substract().
diff_img = cv2.subtract(mask_img, live_img)

# Enhence the differences image.
enhenced_img = diff_img / 255.0
enhenced_img = np.power(enhenced_img, 0.7)
enhenced_img *= 255

# Display the results.
plot.subplot(221), plot.imshow(mask_img, cmap='gray'), plot.title('make image'), plot.axis('off')
plot.subplot(222), plot.imshow(live_img, cmap='gray'), plot.title('live image'), plot.axis('off')
plot.subplot(223), plot.imshow(diff_img, cmap='gray'), plot.title('differences image'), plot.axis('off')
plot.subplot(224), plot.imshow(enhenced_img, cmap='gray'), plot.title('enhenced image'), plot.axis('off')
plot.savefig('../images/Results Example 2.6.2.png')
plot.show()
