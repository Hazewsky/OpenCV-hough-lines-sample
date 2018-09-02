import cv2
import numpy as np
num = input("Type 0 or 1 to show image \n")
print(num)
path = "images/sample{}.jpg"

img = cv2.imread(path.format(num))
kernelSize = 5
kernel = np.ones((5,5),np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
blur_gray = cv2.GaussianBlur(gray,(kernelSize,kernelSize),0)
ret,thresh = cv2.threshold(hsv, 230,255, cv2.THRESH_BINARY)
thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
#cv2.imshow("",thresh)
range = cv2.inRange(thresh, (0,0,127),(0,0,255))
edges = cv2.Canny(range, 100, 300,apertureSize=3, L2gradient=True)
#cv2.imshow("edge",edges)
closed = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel)
#cv2.imshow("closed",closed)
minLLength = 100
maxLGap = 15
lines = cv2.HoughLinesP(closed, 1, np.pi/180, 100, minLineLength=minLLength, maxLineGap=maxLGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1, y1),(x2, y2),(127,255,127),2)
cv2.imshow("lines", img)
cv2.imwrite("output.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
