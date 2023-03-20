import cv2
import matplotlib.pyplot as plot
import numpy as np


def gauss_noise(mean, stand_deviation, shape):
    noise = np.random.normal(mean, stand_deviation, shape)
    return noise


def noisy_image_average(mean, stand_deviation, img, k):
    g = np.zeros(img.shape)
    for i in range(k):
        g += gauss_noise(mean, stand_deviation, img.shape)
        g /= k
    averaging_img = img + g
    return averaging_img


original_img = cv2.imread('../images/Fig0226(galaxy_pair_original).png', flags=0)

Gauss_Noise = gauss_noise(0, 64, original_img.shape)
noisy_img = original_img + Gauss_Noise

averaging_img_5 = noisy_image_average(0, 64, original_img, 5)
averaging_img_10 = noisy_image_average(0, 64, original_img, 10)
averaging_img_20 = noisy_image_average(0, 64, original_img, 20)
averaging_img_50 = noisy_image_average(0, 64, original_img, 50)
averaging_img_100 = noisy_image_average(0, 64, original_img, 100)

plot.figure(figsize=(8, 8))
plot.subplot(332), plot.imshow(original_img, cmap='gray'), plot.title('original image'), plot.axis('off')
plot.subplot(334), plot.imshow(noisy_img, cmap='gray'), plot.title('noisy image'), plot.axis('off')
plot.subplot(335), plot.imshow(averaging_img_5, cmap='gray'), plot.title('averaging image (k=5)'), plot.axis('off')
plot.subplot(336), plot.imshow(averaging_img_10, cmap='gray'), plot.title('averaging image (k=10)'), plot.axis('off')
plot.subplot(337), plot.imshow(averaging_img_20, cmap='gray'), plot.title('averaging image (k=20)'), plot.axis('off')
plot.subplot(338), plot.imshow(averaging_img_50, cmap='gray'), plot.title('averaging image (k=50)'), plot.axis('off')
plot.subplot(339), plot.imshow(averaging_img_100, cmap='gray'), plot.title('averaging image (k=100)'), plot.axis('off')
plot.tight_layout()
plot.show()
