import cv2
import numpy as np
import matplotlib.pyplot as plt


def motion_blur(img, a=0.1, b=0.1, T=1):
    M, N = img.shape[:2]
    H = np.empty(img.shape, dtype=np.complex128)
    # calculate the transfer function of motion blur
    for u in range(M):
        for v in range(N):
            s = u * a + v * b
            H[u, v] = (T / (np.pi * s + np.finfo(float).eps)) * np.sin(np.pi * s) * np.exp(-1j * np.pi * s)
    # apply the transfer function of motion blur
    f = img
    F = np.fft.fft2(f)
    G = H * F
    g = np.fft.ifft2(G)
    g = np.real(g)
    return g


original_img = cv2.imread("../images/Fig0526(a).png", 0)

blurred_img = motion_blur(original_img)

plt.figure(figsize=(6, 4))
plt.subplot(121), plt.imshow(original_img, 'gray'), plt.title("original image"), plt.axis('off')
plt.subplot(122), plt.imshow(blurred_img, 'gray'), plt.title("blurred image"), plt.axis('off')
plt.suptitle("Image Blurring due to Motion")
plt.tight_layout()
plt.show()
