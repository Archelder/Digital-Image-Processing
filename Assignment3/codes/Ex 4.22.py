import cv2
import numpy as np
import matplotlib.pyplot as plt


def homo_filter(gamma_L, gamma_H, c, D, shape):
    H = np.zeros(shape, dtype=np.float64)
    row_c, col_c = np.floor(shape[0] / 2), np.floor(shape[1] / 2)
    D_sqr = D ** 2
    for u in range(shape[0]):
        for v in range(shape[1]):
            d_sqr = ((u - row_c) ** 2) + ((v - col_c) ** 2)
            H[u, v] = ((gamma_H - gamma_L) * (1 - np.exp(-c * d_sqr / D_sqr))) + gamma_L
    return H


# define constants
GAMMA_L = 0.4
GAMMA_H = 3.0
SLOPE = 5
CUTOFF_FREQUENCY = 20

# read the original image
original_img = cv2.imread("../images/Fig0462(a)(PET_image).png", flags=0)

# calculate the 2D DFT of the original image using `np.fft.fft2()`
original_frq = np.fft.fft2(original_img)

# centralize DFT
centred_original_frq = np.fft.fftshift(original_frq)

# construct a Homomorphic Filter
HF = homo_filter(GAMMA_L, GAMMA_H, c=SLOPE, D=CUTOFF_FREQUENCY, shape=original_img.shape)

# apply the Homomorphic Filter
centred_filtered_frq = centred_original_frq * HF

# inverse the 2D DFT
filtered_frq = np.fft.ifftshift(centred_filtered_frq)
filtered_img = np.real(np.fft.ifft2(filtered_frq))

plt.imshow(filtered_img, 'gray')
plt.show()
