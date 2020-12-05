import cv2
import numpy as np
##
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
## add line
cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 4)
cv2.imshow("line_with_img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## rectangle
cv2.rectangle(img, (10, 10), (50, 50), (0, 0, 255), 2)
cv2.imshow("rectangle_with_img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## circle

cv2.circle(img, (200, 200), 50, (255, 0, 0), 3)
cv2.imshow("circle_with_img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## put text

cv2.putText(img, "image", (350, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 4)
cv2.imshow("text_with_img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
