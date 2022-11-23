import cv2
import numpy as np

## Read
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()


    ## convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    mask = cv2.inRange(hsv, (36, 25, 25), (86, 255, 255))
    #mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

    ## slice the green
    imask = mask>0
    green = np.zeros_like(frame, np.uint8)
    green[imask] = frame[imask]

    ## save
    cv2.imshow("Image INPUT", frame)
    cv2.imshow("Image", green)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destoryAllWindows()