import cv2
import numpy as np

image = cv2.imread("images/musk.jpg")


#cv2.line(imagen, punto1, punto2, color, grosor, tipo de linea)
cv2.line(image, (0, 0), (280, 80), (0, 255, 0), thickness=3, lineType=cv2.LINE_AA);
#cv2.circle(imagen, centro, radio, color, grosor -1 es lleno, tipo de linea)
cv2.circle(image, (230, 180), 20, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA);
#cv2.elipse(imagen, centro, (ancho, alto), angulo, inicio, fin, color, grosor, tipo de linea)
cv2.ellipse(image, (290, 315), (80, 35), 0, 0, 360, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA);
#cv2.rectangle(imagen, punto1, punto2, color, grosor, tipo de linea)
cv2.rectangle(image, (310, 160), (380, 200), (255, 0, 255), thickness=5, lineType=cv2.LINE_8);
#cv2.putText(imagen, texto, punto, fuente, escala, color, grosor, tipo de linea)
cv2.putText(image, "Hola Mundo!", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 1.5, (250, 255, 255), 2, cv2.LINE_AA);

'''
cv2.LINE_8: Conectividad de 8, predeterminado, conexión diagonal y ortogonal.
cv2.LINE_4: Conectividad de 4, solo conexión ortogonal.
cv2.LINE_AA: Línea suavizada (anti-aliasing), líneas más suaves y estéticas.
'''
cv2.imshow("Original", image)

while True:
    c = cv2.waitKey(20)
    if c == 27:  # ESC key
        break

cv2.destroyAllWindows()