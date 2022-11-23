import cv2
import numpy as np

count = 0
## Read
img = cv2.imread("sample1.png")

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
mask = cv2.inRange(hsv, (0, 0, 0), (180, 255, 55))
##mask = cv2.inRange(hsv, (36, 45, 25), (86, 255, 255))   #for green
'''mask1 = cv2.inRange(hsv, (5, 45, 25), (20, 255, 255))  #for red
mask2 = cv2.inRange(hsv, (165, 45, 25), (180, 255, 255))
mask = mask1 + mask2'''
# mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

## slice the green
imask = mask > 0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

#dilation
kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(green, kernel, iterations=2)
dilate = cv2.dilate(erosion, kernel, iterations=2)

#Edge Detection
canny = cv2.Canny(dilate, 200, 300)

#Contour Drawing
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours2, heirarchy2 = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours2:
    (x, y, h, w) = cv2.boundingRect(contour)
    if cv2.contourArea(contour) < 100:
        continue
    cv2.rectangle(green, (x, y), (x+w, y+h), (0, 0, 255), 1)
    count = count + 1


final = cv2.drawContours(green, contours, -1, (0, 0, 255), 1)
print(count)

cv2.imshow("Image INPUT", img)
cv2.imshow("Image", green)
#cv2.imshow("Dilated", dilate)
cv2.imshow("Edge Detection", canny)
cv2.imshow("Final Product", final)
cv2.waitKey()
cv2.destroyAllWindows()

