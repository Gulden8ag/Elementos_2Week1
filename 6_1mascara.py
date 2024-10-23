import cv2
import numpy as np

image = cv2.imread("images/musk.jpg")


#mascara simple

# Crear una máscara de un solo canal del tamaño de la imagen
mask1 = np.zeros(image.shape[:2], dtype=np.uint8)
'''
En python el ':' se utiliza para indicar un rango o un corte dentro de una secuencia
la sintaxis completa seria [start:stop] si no se especifica el start se toma como 0 y 
si no se especifica el stop se toma como el tamaño de la secuencia

dtype indica el tipo de dato que se almacenara en la matriz, en este caso es un entero sin signo de 8 bits es
decir un valor entre 0 y 255 perfecto para una mascara binaria o escala de grises
'''
# Definir un área en la máscara 
mask1[50:200, 170:320] = 255

cv2.imshow("Original", image)
cv2.imshow("Mask1", mask1)


#mascara en rango de colores

mask2 = cv2.inRange(image, (0,0,0), (255,100,100))

cv2.imshow("Original", image)
#cv2.imshow("Mask2", mask2)

'''
src1: Primera imagen o matriz de entrada.
src2: Segunda imagen o matriz de entrada. En este caso, es la misma que src1 (es decir, image).
dst: (Opcional) Salida en la que se guardará el resultado. Si no se especifica, se crea una nueva imagen de salida.
mask: (Opcional) Una máscara opcional. Si se proporciona, la operación se aplicará solo a los píxeles donde la máscara tenga un valor diferente de 0.
'''
result = cv2.bitwise_and(image, image, mask=mask1)
#result = cv2.bitwise_and(image, image, mask=mask2)

cv2.imshow("AND", result)

while True:
    c = cv2.waitKey(20)
    if c == 27:  # ESC key
        break
    
cv2.destroyAllWindows()