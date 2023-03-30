import cv2
import numpy as np
import matplotlib.pyplot as plt

img_a_lt = np.ones((256, 128))
img_a_rt = np.zeros((256, 128))
img_a = np.concatenate((img_a_lt, img_a_rt), axis=1)
img_a = img_a.astype(np.uint8)

img_b_white = np.ones((32, 32))
img_b_black = np.zeros((32, 32))
img_b_piece = np.concatenate(
    (np.concatenate((img_b_white, img_b_black), axis=1), np.concatenate((img_b_black, img_b_white), axis=1)), axis=0)
img_b = np.tile(img_b_piece, (4, 4))
img_b = img_b.astype(np.uint8)

hist_a = cv2.calcHist([img_a], channels=[0], mask=None, histSize=[1], ranges=[0, 2])
hist_b = cv2.calcHist([img_b], channels=[0], mask=None, histSize=[1], ranges=[0, 2])

plt.subplot(221), plt.imshow(img_a, cmap='gray'), plt.title('image a'), plt.axis('off')
plt.subplot(222), plt.hist(img_a.ravel()), plt.title('histgram a')
plt.subplot(223), plt.imshow(img_b, cmap='gray'), plt.title('image b'), plt.axis('off')
plt.subplot(224), plt.hist(img_b.ravel()), plt.title('histgram b')

plt.tight_layout()
plt.show()
