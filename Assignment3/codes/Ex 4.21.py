import cv2
import numpy
import matplotlib.pyplot as plt

original_image = cv2.imread("../images/Fig0459(a)(orig_chest_xray).png", flags=0)

# 进行FFT并将结果进行平移，以便更好地显示频谱和进行滤波
original_frq = numpy.fft.fft2(original_image)
centred_original_frq = numpy.fft.fftshift(original_frq)

# 构造高斯函数H（u，v）
rows, cols = original_image.shape  # rows cols分别得到图像的行数和列数
row_centre, col_centre = rows // 2, cols // 2  # 得到图像中心点的坐标（crow，cols）
D0 = 70
GHPF = numpy.zeros((rows, cols))
for u in range(rows):
    for v in range(cols):
        D2 = (u - row_centre) ** 2 + (v - col_centre) ** 2
        GHPF[u, v] = 1 - numpy.exp(-D2 / (2 * D0 * D0))
plt.imshow(GHPF,'gray')