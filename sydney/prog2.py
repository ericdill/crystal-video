import numpy as np
import cv2
from matplotlib import pyplot as plt

vid = cv2.VideoCapture('C:/Users/sydne/OneDrive - North Carolina State University/Research/3.58 clips/3_58_-65_02-02-2022_00000000.mov')



while(vid.isOpened()):
  ret, frame = vid.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY_INV, 11, 2)
  #Thresh = np.uint8(Thresh)
  #denoise_2 = cv2.fastNlMeansDenoisingMulti(Thresh,None,5,5,7,21)
  
  cv2.imshow('Thresh',Thresh)
  #cv2.imshow('gray', gray)
  if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  
    
vid.release()
cv2.destroyAllWindows()