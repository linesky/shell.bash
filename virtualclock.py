import cv2
import numpy as np
from time import gmtime, strftime
import math
import time
#pip install opencv-python
def draw_grid(frame, grid_size):

    cv2.ellipse(frame, (200, 200),(100,100),0, 0,360,(255,255,255), 2)

    for i in range(12):
        angle = math.pi / 6 * i
        x_start = 200 + 100 * 0.8 * math.sin(angle)
        y_start = 200 - 100 * 0.8 * math.cos(angle)
        x_end = 200 + 100 * 0.9 * math.sin(angle)
        y_end = 200 - 100 * 0.9 * math.cos(angle)
        cv2.line(frame,(int(x_start),int(y_start)), (int(x_end), int(y_end)),(255,255,255) ,2)
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hour_angle = math.pi / 6 * hours + math.pi / 360 * minutes
    minute_angle = math.pi / 30 * minutes
    second_angle = math.pi / 30 * seconds
    x_end = 200 + (100 * 0.4) * math.sin(hour_angle)
    y_end = 200 -  (100 * 0.4) * math.cos(hour_angle)
    cv2.line(frame,(200, 200), (int(x_end), int(y_end)),(255,255,255) ,2)
    x_end = 200 + (100 * 0.6) * math.sin(minute_angle)
    y_end = 200 -  (100 * 0.6) * math.cos(minute_angle)
    cv2.line(frame,(200, 200), (int(x_end), int(y_end)),(255,255,255) ,2)
    x_end = 200 + (100 * 0.7) * math.sin(second_angle)
    y_end = 200 -  (100 * 0.7) * math.cos(second_angle)
    cv2.line(frame,(200, 200), (int(x_end), int(y_end)),(255,255,255) ,2)
   
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

