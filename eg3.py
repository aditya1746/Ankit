import cv2
import numpy as np

fps = 30
w,h = 720, 480

cap = cv2.VideoCapture(0) # 0=>webcam, 1=> usbcam, mobile ke camera ko bhi wireless connection ke through le sakte he, usme thodi or complexities he
# cap = cv2.VideoCapture('vtest.avi')

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output = cv2.VideoWriter('output.mp4', fourcc, fps, (w, h))
n = 0

while cap.isOpened():

    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    num = 'img' + str(n) + '.jpg'

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(num, frame)

        n = n+1
    
    # frame = cv2.flip(frame, 0) 
    # output.write(frame)

cap.release()
cv2.destroyAllWindows()
