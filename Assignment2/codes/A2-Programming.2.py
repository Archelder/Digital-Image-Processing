import cv2
import numpy as np
import matplotlib.pyplot as plt

GAMMA = 0.6

a_original_img = cv2.imread('../images/Fig0343(a)(skeleton_orig).png', 0)
a_original_img = a_original_img.astype(np.float64)

b_laplacian_img = cv2.Laplacian(a_original_img, cv2.CV_64F, None)
norm_b_laplacian_img = cv2.normalize(b_laplacian_img, None, 0, 256, cv2.NORM_MINMAX)

c_sharpened_img = cv2.add(a_original_img, b_laplacian_img)  # c_sharpened_img = a_original_img + b_laplacian_img

d_sobel_img_x = cv2.Sobel(a_original_img, cv2.CV_64F, 1, 0)
d_sobel_img_x = cv2.convertScaleAbs(d_sobel_img_x)
d_sobel_img_y = cv2.Sobel(a_original_img, cv2.CV_64F, 0, 1)
d_sobel_img_y = cv2.convertScaleAbs(d_sobel_img_y)
d_sobel_img = cv2.addWeighted(d_sobel_img_x, 0.5, d_sobel_img_y, 0.5, 0, dtype=cv2.CV_64F)

e_smoothed_sobel_img = cv2.blur(d_sobel_img, (5, 5))

f_mask_img = np.multiply(norm_b_laplacian_img, e_smoothed_sobel_img)

g_sharpened_img = cv2.add(a_original_img, f_mask_img)
g_sharpened_img = cv2.normalize(g_sharpened_img, None, 0, 256, cv2.NORM_MINMAX)
h_gamma_trans_img = (cv2.pow((g_sharpened_img / 255), GAMMA)) * 255  # transformed from g_sharpened_img

plt.figure(figsize=(12, 8))

ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 1
plt.subplot(2, 4, i)
plt.imshow(a_original_img, cmap='gray'), plt.title(f'({ls[i - 1]}) original', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i)
plt.imshow(norm_b_laplacian_img, cmap='gray'), plt.title(f'({ls[i - 1]}) laplacian', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i)
plt.imshow(c_sharpened_img, cmap='gray'), plt.title(f'({ls[i - 1]}) sharpened by laplacian', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i)
plt.imshow(d_sobel_img, cmap='gray'), plt.title(f'({ls[i - 1]}) sobel', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i)
plt.imshow(e_smoothed_sobel_img, cmap='gray'), plt.title(f'({ls[i - 1]}) smoothed sobel', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i)
plt.imshow(f_mask_img, cmap='gray'), plt.title(f'({ls[i - 1]}) mask', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i)
plt.imshow(g_sharpened_img, cmap='gray'), plt.title(f'({ls[i - 1]}) sharpened by mask', y=-0.1), plt.axis('off')
i += 1
plt.subplot(2, 4, i), plt.imshow(h_gamma_trans_img, cmap='gray')
plt.title(f'({ls[i - 1]}) sharpened by mask\n ($\gamma = {GAMMA}$)', y=-0.15), plt.axis('off')

plt.tight_layout()
plt.show()