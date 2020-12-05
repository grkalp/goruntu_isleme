import cv2
import numpy as np
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings("ignore")
## read image
img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.title("org")
plt.show()
## blurring (detayı azaltır, gürültüyü engeller)
# 1 - ortalama bulanıklaştırma yöntemi
dst2 = cv2.blur(img, ksize=(3, 3))
plt.figure()
plt.imshow(dst2)
plt.title("Ortalama Blur")
plt.show()
## gaussian blur
gb = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.title("Gaussian Blur")
plt.show()
## median blur
mb = cv2.medianBlur(img, ksize=3)
plt.figure()
plt.imshow(mb)
plt.title("Median Blur")
plt.show()

## create gaussian noise and add existing image but you have to do normalize this image before adding

def gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5

    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = gauss + image
    return noisy


# we read image again
img2 = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\NYC.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) / 255  # normalize

gaussian_noise_image = gaussian_noise(img2)
plt.figure()
plt.imshow(gaussian_noise_image)
plt.title("gaussian_noise_image")
plt.show()

# we want to decrease noisy on image we can use gaussian blur method

gb2 = cv2.GaussianBlur(gaussian_noise_image, (3, 3), sigmaX=7)
plt.figure()
plt.imshow(gb2)
plt.title("gaussian_noise_image_blur")
plt.show()


## tuz, karabiber gürültüsü oluşturup median blur ile azaltmaya çalışalım

def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.4

    amount = 0.004
    noisy = np.copy(image)

    # salt white
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    # pepper black
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0

    return noisy

sp_image = saltPepperNoise(img)
plt.figure()
plt.imshow(sp_image), plt.title("salt_and_pepper"), plt.show()

# median blur
mb2 = cv2.medianBlur(sp_image, ksize=3)
plt.figure()
plt.imshow(mb)
plt.title("Median Blur with sp_image")
plt.show()
