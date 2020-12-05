import cv2
import numpy as np
##
img = cv2.imread("C:\\Users\\alperh\\PycharmProjects\\goruntu_isleme\\1-opencv_goruntu_isleme\\kart.png")
cv2.imshow("kart", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
##
width = 400
height = 500

'''
Nihai resim pikselleri için öncesinde genişlik ve yükselik değerlerini yukarıda belirledik. Herhangi bir kuralı yok.
Resim boyutuna göre belirleyebiliriz.
Dönüştürmek istediğimiz resimin köşelerinin piksel değerlerini bir matris içerisinde depoluyoruz. paint ile baktık
nihai olmasını istediğimiz piksel değerlerini de bir matris içerisinde depoladık.
dönüştürme matrisini oluşturduk ve sonrasında dönüştürme işlemini uyguladık.
'''

pts1 = np.float32([[203, 1], [1, 472], [540, 150], [338, 617]])
pts2 = np.float32([[0, 0], [0, height], [width, 0], [width, height]])
    
matrix = cv2.getPerspectiveTransform(pts1, pts2)

img_output = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("nihai_resim", img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()


