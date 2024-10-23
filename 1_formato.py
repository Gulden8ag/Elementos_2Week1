import cv2
import numpy as np



testImage1 = cv2.imread("images/zero.jpg")


print(testImage1)
print("image dimension ={}".format(testImage1.shape))


height, width, _ = testImage1.shape

print("height ={}, width ={}".format(height, width))

'''
La imagen en este caso tiene 3 dimensiones. La tercera dimensión indica el número de canales en una imagen.
 Para la mayoría de las imágenes, este número es 3 (es decir, R, G, B). 
 En algunos casos, puede haber un canal adicional (llamado canal alfa) que contiene la información de transparencia 
 de los píxeles;

 Por ejemplo el arreglo {0,0,0} indica el pixel en la pos0,0 y el tercer valor es el canal de color que al ser 0 indica el canal azul
'''

cv2.destroyAllWindows()