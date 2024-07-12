import cv2
import numpy as np
from time import gmtime, strftime
import math
import datetime
import time
global secss
global xx
global yy
global xxx
global yyy
secss=-1
xx=15
yy=15
xxx=5
yyy=5
#pip install opencv-python
def draw_grid(frame, grid_size):
    global secss
    global xx
    global yy
    global xxx
    global yyy
    dt = datetime.datetime.now()
    mseconds=dt.microsecond / 1000
    if secss==-1:
        secss=mseconds
    mm=abs(mseconds-secss)
    
    if mm > 50:
        secss=mseconds
        xx=xx+xxx
        yy=yy+yyy
        if xx> 610:
            xxx=-xxx
        if yy > 450:
            yyy=-yyy
        if yy<15:
            yyy=-yyy
        if xx<15:
            xxx=-xxx


    cv2.ellipse(frame, (xx, yy),(15,15),0, 0,360,(255,255,255), 2)


   
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

