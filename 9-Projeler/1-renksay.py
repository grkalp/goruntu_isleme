import cv2
import numpy as np

# alt_Renk = np.array([30, 60, 60])
# ust_Renk = np.array([64, 255, 255])
# RENK = 'YESIL'

# alt_Renk = (10, 100, 100)
# ust_Renk = (40, 255, 255)
# RENK = 'SARI'

alt_Renk = (170, 100, 100)
ust_Renk = (190, 255, 255)
RENK = 'KIRMIZI'

# alt_Renk = (75, 100, 100)
# ust_Renk = (130, 255, 255)
# RENK = 'Mavi'

kamera = cv2.VideoCapture(0)
cember = True

while True:
    if not kamera.isOpened():
        break
    _, kare = kamera.read()
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)
    maske = cv2.inRange(hsv, alt_Renk, ust_Renk)
    kernel = np.ones((5, 5), dtype='int')
    maske = cv2.dilate(maske, kernel)
    # res = cv2.bitwise_and(kare, kare, mask=maske)
    _, konturlar, _ = cv2.findContours(maske.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    say = 0
    for kontur in konturlar:
        alan = cv2.contourArea(kontur)
        if alan > 600:
            say += 1
            (x, y, w, h) = cv2.boundingRect(kontur)
            cv2.rectangle(kare, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if cember:
                (x, y), ycap = cv2.minEnclosingCircle(kontur)
                merkez = (int(x), int(y))
                ycap = int(ycap)
                img = cv2.circle(kare, merkez, ycap, (255, 0, 0), 2)
    if say > 0:
        cv2.putText(kare, f"{say} {RENK} nesne bulundu", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

    cv2.imshow("kare", kare)
    k = cv2.waitKey(4) & 0xFF
    if k == 27:
        break
if kamera.isOpened():
    kamera.release()
cv2.destroyAllWindows()


