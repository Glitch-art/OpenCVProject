"""
TITLE: Read images-videos-webcam
"""

import cv2

print("Package Imported")

# Imagen
'''
img = cv2.imread("Resources/lena.png")

cv2.imshow("Output", img)
cv2.waitKey(5000)
'''

# Video
'''
cap = cv2.VideoCapture("Resources/Megamind.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
'''

# Webcam

cap = cv2.VideoCapture(0)
cap.set(3, 1024)  # Ancho
cap.set(4, 640)  # Alto
cap.set(10, 100)  # Brillo

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
