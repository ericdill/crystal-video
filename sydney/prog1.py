import numpy as np
import cv2
#from matplotlib import pyplot as plt
vid = cv2.VideoCapture('C:/Users/sydne/OneDrive - North Carolina State University/Research/3.58 clip2.mov')

#video writer


#height =  int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#fps = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

#videowriter = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('P','I','M','1'), fps, (width, height), isColor=False) 
                                                                           
for frame_idx in range(int(vid.get(cv2.CAP_PROP_FRAME_COUNT))):
    
    # Read frame 
    #ret, frame = cap.read()
    
    # Gray transform
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Show image
    #cv2.imshow('Video Player', gray)
    
    # Write out frame 
#while(vid.isOpened()):
  ret, frame = vid.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY_INV, 11, 2)
  #Thresh = np.uint8(Thresh)
  #denoise_2 = cv2.fastNlMeansDenoisingMulti(Thresh,None,5,5,7,21)
  
  cv2.imshow('Thresh',Thresh)
  #cv2.imshow('gray', gray)
  #videowriter.write(Thresh)
  if cv2.waitKey(25) & 0xFF == ord('q'):
      break

    
vid.release()
cv2.destroyAllWindows()
#videowriter.release