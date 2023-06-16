import cv2

image = cv2.imread("maxresdefault.jpg")

#Rotacionar a imagem
rotate_img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
scale_rotate = cv2.resize(rotate_img, (800, 400))

#Espelhar a imagem
mirror_img = cv2.flip(image, 1)
scale_mirror = cv2.resize(mirror_img, (800,400))

#Plotando as imagens
cv2.imshow("Naruto-kun", scale_rotate)
cv2.imshow("Naruto-kun_contrario", scale_mirror)

#Esperando o usuário apertar alguma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()