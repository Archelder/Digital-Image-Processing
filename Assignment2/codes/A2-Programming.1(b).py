import cv2
import numpy as np
import matplotlib.pyplot as plt

img_a_lt = np.ones((256, 128))
img_a_rt = np.zeros((256, 128))
img_a = np.concatenate((img_a_lt, img_a_rt), axis=1)

img_b_white = np.ones((32, 32))
img_b_black = np.zeros((32, 32))
img_b_piece = np.concatenate(
    (np.concatenate((img_b_white, img_b_black), axis=1), np.concatenate((img_b_black, img_b_white), axis=1)), axis=0)
img_b = np.tile(img_b_piece, (4, 4))

# blur images
img_a_blurred = cv2.blur(img_a, ksize=(9, 9))
img_b_blurred = cv2.blur(img_b, ksize=(9, 9))

plt.subplot(231), plt.imshow(img_a, cmap='gray'), plt.title('image a'), plt.axis('off')
plt.subplot(232), plt.imshow(img_a_blurred, cmap='gray'), plt.title('blurred image a'), plt.axis('off')
plt.subplot(233), plt.hist(img_a_blurred.ravel(), bins=64), plt.title('histogram of \nblurred image a')
plt.subplot(234), plt.imshow(img_b, cmap='gray'), plt.title('image b'), plt.axis('off')
plt.subplot(235), plt.imshow(img_b_blurred, cmap='gray'), plt.title('blurred image b'), plt.axis('off')
plt.subplot(236), plt.hist(img_b_blurred.ravel(), bins=64), plt.title('histogram of \nblurred image b')
plt.tight_layout()
plt.savefig('../images/ansfig_A2-Programming.1(b).png')
plt.show()
