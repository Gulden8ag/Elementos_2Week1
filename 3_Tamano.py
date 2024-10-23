import cv2
import numpy as np

image = cv2.imread("images/musk.jpg")

x1, y1 = 100, 100  
x2, y2 = 400, 400  
#Se obtiene la altura y el ancho de la imagen
height, width, _ = image.shape
#Se recorta la imagen segun las coordenadas de un cuadrado
crop = image[y1:y2, x1:x2]
#Se expande la imagen recortada a la altura y ancho de la imagen original
resize=cv2.resize(crop,(width,height))

#Se muestra la imagen original, la imagen recortada y la imagen expandida
cv2.imshow("Original", image)
cv2.imshow("Crop", crop)
cv2.imshow("Expan", resize)
#Se imprime la forma de la imagen original y la imagen recortada
print(image.shape)
print(crop.shape)

while True:
    c = cv2.waitKey(20)
    if c == 27:  # ESC key
        break

cv2.destroyAllWindows()