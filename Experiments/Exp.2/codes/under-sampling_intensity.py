import cv2
import matplotlib.pyplot as plt

original_img = cv2.imread("../images/Fig0221(a)(ctskull-256).tif", flags=0)
ORIGINAL_GRAY_LEVELS = 256
target_gray_levels = [128, 64, 32, 16, 8, 4, 2]
reduced_img = []

for levels in target_gray_levels:
    reduced_img.append(cv2.convertScaleAbs(original_img, alpha=((levels - 1) / (ORIGINAL_GRAY_LEVELS - 1))))

plt.subplot(241), plt.imshow(original_img, cmap='gray'), plt.title("256 levels"), plt.axis('off')

for i in range(7):
    plt.subplot(242 + i), plt.imshow(reduced_img[i], cmap='gray'), \
        plt.title(f"{target_gray_levels[i]} levels"), plt.axis('off')

plt.show()
