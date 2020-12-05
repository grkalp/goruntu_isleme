import cv2
import numpy as np
import matplotlib.pyplot as plt

##

img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\img1.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

## threshold

_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.show()

## adaptive threshold  daha etkili bir çözüm

thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.show()


















