import cv2
import numpy as np
from time import gmtime, strftime
#pip install opencv-python
def draw_grid(frame, grid_size):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 50)
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2
    cv2.putText(frame, str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())), org, font, fontScale, color, thickness, cv2.LINE_AA) 

    

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    grid_size = 16

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)

        # Desenhar a grade
        draw_grid(frame, grid_size)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality Grid', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

