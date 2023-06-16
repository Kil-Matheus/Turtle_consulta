import cv2
import numpy as np
from ultralytics import YOLO

# def Processamento():
#     imagem = cv2.imread("Trinca.jpg")
#     _, imagem = cv2.imencode('.jpg', imagem)
#     # _, imagem = imagem.split(',', 1)
#     model = YOLO("best.pt")
#     frame = cv2.imdecode(np.frombuffer(imagem, np.uint8), -1)
#     result = model.predict(frame, conf=0.5)
#     processed_img = result[0].plot()
#     processed_img = cv2.imencode('.jpg', processed_img)
    
#     return processed_img

# def main():
#     resultado = Processamento()
#     cv2.imshow(resultado)
#     return 0

# if __name__ == "__main__":
#     main()

import cv2
import numpy as np
from ultralytics import YOLO

def Processamento():
    imagem = cv2.imread("Trinca.jpg")
    model = YOLO("best.pt")
    frame = imagem
    result = model.predict(frame, conf=0.5)
    processed_img = result[0].plot()
    _, processed_img = cv2.imencode('.jpg', processed_img)
    
    return processed_img

def main():
    resultado = Processamento()
    img_decoded = cv2.imdecode(resultado, -1)
    cv2.imshow("Imagem processada", img_decoded)
    cv2.waitKey(0)
    
    return 0

if __name__ == "__main__":
    main()
