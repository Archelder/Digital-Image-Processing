import cv2
import matplotlib.pyplot as plot

shaded_img = cv2.imread(
    'images/Fig0229(a)(tungsten_filament_shaded).png',
    flags=0)
shading_pattern = cv2.imread(
    'images/Fig0229(b)(tungsten_sensor_shading).png',
    flags=0)

product_img = cv2.multiply(shaded_img, shading_pattern, scale=256)  # 乘法
quotient_img = cv2.divide(shaded_img, shading_pattern, scale=256)  # 除法

# 绘图
plot.subplot(132), plot.imshow(shaded_img, cmap='gray'), plot.title('shaded_img'), plot.axis('off')  # 原始图像
plot.subplot(131), plot.imshow(product_img, cmap='gray'), plot.title('product_img'), plot.axis('off')  # 乘法结果
plot.subplot(133), plot.imshow(quotient_img, cmap='gray'), plot.title('quotient_img'), plot.axis('off')  # 除法结果
plot.show()
