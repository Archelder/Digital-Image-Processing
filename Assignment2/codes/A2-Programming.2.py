import cv2
import numpy as np
import matplotlib.pyplot as plt

LAPLACIAN_KERNEL = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
],
    dtype=np.int16)

SOBEL_KERNEL = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1],
],
    dtype=np.int16)

a_original_img = cv2.imread('../images/Fig0343(a)(skeleton_orig).png', 0)
a_original_img = a_original_img.astype(np.int16)

b_laplacian_img = cv2.filter2D(a_original_img, -1, LAPLACIAN_KERNEL)

c_sharpened_img = cv2.add(a_original_img, b_laplacian_img)  # c_sharpened_img = a_original_img + b_laplacian_img

d_sobel_img = cv2.Sobel(a_original_img,-1)

e_smoothed_sobel_img = None
f_mask_img = None  # f_mask_img = b_laplacian_img * e_smoothed_sobel_img
g_sharpened_img = None  #
h_sigma_trans_img = None  # transformed from g_sharpened_img

norm_b_laplacian_img = cv2.normalize(b_laplacian_img, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(10, 8))
plt.subplot(221), plt.imshow(a_original_img, cmap='gray'), plt.title('original'), plt.axis('off')
plt.subplot(222), plt.imshow(b_laplacian_img, cmap='gray'), plt.title('laplacian'), plt.axis('off')
plt.subplot(223), plt.imshow(c_sharpened_img, cmap='gray'), plt.title('sharpened by laplacian'), plt.axis('off')
plt.subplot(224), plt.imshow(d_sobel_img, cmap='gray'), plt.title('sobel grad'), plt.axis('off')
plt.tight_layout()
plt.show()
