import cv2
import numpy as np

img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\lenna.png")
cv2.imshow("org", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
## yatay birleştirme
hor = np.hstack((img, img))
cv2.imshow("horizontal", hor)
cv2.waitKey(0)
cv2.destroyAllWindows()

## dikey birleştirme
ver = np.vstack((img, img))
cv2.imshow("vertical", ver)
cv2.waitKey(0)
cv2.destroyAllWindows()