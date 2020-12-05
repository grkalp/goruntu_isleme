import cv2
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")
## read image
img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\datai_team.jpg", 0)
plt.figure()
plt.imshow(img, cmap="gray"), plt.axis("off")
plt.title("original")
plt.show()

'''
5 adet morfolojik işlem var. 
1- erode --> erozyon
2- dilation --> genişleme
3- opening --> açılma
4- closing --> kapatma
5- gradient --> erozyon ile genişlemenin farkını alıyoruz --  kısaca ilkel edge detection yapmak
'''
## erode (erozyon)
kernel = np.ones((5, 5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations=1)
plt.figure()
plt.imshow(result, cmap="gray"), plt.axis("off")
plt.title("erode")
plt.show()
## genişleme dilation  --> reverse of the erode
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure()
plt.imshow(result2, cmap="gray"), plt.axis("off")
plt.title("dilation")
plt.show()
## opening (açılma) --> beyaz noktaları temizlemek için kullanırız genel olarak
# ilk olarak resim üzerine beyaz noktalardan gürültü ekleyelim

white_noise = np.random.randint(0, 2, size=img.shape[:2])
white_noise = white_noise * 255
white_noise_img = white_noise + img
plt.figure()
plt.imshow(white_noise_img, cmap="gray"), plt.axis("off")
plt.title("white_noise with image")
plt.show()

# opening
opening = cv2.morphologyEx(white_noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening, cmap="gray"), plt.axis("off")
plt.title("opening with image")
plt.show()

## closing (kapatma) --> siyah noktaları temizlemek için kullanırız genel olarak
# ilk olarak resim üzerine siyah noktalardan gürültü ekleyelim

black_noise = np.random.randint(0, 2, size=img.shape[:2])
black_noise = black_noise * -255
black_noise_img = black_noise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure()
plt.imshow(black_noise_img, cmap="gray"), plt.axis("off")
plt.title("black_noise with image")
plt.show()

# closing
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing, cmap="gray"), plt.axis("off")
plt.title("closing with image")
plt.show()

## gradient

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient, cmap="gray"), plt.axis("off")
plt.title("gradient with image")
plt.show()

