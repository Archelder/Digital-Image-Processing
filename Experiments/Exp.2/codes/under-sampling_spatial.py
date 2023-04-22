import cv2
import matplotlib.pyplot as plt

original_img = cv2.imread("../images/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif", flags=0)
ORIGINAL_DPI = 1250
target_dpi = [300, 150, 72]

resize_ratio = []
for i in target_dpi:
    resize_ratio.append((i / ORIGINAL_DPI))

reduced_img = []
for ratio in resize_ratio:
    reduced_img.append(cv2.resize(original_img, dsize=None, fx=ratio, fy=ratio))

plt.subplot(221), plt.imshow(original_img, cmap='gray'), plt.title("1250 dpi"), plt.axis('off')

for i in range(3):
    plt.subplot(222 + i), plt.imshow(reduced_img[i], cmap='gray'), plt.title(f"{target_dpi[i]} dpi"), plt.axis('off')

plt.show()
