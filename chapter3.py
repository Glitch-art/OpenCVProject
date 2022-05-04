"""
TITLE: Resizing and cropping (cambio de tamaño y recortando)
"""
import cv2

img = cv2.imread("Resources/butterfly.jpg")
print(img.shape)    # Height, Width, chanelsBGR

imgResize = cv2.resize(img, (300,200))
print(imgResize.shape)

imgCropped = img[0:200, 100:300]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)