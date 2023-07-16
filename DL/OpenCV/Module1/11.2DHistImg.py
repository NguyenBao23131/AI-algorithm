import numpy as np
import cv2 as cv
img = cv.imread('D:/2-bai tap cua dev/PythonAI/AI/DL/OpenCV/Module1/img/img6.jpg')

assert img is not None, "file could not be read, check with os.path.exists()"

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv.imshow("test", hist)
cv.waitKey(0)
cv.destroyAllWindows()
