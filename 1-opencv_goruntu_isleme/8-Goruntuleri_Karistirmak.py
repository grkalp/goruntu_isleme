import cv2
import numpy as np
import matplotlib.pyplot as plt
## opencv default olarak BGR formatında resimleri okuyor. Biz şimdi RGB formatına dönüştürelim

img1 = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\img1.JPG")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\img2.JPG")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
##
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

## birleştirme yaparken aynı boyutta olmak zorundalar

print(img1.shape)
print(img2.shape)
# boyutları farklı

img1 = cv2.resize(img1, (600, 600))
img2 = cv2.resize(img2, (600, 600))

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

## karıştırılmış resim = alpha*img1 + beta*img2

blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)







