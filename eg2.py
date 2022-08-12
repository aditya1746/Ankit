import cv2
import numpy as np

img = np.zeros((480, 720, 3), np.uint8) # height, width, channels ----------- uint8 => unsigned int 8 bytes

# img1 = cv2.imread('image5.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL) # defining the window in which image is displayed, by default argument is cv2.WINDOW_AUTOSIZE

cv2.imshow('image', img)

k = cv2.waitKey(10000) & 0xFF

if(k == ord('s')):
    cv2.imwrite('saved.png', img)

cv2.destroyAllWindows()
# cv2.destroyWindow('image')