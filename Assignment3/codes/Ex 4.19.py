import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the original image
original_img = cv2.imread("../images/Fig0457(a)(thumb_print).png", flags=0)

# calculate the spectrum of the original image using `np.fft.fft2()`
spectrum = np.fft.fft2(original_img)

# centralise the spectrum of the original image using `np.fft.fftshift()`
spectrum = np.fft.fftshift(spectrum)

# construct a Butterworth Highpass Filter with $D=50$, $n=4$
D = 50
n = 4
rows, cols = original_img.shape
centre_r, centre_c = rows // 2, cols // 2

H_bhpf = np.zeros((rows, cols), np.float64)
for u in range(rows):
    for v in range(cols):
        d = np.sqrt((u - centre_c) ** 2 + (v - centre_r) ** 2)
        if d != 0:
            H_bhpf[u, v] = 1 / (1 + (D / d) ** (2 * n))
        else:
            H_bhpf[u, v] = 1

# apply BHPF to the spectrum of the original image
filtered_spectrum = spectrum * H_bhpf

# calculate the image after BHP filtering using `np.fft.ifftshift()` and `np.fft.ifft2()`
filtered_spectrum = np.fft.ifftshift(filtered_spectrum)
filtered_img = np.fft.ifft2(filtered_spectrum)
filtered_img = np.real(filtered_img)
_, cutoff_image = cv2.threshold(filtered_img, 0, 255, cv2.THRESH_TOZERO)
# threshold the filtered image
thresholded_img = filtered_img.copy()
thresholded_img[thresholded_img < 0] = 0
thresholded_img[thresholded_img > 0] = 1
thresholded_img = -thresholded_img

# display results
plt.figure("Highpass Filtering", (12, 5))
plt.subplot(141), \
    plt.imshow(original_img, 'gray'), plt.title("original"), plt.axis('off')
plt.subplot(142), \
    plt.imshow(cutoff_image, 'gray'), \
    plt.title("filtered image (unnormalized)"), plt.axis('off')
plt.subplot(143), \
    plt.imshow(filtered_img, 'gray'), plt.title("filtered image (normalized)"), plt.axis('off')
plt.subplot(144), \
    plt.imshow(thresholded_img, 'gray'), plt.title("threshold imgage"), plt.axis('off')
plt.suptitle("Highpass Filtering")
plt.tight_layout()
plt.show()
