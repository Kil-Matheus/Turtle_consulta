import cv2
import numpy as np

image = cv2.imread("maxresdefault.jpg")
image_2 = cv2.resize(image, (800, 400))

#Kernel customizado
kernel = np.array([[0, -1, 0],
                   [-1, 42, -1],
                   [0, -1, 0]], dtype=np.float32)

#Aplicando o filtro
image_filter = cv2.filter2D(image, -1, kernel)
image_filter_2 = cv2.resize(image_filter, (800, 400))

#Plotando as imagens
cv2.imshow("Naruto-kun-filtrado", image_filter_2)
cv2.imshow("Naruto-kun", image_2)

#Exibir imagem
cv2.waitKey(0)
cv2.destroyAllWindows()
