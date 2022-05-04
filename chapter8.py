"""
TITLE: Contours / shape detections
"""

from ExtraCode import stackImages
import cv2
import numpy as np


def empty(a):
    pass


def defineGeometricFigure(objCorners, w, h):
    if objCorners == 3 : objectType = "Triangulo"
    elif objCorners == 4 :
        aspectRatio = w/float(h)
        if aspectRatio > 0.95 and aspectRatio < 1.05 : objectType = "Cuadrado"
        else : objectType = "Rectangulo"
    elif objCorners > 4 : objectType = "Circulo"
    else : objectType = "None"

    return objectType


def getCountours(img, valor):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for count, cnt in enumerate(contours):
        print("contour N°: " + str(count + 1))
        area = cv2.contourArea(cnt)
        print("area: " + str(area))
        if area > valor:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print("perímetro: " + str(peri))
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCorners = len(approx)
            print(objCorners)
            x, y, w, h = cv2.boundingRect(approx)
            objectType = defineGeometricFigure(objCorners, w, h)
            print(objectType)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0))
            cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.6,
                        (0, 0, 0), 2)


path = 'Resources/shapes.png'

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 800, 40)
cv2.createTrackbar("Area", "TrackBars", 0, 12000, empty)

while True:
    img = cv2.imread(path)
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    valor = cv2.getTrackbarPos("Area", "TrackBars")
    getCountours(imgCanny, valor)

    imgBlank = np.zeros_like(img)
    imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
                                 [imgCanny, imgContour, imgBlank]))
    cv2.imshow("Stack", imgStack)

    cv2.waitKey(1)
