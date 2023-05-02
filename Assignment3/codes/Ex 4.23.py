import cv2
import numpy as np
import matplotlib.pyplot as plt


def butter_notch_reject(Q, u_list, v_list, D_list, n, shape):
    M, N = shape
    row_c, col_c = np.floor(M / 2), np.floor(N / 2)
    H_NR = np.ones(shape, dtype=np.float64)
    for k in range(Q):
        H = np.zeros(shape, dtype=np.float64)
        H_1 = np.zeros(shape, dtype=np.float64)
        H_2 = np.zeros(shape, dtype=np.float64)
        for u in range(M):
            for v in range(N):
                d_1 = np.sqrt((u - row_c - u_list[k]) ** 2 + (v - col_c - v_list[k]) ** 2)
                d_2 = np.sqrt((u - row_c + u_list[k]) ** 2 + (v - col_c + v_list[k]) ** 2)
                H_1[u, v] = 1 / (1 + np.power(D_list[k] / (0.00000000001 + d_1), 2 * n))
                H_2[u, v] = 1 / (1 + np.power(D_list[k] / (0.00000000001 + d_2), 2 * n))
        H = H_1 * H_2
        H_NR *= H
    return H_NR


# read the original image
original_img = cv2.imread("../images/Fig0464(a)(car_75DPI_Moire).png", flags=0)

# calculate the 2D DFT of the original image
original_frq = np.fft.fft2(original_img)
centred_original_frq = np.fft.fftshift(original_frq)

original_spectrum = np.abs(centred_original_frq)
log_spectrum = np.log(original_spectrum)

xs = [55, 55, 57, 58]
ys = [44, 86, 166, 207]
u = []
v = []
row_c, col_c = np.floor(original_img.shape[0] / 2), np.floor(original_img.shape[1] / 2)
for x in xs:
    v.append(col_c - x)
for y in ys:
    u.append(row_c - y)

D = [9 for i in range(4)]
BNRF = butter_notch_reject(4, u, v, D, n=4, shape=original_img.shape)
centred_filtered_frq = centred_original_frq * BNRF
filtered_spectrum = log_spectrum * BNRF
log_filtered_spectrum = np.log(filtered_spectrum)

# inverse the 2D DFT
filtered_frq = np.fft.ifftshift(centred_filtered_frq)
filtered_img = np.real(np.fft.ifft2(filtered_frq))

# display the results
plt.figure("Notch Reject Filtering", (6, 8))
plt.subplot(221), plt.imshow(original_img, 'gray'), plt.title("original image"), plt.axis('off')
plt.subplot(222), plt.imshow(log_spectrum, 'gray'), plt.title("original spectrum"), plt.axis('off')
plt.subplot(223), plt.imshow(filtered_spectrum, 'gray'), plt.title("filtered spectrum"), plt.axis('off')
plt.subplot(224), plt.imshow(filtered_img, 'gray'), plt.title("filtered image"), plt.axis('off')

plt.tight_layout()
plt.show()
