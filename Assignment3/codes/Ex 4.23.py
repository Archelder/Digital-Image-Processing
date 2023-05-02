import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the original image
original_img = cv2.imread("../images/Fig0464(a)(car_75DPI_Moire).png", flags=0)

# calculate the 2D DFT of the original image
original_frq = np.fft.fft2(original_img)
centred_original_frq = np.fft.fftshift(original_frq)

plt.figure("Notch Reject Filtering", (10, 10))
