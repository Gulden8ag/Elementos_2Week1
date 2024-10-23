import cv2
import numpy as np



testImage1 = cv2.imread("images/musk.jpg")
cv2.imshow("Original", testImage1)

#Primer Prueba para revisar como guarda los datos de color
'''
testImage1_rgb = cv2.cvtColor(testImage1, cv2.COLOR_BGR2RGB)
testImage2_bgr = cv2.cvtColor(testImage1_rgb, cv2.COLOR_RGB2BGR)

cv2.imshow("Original", testImage1)
cv2.imshow("RGB", testImage1_rgb)
cv2.imshow("BGR", testImage2_bgr)
'''

#Segunda prueba donde modificamos los canales de color poniendolos en 0 eliminando el color
'''
testImage_no_blue = testImage1.copy()
testImage_no_blue[:, :, 0] = 0

testImage_no_red = testImage1.copy()
testImage_no_red[:, :, 2] = 0

testImage_no_green = testImage1.copy()
testImage_no_green[:, :, 1] = 0

testImage_no_green_noblue = testImage1.copy()
testImage_no_green_noblue[:, :, 1] = 0
testImage_no_green_noblue[:, :, 0] = 0

testImage_no_color = testImage1.copy()
testImage_no_color[:, :, 2] = 0
testImage_no_color[:, :, 1] = 0
testImage_no_color[:, :, 0] = 0

cv2.imshow("Original", testImage1)
cv2.imshow("Sin Azul", testImage_no_blue)
cv2.imshow("Sin Rojo", testImage_no_red)
cv2.imshow("Sin Verde", testImage_no_green)
cv2.imshow("Sin Verde ni azul", testImage_no_green_noblue)
cv2.imshow("No color", testImage_no_color)

'''

#Tercera prueba donde dividimos la imagen en 4 cuadrantes y eliminamos un color en cada cuadrante
'''
cuadrante= testImage1.copy()
height, width, _ = testImage1.shape
half_height = height // 2
half_width = width // 2

cuadrante[0:half_height, half_width:width, 1] = 0 
cuadrante[half_height:height, 0:half_width, 2] = 0  # Red channel = 0
cuadrante[half_height:height, half_width:width, 0] = 0  # Blue channel = 0
cv2.imshow("Cuadrante", cuadrante)
'''



while True:
    c = cv2.waitKey(20)
    if c == 27:
        break

cv2.destroyAllWindows()