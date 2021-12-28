## PUT THIS ALL IN ONE CELL!
import math
import cv2
import dlib

# Connects to your computer's default camera
cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#midoint function

while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmark = predictor(gray, face)
        left_point = (landmark.part(36).x, landmark.part(36).y)
        right_point = (landmark.part(39).x, landmark.part(39).y)
        #x,y = face.left(), face.top()
        #x1,y1 = face.right(), face.bottom()
        cv2.circle(frame, left_point, 1, (255,0,0),1)
        cv2.circle(frame, right_point, 1, (255,0,0),1)
        cv2.line(frame, left_point ,right_point ,(255,0,0), 1)
        
        left_point1 = (landmark.part(42).x, landmark.part(42).y)
        right_point1 = (landmark.part(45).x, landmark.part(45).y)
        cv2.circle(frame, left_point1, 1, (255,0,0),1)
        cv2.circle(frame, right_point1, 1, (255,0,0),1)
        cv2.line(frame, left_point1 ,right_point1 ,(255,0,0), 1)
        
        up1 = (landmark.part(37).x, landmark.part(37).y)
        up2 = (landmark.part(38).x, landmark.part(38).y)
        
        low1 = (landmark.part(40).x, landmark.part(40).y)
        low2 = (landmark.part(41).x, landmark.part(41).y)
        
        
        right_up1 = (landmark.part(43).x, landmark.part(43).y)
        right_up2 = (landmark.part(44).x, landmark.part(44).y)
        
        right_low1 = (landmark.part(47).x, landmark.part(47).y)
        right_low2 = (landmark.part(46).x, landmark.part(46).y)
        #cv2.circle(frame, up1, 3, (255,255,255),3)
        #cv2.circle(frame, up2, 3, (255,255,255),3)
        
        
        #cv2.circle(frame, low1, 3, (0,222,0),3)
        #cv2.circle(frame, low2, 3, (0,0,255),3)
        
        up_mid = ((up1[0] + up2[0])/2 , (up1[1] + up2[1])/2 ) 
        low_mid = ((low1[0] + low2[0])/2 , (low1[1] + low2[1])/2 )
        dist = math.sqrt((up_mid[0]-low_mid[0])**2 + (up_mid[1]-low_mid[1])**2 ) 
        print(low1,low2,up_mid,dist)
        
        right_up_mid = ((right_up1[0] + right_up2[0])/2 , (right_up1[1] + right_up2[1])/2 ) 
        right_low_mid = ((right_low1[0] + right_low2[0])/2 , (right_low1[1] + right_low2[1])/2 )
        right_dist = math.sqrt((right_up_mid[0]-right_low_mid[0])**2 + (right_up_mid[1]-right_low_mid[1])**2 )
        text='blinking'
        font = cv2.FONT_HERSHEY_SIMPLEX
        if (right_dist < 5.5 and right_dist < 5.5):
            cv2.putText(frame, text, (50, 50), font, 2, (255, 255, 0), 2)
        
    # Display the resulting frame
        cv2.line(frame, (int(up_mid[0]),int(up_mid[1])) ,(int(low_mid[0]),int(low_mid[1])) ,(0,255,0), 3)
        cv2.line(frame, (int(right_up_mid[0]),int(right_up_mid[1])) ,(int(right_low_mid[0]),int(right_low_mid[1])) ,(0,255,0), 3)
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
