import cv2
import numpy as np
import matplotlib.pyplot as plt


def motion_degrade_function(img, a=0.1, b=0.1, T=1):
    M, N = img.shape[:2]
    H = np.empty(img.shape, dtype=complex)
    # calculate the transfer function of motion blur
    for u in range(M):
        for v in range(N):
            s = u * a + v * b
            H[u, v] = (T / (np.pi * s + np.finfo(complex).eps)) * np.sin(np.pi * s) * np.exp(-1j * np.pi * s)
    return H


def motion_blur(img, a=0.1, b=0.1, T=1):
    H = motion_degrade_function(img, a, b, T)
    # apply the transfer function of motion blur
    f = img.copy()
    F = np.fft.fft2(f)
    G = H * F
    g = np.fft.ifft2(G)
    g = np.real(g)
    return g


def inverse_motion_blur(img, a=0.1, b=0.1, T=1):
    H = motion_degrade_function(img, a, b, T)
    # apply the transfer function of motion blur
    g = img.copy()
    G = np.fft.fft2(g)
    F = G / (H + np.finfo(complex).eps)
    f = np.fft.ifft2(F)
    f = np.real(f)
    return f


def gauss_blur(img, mean, stand_deviation):
    n = np.random.normal(mean, stand_deviation, img.shape)
    f = img.copy()
    g = f + n
    return g


def wiener_filter(img, H, K):
    G = np.fft.fft2(img)
    H_square = np.power(H, 2)
    H_abs = np.abs(H)
    F = ((1 / (H_abs + np.finfo(complex).eps)) * (H_square / (H_square + K))) * G
    f = np.real(np.fft.ifft2(F))
    return f


original_img = cv2.imread("../images/Fig0526(a).png", 0)
trans_func = motion_degrade_function(original_img)
motion_blurred_img = motion_blur(original_img)

gauss_blurred_img = gauss_blur(motion_blurred_img, 0, np.sqrt(650))

inverse_filtered_img = inverse_motion_blur(gauss_blurred_img)
wiener_filtered_img = wiener_filter(gauss_blurred_img, trans_func, K=0.1)
CLS_filtered_img = 0

# display the results
img_ls = [original_img, motion_blurred_img, gauss_blurred_img, inverse_filtered_img, wiener_filtered_img,
          CLS_filtered_img]
title_ls = ['original image', 'motion blurred', 'motion blurred with Gaussian noise', 'inverse filtered',
            'wiener filtered', 'constrained least squares filtered']
fig, axs = plt.subplots(2, 3, figsize=(10, 8))
for i in range(5):
    ax = axs.flat[i]
    ax.imshow(img_ls[i], cmap='gray')
    ax.set_title(title_ls[i])
    ax.set_xticks([])
    ax.set_yticks([])
axs[1, 2].set_visible(False)
plt.tight_layout()
plt.show()
