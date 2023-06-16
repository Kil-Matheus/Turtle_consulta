import cv2

#Recebendo Imagem
image = cv2.imread("maxresdefault.jpg")

#Mexendo na escala da imagem (Largura, Altura) especifica a escala
scale_img_pixel = cv2.resize(image, (800, 400))

#Mexendo na escala da imagem por uma porcentagem
scale_img_porc = cv2.resize(image, None, fx=0.5, fy=0.5)

#Plotando as imagens
scale_img_pixel = cv2.imshow("Naruto-kun", scale_img_pixel)

# scale_img_porc = cv2.imshow("Naruto-kun", scale_img_porc)

cv2.waitKey(0)
cv2.destroyAllWindows()