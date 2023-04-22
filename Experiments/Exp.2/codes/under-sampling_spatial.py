import cv2
import matplotlib.pyplot as plt

original_img = cv2.imread("../images/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif", flags=0)
ORIGINAL_DPI = 1250
img_h, img_w = original_img.shape
target_dpi = [300, 150, 72]

resize_ratio = []
for i in target_dpi:
    resize_ratio.append((i / ORIGINAL_DPI))

reduced_img = []
for ratio in resize_ratio:
    reduced_img.append(cv2.resize(original_img, dsize=None, fx=ratio, fy=ratio))

results = plt.figure("Results")
plt.subplot(221), plt.imshow(original_img, cmap='gray'), plt.title("1250 dpi"), plt.axis('off')
for i in range(3):
    plt.subplot(222 + i), plt.imshow(reduced_img[i], cmap='gray'), plt.title(f"{target_dpi[i]} dpi"), plt.axis('off')

cropped_img = []
zoomed_img = []
top = img_h // 4
bottom = img_h // 2
left = img_w // 4
right = img_w // 2

for img in reduced_img:
    zoomed_img.append(cv2.resize(img, dsize=(img_w, img_h)))

cropped_img.append(original_img[top:bottom, left:right])
for img in zoomed_img:
    cropped_img.append(img[top:bottom, left:right])

results_zoomed = plt.figure("Results (zoomed)")
plt.subplot(221), plt.imshow(cropped_img[0], cmap='gray'), plt.title("1250 dpi"), plt.axis('off')
for i in range(3):
    plt.subplot(222 + i), plt.imshow(cropped_img[i + 1], cmap='gray'), plt.title(f"{target_dpi[i]} dpi"), plt.axis(
        'off')
plt.show()
