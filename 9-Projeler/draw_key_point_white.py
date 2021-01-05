import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("C:\\Users\\alperh\\Desktop\\goruntu_isleme\\white_point.jpg", 0)
img = cv2.resize(img, (800, 600))
surf = cv2.xfeatures2d.SURF_create(48500)
kp, des = surf.detectAndCompute(img, None)
print(len(kp))

# img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
# plt.imshow(img2)
plt.imshow(img)
'''
DİJİTAL BASKI MAKİNASI DESENLERİNDE KEYPOINT TANIMLAMAK İÇİN KULLANILABİLİR Mİ? 

'''
##
new_img = img[220:400, 250:500]
# hsv = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)

# plt.figure()
# plt.imshow(hsv[:, 0:50])
# plt.show()
#
# plt.figure()
# plt.imshow(hsv[:, 50:100])
# plt.show()

plt.figure()
plt.hist(new_img[:, 0:50].ravel(), 256, [0, 256])
plt.show()

plt.figure()
plt.hist(new_img[:, 50:100].ravel(), 256, [0, 256], color="red")
plt.show()

# plt.figure()
# hist = cv2.calcHist([hsv[:, 0:50]], [0, 1], None, [180, 256], [0, 180, 0, 256])
# plt.imshow(hist, interpolation="nearest")
# plt.show()
#
# plt.figure()
# hist2 = cv2.calcHist([hsv[:, 50:100]], [0, 1], None, [180, 256], [0, 180, 0, 256])
# plt.imshow(hist2, interpolation="nearest")
# plt.show()