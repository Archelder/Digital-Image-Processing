import cv2
import matplotlib.pyplot as plt
import numpy as np

# open
original_image = cv2.imread("../images/FigP0501.png", flags=0)
image_height=original_image.shape[0]
image_width=original_image.shape[1]

def Harmonic(m):
    order=m*m
    kernalMean=np.ones((m,m),np.float32)
    hPad=int((m-1)/2)
    wPad=int((m-1)/2)
    imgPad=np.pad(original_image.copy(),((hPad,m-hPad-1),(wPad,m-wPad-1)),mode="edge")
    elsilon=1e-8
    imgHarMean=original_image.copy()
    for i in range(hPad,image_height+hPad):
        for j in range(wPad,image_width+wPad):
            sumTemp=np.sum(1.0/(imgPad[i-hPad:i+hPad+1,j-wPad:j+wPad+1]+elsilon))
            imgHarMean[i-hPad][j-wPad]=order/sumTemp
    return imgHarMean

size = [3, 7, 9]

target_image = []
for i in size:
    target_image.append(Harmonic(i))

# show
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(10, 4))

ax = axs[0]
ax.imshow(original_image, cmap='gray')
ax.set_title(f"original image")
ax.set_xticks([])
ax.set_yticks([])

for i in range(3):
    ax = axs[i + 1]
    ax.imshow(target_image[i], cmap='gray')
    ax.set_title(fr"${size[i]}\times${size[i]}")
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Running Results of Harmonic Mean Filtering")

plt.tight_layout()

plt.show()
