import cv2
import numpy as np
import matplotlib.pyplot as plt


def geometric_mean_filter(img, size):
    h, w = img.shape[:2]
    order = 1 / np.power(size, 2)
    pad = int((size - 1) / 2)
    padded_img = np.pad(img, pad, mode='edge')


def GMF(shape):
    return geometric_mean_filter(shape)


# read the original image
original_image = cv2.imread("../images/FigP0501.png", flags=0)
