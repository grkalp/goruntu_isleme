import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

## read image
img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\sudoku.jpg", 0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.title("original")
plt.show()

## X Gradyan
sobelx = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)
plt.figure()
plt.imshow(sobelx, cmap="gray")
plt.title("sobelx")
plt.show()

## Y Gradyan
sobely = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure()
plt.imshow(sobely, cmap="gray")
plt.title("sobely")
plt.show()

## laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap="gray")
plt.title("laplacian")
plt.show()