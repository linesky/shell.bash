import cv2
import numpy as np
from time import gmtime, strftime
import math
import time
import datetime
global secss
global xx
global yy
global xxx
global yyy
secss=-1
xx=600
yy=58
xxx=-5
yyy=-5
#pip install opencv-python
def draw_grid(frame, grid_size):
    global secss
    global xx
    global yy
    global xxx
    global yyy
    text="Virtual Reality Scroll...."
    dt = datetime.datetime.now()
    mseconds=dt.microsecond / 1000
    if secss==-1:
        secss=mseconds
    mm=abs(mseconds-secss)
    l=-(len(text)*12)
    
    if mm > 50:
        secss=mseconds
        xx=xx+xxx
        
        if xx< l:
            xx=640
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (xx, yy)
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2
    cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)     


    


   
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

