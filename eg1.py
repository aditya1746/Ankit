import cv2

# img = cv2.imread('lena.jpg')  # to read an image
img = cv2.imread('image5.jpg', 0) # 0 => gray, 1=> color, -1 => unchanged

cv2.imshow('frame',img) 
cv2.waitKey(0) # 0 => wait until a key is pressed, if arg>0 then wait for only that much milli seconds and then move on

cv2.destroyAllWindows()

print(img.shape) # height, width, channels ------------- height = rows, width = columns
# h,w,ch = img.shape[0], img.shape[1], img.shape[2]
# r,c,p = img.shape[0], img.shape[1], img.shape[2]

