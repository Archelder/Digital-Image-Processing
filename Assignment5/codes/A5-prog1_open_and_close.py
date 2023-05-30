import cv2
import numpy as np
import matplotlib.pyplot as plt

original_img = cv2.imread('../images/Figp0917.png', 0)

# create a circle structure element with radius 15
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (32, 32))

A = original_img
B = se.copy()
# erode A by B using function `cv2.erode()`
C = cv2.erode(A, B)
# dilate C by B using function `cv2.dilate()`
D = cv2.dilate(C, B)
# dilate D by B
E = cv2.dilate(D, B)
# erode E by B
F = cv2.erode(E, B)

# display the results
B = np.zeros(original_img.shape)
h, w = B.shape[:2]
sh, sw = se.shape[:2]
y = int((h - sh) / 2)
x = int((w - sw) / 2)
B[y:y + sh, x:x + sw] = se

disp_img = [A, B, C, D, E, F]
disp_cap = ["A: original image", "B: structure element", "$C=A\ominus B$", "$D=C\oplus B$\n$(D=A\circ B)$",
            "$E=D\oplus B$", "$F=E\ominus B$\n" + r"$(F=D\bullet B)$"]

fig, axs = plt.subplots(2, 3, figsize=(10, 8))
for i in range(len(disp_img)):
    ax = axs.flat[i]
    ax.imshow(disp_img[i], 'gray')
    ax.set_title(disp_cap[i])
    ax.set_xticks([])
    ax.set_yticks([])
plt.suptitle("Erosion, Dilation, Opening and Closing")
# plt.tight_layout()
plt.show()
