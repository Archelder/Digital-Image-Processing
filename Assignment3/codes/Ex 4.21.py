import cv2
import numpy
import matplotlib.pyplot as plt

original_image = cv2.imread("../images/Fig0459(a)(orig_chest_xray).png", flags=0)

# FFT and shift
original_frq = numpy.fft.fft2(original_image)
centred_original_frq = numpy.fft.fftshift(original_frq)

# construct a Gaussian Highpass Filter
rows, cols = original_image.shape  # rows cols分别得到图像的行数和列数
row_centre, col_centre = rows // 2, cols // 2  # 得到图像中心点的坐标（crow，cols）
D0 = 70
GHPF = numpy.zeros((rows, cols))
for u in range(rows):
    for v in range(cols):
        D2 = (u - row_centre) ** 2 + (v - col_centre) ** 2
        GHPF[u, v] = 1 - numpy.exp(-D2 / (2 * D0 * D0))

centred_filtered_frq = centred_original_frq * GHPF
filtered_frq = numpy.fft.ifftshift(centred_filtered_frq)
filtered_img = numpy.real(numpy.fft.ifft2(filtered_frq))

# high-frequency-emphasis filtering using the same filter
k1 = 0.5
k2 = 0.75
centred_enhanced_filtered_freq = numpy.zeros((rows, cols), dtype=numpy.complex128)
for u in range(rows):
    for v in range(cols):
        centred_enhanced_filtered_freq[u, v] = (k1 + k2 * GHPF[u, v]) * centred_original_frq[u, v]
enhanced_filtered_frq = numpy.fft.ifftshift(centred_enhanced_filtered_freq)
enhanced_filtered_img = numpy.real(numpy.fft.ifft2(enhanced_filtered_frq))

# performing histogram equalization
equalized_img = cv2.equalizeHist(enhanced_filtered_img.astype(numpy.uint8))

# display the results
plt.figure("High-Frequency-Emphasis Filtering", (8, 8))
plt.subplot(221), plt.imshow(original_image, 'gray'), plt.title("original"), plt.axis('off')
plt.subplot(222), plt.imshow(filtered_img, 'gray'), plt.title("filtered"), plt.axis('off')
plt.subplot(223), plt.imshow(enhanced_filtered_img, 'gray'), plt.title("enhanced filtered"), plt.axis('off')
plt.subplot(224), plt.imshow(equalized_img, 'gray'), plt.title("equalized"), plt.axis('off')
plt.suptitle(f"Running Results of Example 4.21 High-Frequency-Emphasis Filtering")

plt.tight_layout()
plt.show()
