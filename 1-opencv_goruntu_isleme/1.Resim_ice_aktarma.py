# import libraries
import cv2

## import the image
img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\messi5.jpg", 0)
cv2.imshow("den", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
