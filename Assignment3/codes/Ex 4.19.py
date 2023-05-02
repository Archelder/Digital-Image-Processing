import cv2
import numpy as np
import matplotlib.pyplot as plt


def butterHP(D, n, shape):
    """
    :param D: cutoff frequency
    :param n: order
    :param shape: (rows, columns)
    :return: array H with the same shape
    """
    H = np.zeros(shape, dtype=np.float64)
    row_c, col_c = np.floor(shape[0] / 2), np.floor(shape[1] / 2)
    for u in range(shape[0]):
        for v in range(shape[1]):
            d = np.sqrt(((u - row_c) ** 2) + ((v - col_c) ** 2))
            H[u, v] = 1 / (1 + np.power(D / (0.00000000001 + d), 2 * n))
    return H


# read the original image
original_img = cv2.imread("../images/Fig0457(a)(thumb_print).png", flags=0)

# calculate the 2D DFT of the original image using `np.fft.fft2()`
original_frq = np.fft.fft2(original_img)

# centralize DFT
centred_original_frq = np.fft.fftshift(original_frq)

# construct a Butterworth Highpass Filter
BHPF = butterHP(D=25, n=4, shape=original_img.shape)

centred_filtered_frq = centred_original_frq * BHPF
filtered_frq = np.fft.ifftshift(centred_filtered_frq)
filtered_img = np.real(np.fft.ifft2(filtered_frq))
filtered_img_cutoff = filtered_img.copy()
filtered_img_cutoff[filtered_img_cutoff < 0] = 0

# threshold the filtered image setting negative values to 0, positive values to 1
threshold_img = filtered_img.copy()
threshold_img[threshold_img < 0] = 0
threshold_img[threshold_img > 0] = 1

# display the results
plt.figure("Butterworth Highpass Filtering", (12, 4))
plt.subplot(141), plt.imshow(original_img, 'gray'), plt.title("original"), plt.axis('off')
plt.subplot(142), plt.imshow(filtered_img_cutoff, 'gray'), plt.title("filtered (unnormalized)"), plt.axis('off')
plt.subplot(143), plt.imshow(filtered_img, 'gray'), plt.title("filtered (normalized)"), plt.axis('off')
plt.subplot(144), plt.imshow(threshold_img, 'gray'), plt.title("filtered (thresholded)"), plt.axis('off')
plt.suptitle(f"Running Results of Example 4.19 Butterworth Highpass Filtering")

plt.tight_layout()
plt.show()
