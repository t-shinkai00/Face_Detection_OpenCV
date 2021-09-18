import numpy as np
import cv2

img = cv2.imread('data/messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
# print(k)
if k == ord('q'):         # wait for 'q' key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()