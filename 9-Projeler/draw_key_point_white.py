import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("C:\\Users\\alperh\\Desktop\\goruntu_isleme\\penta.jpg",0)
# img = cv2.resize(img, (800, 600))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
# new_img = img[220:400, 250:500]
# hsv = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)

# plt.figure()
# plt.imshow(hsv[:, 0:50])
# plt.show()
#
# plt.figure()
# plt.imshow(hsv[:, 50:100])
# plt.show()

plt.figure()
plt.hist(img[2000:3000, 500:1000].ravel(), 256, [0, 256])
# plt.show()
#
# plt.figure()
plt.hist(img[2000:3000, 2000:2500].ravel(), 256, [0, 256], color="red")
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

##
plt.figure()
plt.imshow(img[2000:3000, 2000:2500])
plt.show()

plt.figure()
plt.imshow(img[2000:3000, 500:1000])
plt.show()


##

diff = cv2.subtract(img[2000:3000, 2000:2500], img[2000:3000, 500:1000])
plt.figure()
plt.imshow(diff)
plt.show()

##

a = img[2000:3000, 2000:2500].ravel()
print(np.std(a), np.mean(a))

b = img[2000:3000, 500:1000].ravel()
print(np.std(b), np.mean(b))

##
# import pandas as pd
#
# df = pd.DataFrame(zip(a, b),columns=["a", "b"])
# df.to_csv("deneme.csv")
## normality test
from scipy.stats import anderson, anderson_ksamp
from scipy import stats
# normality test
result = anderson(b)
print('Statistic: %.3f' % result.statistic)
p = 0
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < result.critical_values[i]:
		print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	else:
		print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))

print(stats.ttest_ind(a, b))