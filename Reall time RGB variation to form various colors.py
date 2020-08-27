import numpy as np
import cv2

def callback_fn(x):
    print(x)

# let's create a empty black image...
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Combination of RGB to form colors...')

cv2.createTrackbar('Blue','Combination of RGB to form colors...',0,255,callback_fn)
cv2.createTrackbar('Green','Combination of RGB to form colors...',0,255,callback_fn)
cv2.createTrackbar('Red','Combination of RGB to form colors...',0,255,callback_fn)

while True:
    cv2.imshow('Combination of RGB to form colors...',img)
    k=cv2.waitKey(1)&0xff
    if k==ord('q'):
        break
    b_color=cv2.getTrackbarPos('Blue','Combination of RGB to form colors...')
    g_color=cv2.getTrackbarPos('Green','Combination of RGB to form colors...')
    r_color = cv2.getTrackbarPos('Red', 'Combination of RGB to form colors...')
    img[:] = [b_color,g_color,r_color]
cv2.destroyAllWindows()
