import cv2
import numpy as np

image = cv2.imread("images/musk.jpg")

x1, y1 = 100, 100  
x2, y2 = 400, 400  

height, width, _ = image.shape
crop = image[y1:y2, x1:x2]
resize=cv2.resize(crop,(width,height))

cv2.imshow("Original", image)
cv2.imshow("Crop", crop)
cv2.imshow("Expan", resize)
print(image.shape)
print(crop.shape)

while True:
    c = cv2.waitKey(20)
    if c == 27:  # ESC key
        break

cv2.destroyAllWindows()