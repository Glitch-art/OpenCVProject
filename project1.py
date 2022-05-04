""""
TITLE: Virtual Painting
"""

import cv2
import numpy as np
import ExtraCode

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)  # Ancho
# cap.set(4, frameHeight)  # Alto
cap.set(10, 95)  # Brillo

myColors = [[17, 30, 64, 192, 130, 255],    # Yellow
            [110, 167, 29, 255, 139, 255],  # Purple
            [100, 126, 82, 220, 80, 255]]   # Blue


def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for value, color in enumerate(myColors):
        lower = np.array([color[0], color[2], color[4]])     # h_min, s_min, v_min
        upper = np.array([color[1], color[3], color[5]])     # h_max, s_max, v_max
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow("Color #" + str(value + 1), mask)


while True:
    success, img = cap.read()
    findColor(img, myColors)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
