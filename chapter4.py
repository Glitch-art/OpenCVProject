"""
TITLE: Shapes and text
"""
import cv2
import numpy as np

# img = np.zeros((512, 512))      # Matriz de ceros
img = np.zeros((512, 512, 3), np.uint8)      # Matriz de ceros com 3 canalesRGB
#print(img.shape)

# Fondo azul
img[:] = 250,0,0

# paralelogramo Rojo
img[100:200,200:400] = 0,0,255

# Linea Verde
cv2.line(img,(0,0),(300,300),(0,255,0),3)
#Syntax: cv2.line(image, start_point, end_point, color, thickness)

# Rectangulo naranja
cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(0,128,255),2)

# Circulo morado
cv2.circle(img,(400,50),30,(164,73,163),5)

# Texto negro
cv2.putText(img," El Proyecto ",(100,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)

cv2.imshow("Image", img)
cv2.waitKey(0)

