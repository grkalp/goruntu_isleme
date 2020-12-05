import cv2

##
img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\lenna.png")

## resize
print("image_dimension:", img.shape)
img_resized = cv2.resize(img, (800, 800))
cv2.imshow("original", img)
cv2.imshow("resized", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

## crop

img_crop = img[:200, 0:300]         # yukseklik + genislik opencv de ters ilk önce yükseklik geliyor
cv2.imshow("cropped", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
