# import libraries
import cv2
import time
##
cap = cv2.VideoCapture("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\MOT17-04-DPM.mp4")
print("genislik:", cap.get(3))
print("yukseklik:", cap.get(4))
## video yuklendi mi ?
if cap.isOpened() == False:
    print("video yuklenmedi")
else:
    print("video yuklendi")
## video okuma ve görüntüleme

while True:
    ret, frame = cap.read()
    if ret == True:
        time.sleep(0.01)
        cv2.imshow("video", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
