import cv2
import numpy as np
import matplotlib.pyplot as plt


def gauss_noise(img, mean=0, stand_deviation=64):
    noise = np.random.normal(mean, stand_deviation, img.shape)
    return noise


def add_salt_and_pepper_noise(img, noise_ratio=0.5, salt_ratio=0.5, salt=255, pepper=0):
    noisy_img = img.copy()
    # calculate the number of pixels of total noise, salt noise and pepper noise
    noise_pxs = int(np.ceil(img.shape[0] * img.shape[1] * noise_ratio))
    salt_pxs = int(noise_pxs * salt_ratio)
    pepper_pxs = int(noise_pxs - salt_pxs)

    # generate noise
    salt_coords = [np.random.randint(0, i, salt_pxs) for i in img.shape]
    pepper_coords = [np.random.randint(0, i, pepper_pxs) for i in img.shape]
    noisy_img[salt_coords[0], salt_coords[1]] = salt
    noisy_img[pepper_coords[0], pepper_coords[1]] = pepper

    return noisy_img


def adaptive_median_filter(img, max_ksize=7, min_ksize=3):
    # noisy_img = img.copy()
    h, w = img.shape[:2]
    pad = int((max_ksize - 1) / 2)
    padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, borderType=cv2.BORDER_REFLECT_101)
    filtered = np.empty((h, w))
    z_min = 0
    z_max = 0
    z_med = 0
    z_xy = 0

    def stageA(current_ksize):
        nonlocal z_min, z_max, z_med, z_xy, x, y
        current_margins = int((current_ksize - 1) / 2)
        kernel = padded[x - current_margins:x + current_margins + 1, y - current_margins:y + current_margins + 1]
        z_min = np.min(kernel)
        z_max = np.max(kernel)
        z_med = np.median(kernel)
        z_xy = padded[x, y]

        A1 = z_med - z_min
        A2 = z_med - z_max
        if A1 > 0 > A2:
            return stageB()
        else:
            current_ksize += 2
            if current_ksize <= max_ksize:
                return stageA(current_ksize)
            else:
                return z_med

    def stageB():
        nonlocal z_min, z_max, z_med, z_xy
        B1 = z_xy.astype(np.float64) - z_min.astype(np.float64)
        B2 = z_xy.astype(np.float64) - z_max.astype(np.float64)
        if B1 > 0 > B2:
            return z_xy
        else:
            return z_med

    for x in range(pad, pad + h):
        for y in range(pad, pad + w):
            filtered[x - pad, y - pad] = stageA(min_ksize)
    return filtered


original_img = cv2.imread('../images/FigP0438(a).tif', 0)

gauss_noisy_img = original_img + gauss_noise(original_img)
salt_and_pepper_noisy_img = add_salt_and_pepper_noise(original_img)

filtered_gauss_img = adaptive_median_filter(gauss_noisy_img)
filtered_salt_and_pepper_img = adaptive_median_filter(salt_and_pepper_noisy_img)

plt.figure("AMF",figsize=(10, 6))
plt.subplot(131)
plt.imshow(original_img, 'gray'), plt.title("Original"), plt.axis('off')
plt.subplot(232)
plt.imshow(gauss_noisy_img, 'gray'), plt.title("Gaussian noised\n($\mu=0,\sigma=64$)"), plt.axis('off')
plt.subplot(233)
plt.imshow(filtered_gauss_img, 'gray'), plt.title("Adaptive denoised\n(Gaussian)"), plt.axis('off')
plt.subplot(235)
plt.imshow(salt_and_pepper_noisy_img, 'gray'), plt.title("Salt & pepper noised\n($p_a=p_b=0.25$)"), plt.axis('off')
plt.subplot(236)
plt.imshow(filtered_salt_and_pepper_img, 'gray'), plt.title("Adaptive denoised\n(salt & pepper)"), plt.axis('off')
plt.suptitle("Adaptive Mean Filter with $S_{max} = 7$")
plt.tight_layout()
plt.show()
