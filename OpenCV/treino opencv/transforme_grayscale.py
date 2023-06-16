import cv2

#Recebendo a imagem
image = cv2.imread('maxresdefault.jpg')

#Transformando a imagem em escala de cinza
img_cinzas = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Plotando as imagens
cv2.imshow("Naruto_black_white", img_cinzas)
cv2.imshow("Naturo-kun", image)

#Esperando o usuário apertar alguma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()