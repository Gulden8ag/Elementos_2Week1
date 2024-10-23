import cv2
import numpy as np

# Crear dos imágenes haciendo una matriz de ceros de 300x300 con valores de 8 bits 0-255
image1 = np.zeros((300, 300), dtype="uint8")
image2 = np.zeros((300, 300), dtype="uint8")

# Dibuja un rectángulo blanco en la imagen1 y un círculo blanco en la imagen2
cv2.rectangle(image1, (50, 50), (250, 250), 255, -1)  # rectángulo blanco en image1
cv2.circle(image2, (150, 150), 100, 255, -1)  # circulo blanco en image2

# Ejemplos de operacion bitwise
bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_xor = cv2.bitwise_xor(image1, image2)
bitwise_not_image1 = cv2.bitwise_not(image1)
bitwise_not_image2 = cv2.bitwise_not(image2)

# Mostar las imágenes
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.imshow('Bitwise NOT (Image 1)', bitwise_not_image1)
cv2.imshow('Bitwise NOT (Image 2)', bitwise_not_image2)

# Wait for a key press and close all windows
while True:
    c = cv2.waitKey(20)
    if c == 27:  # ESC key
        break
cv2.destroyAllWindows()
