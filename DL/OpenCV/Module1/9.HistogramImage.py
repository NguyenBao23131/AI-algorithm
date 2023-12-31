import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("D:/2-bai tap cua dev/PythonAI/AI/DL/OpenCV/Module1/img/img5.jpg", cv.IMREAD_GRAYSCALE)

# -> TestCase1
# hist = cv.calcHist([img], [0], None, [256], [0,256])
# assert img is not None, "file could not be read, check with os.path.exists()"
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])


# ->testCase2
# tinh toan histogram cua anh
hist,bins = np.histogram(img.flatten(),256,[0,256])

# tinh toan can mau
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

# mask
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]

# show ra hinh can bang
plt.plot(img2, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

plt.show()


