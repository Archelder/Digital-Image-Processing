import cv2
import matplotlib.pyplot as plt

original_img = cv2.imread("../images/FigP1036.png", 0)
thresholded_img = cv2.threshold(original_img, 60, 255, cv2.THRESH_OTSU)[1]

plt.figure(figsize=(8, 6))
plt.subplot(221), plt.imshow(original_img, 'gray'), plt.title("original")

plt.subplot(222), plt.imshow(thresholded_img, 'gray'), plt.title("thresholded")

plt.subplot(212), plt.hist(original_img.flatten(), 256, [0, 255], log=True)
plt.tight_layout()

# save
# output = f'../images/Thresholding segment.jpg'
# plt.savefig(output)

plt.show()
