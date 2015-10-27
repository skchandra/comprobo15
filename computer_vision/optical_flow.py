# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0)

# ret, frame1 = cap.read()
# prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
# hsv = np.zeros_like(frame1)
# hsv[...,1] = 255

# while(1):
#     ret, frame2 = cap.read()
#     next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

#     flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

#     mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
#     hsv[...,0] = ang*180/np.pi/2
#     hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
#     rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

#     cv2.imshow('frame2',rgb)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#     elif k == ord('s'):
#         cv2.imwrite('opticalfb.png',frame2)
#         cv2.imwrite('opticalhsv.png',rgb)
#     prvs = next

# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()

prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

# Set counter to read the second frame at the start
counter = 1

# Until we reach the end of the list...
while (1):
    # Read the next frame in
    
    # Calculate optical flow between the two frames
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Normalize horizontal and vertical components
    horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)     
    vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
    horz = horz.astype('uint8')
    vert = vert.astype('uint8')

    # Show the components as images
    cv2.imshow('Horizontal Component', horz)
    cv2.imshow('Vertical Component', vert)

    # Change - Make next frame previous frame
    prvs = next.copy()

    # If we get to the end of the list, simply wait indefinitely
    # for the user to push something
    
    """if k == 27:
        break
    elif k == ord('s'): # Change
        cv2.imwrite('opticalflow_horz' + str(counter) + '-' + str(counter+1) + '.pgm', horz)
        cv2.imwrite('opticalflow_vert' + str(counter) + '-' + str(counter+1) + '.pgm', vert)"""

    # Increment counter to go to next frame
    counter += 1

cv2.destroyAllWindows()