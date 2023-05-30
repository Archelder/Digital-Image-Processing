import cv2
import numpy as np
import matplotlib.pyplot as plt

original_img = cv2.imread('../images/Figp0917.png')

# create a circle structure element with radius 15
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))

A = original_img
B = se
# erode A by B using function `cv2.erode()`
C = cv2.erode(A, B)
# dilate C by B using function `cv2.dilate()`
D = cv2.dilate(C, B)
# dilate D by B
E = cv2.dilate(D, B)
# erode E by B
F = cv2.erode(E, B)

# display the results
disp_img = [A, B, C, D, E, F]
disp_cap = ["A: original image", "B: structure element", "$C=A\ominus B$", "$D&=C\oplus B$\n&=A\circ B",
            "$E=D\oplus B$", "$F=E\ominus B$"]

