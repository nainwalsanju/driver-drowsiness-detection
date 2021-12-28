# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:40:28 2019

@author: Sanjay
"""


import cv2
import matplotlib.pyplot as plt

see_left=0
see_right=0

front_face_cascade = cv2.CascadeClassifier('front_face.xml')
face_cascade = cv2.CascadeClassifier('face.xml')

def detect_right_face(img):
    #face_img = img.copy()
    global see_right
    face_rects = face_cascade.detectMultiScale(img,scaleFactor=1.2, minNeighbors=5)
    print(face_rects)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
    if len(face_rects)==0:
        x=-1
    else:
        x=1
        see_right += 1
    return (img,x)

def detect_front_face(img):
    #face_img = img.copy()
    #global see_left
    face_rects = front_face_cascade.detectMultiScale(img,scaleFactor=1.2, minNeighbors=5)
    print(face_rects)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
    if len(face_rects)==0:
        x=-3
    else:
        x=3
        #see_left += 1
    return (img,x)



def detect_left_face(img):
    #face_img = img.copy()
    global see_left
    face_rects = face_cascade.detectMultiScale(img,scaleFactor=1.2, minNeighbors=5)
    print(face_rects)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
    if len(face_rects)==0:
        x=-2
    else:
        x=2
        see_left += 1
    return (img,x)


front_face_cascade = cv2.CascadeClassifier('front_face.xml')
face_cascade = cv2.CascadeClassifier('face.xml')
#frame = cv2.imread('../../DATA/tshirt.jpg')
#frame = detect_face(frame)
#
#cv2.imshow('Face Detection', frame)
#cv2.waitKey(0)

cap = cv2.VideoCapture(0)

while True:
    #global see_left
    #global see_right
    ret, frame = cap.read(0)
    right=frame
    left = cv2.flip(frame,1)
    (left,check1) = detect_left_face(left)
    (right,check2) = detect_right_face(right)
    (front,check3) = detect_front_face(frame)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if(check1==2):
        text='left'
        if(see_left >= 150):
            text = "warning left"
        print(text,"see left = ",see_left)
        cv2.putText(left, text, (50, 50), font, 2, (255, 255, 0), 2)
        cv2.imshow('Video Face Detection', left)
    elif (check2==1):
        text='right'
        if(see_right >= 150):
            text = "warning right"
        print(text," see right = ",see_right)
        cv2.putText(right, text, (50, 50), font, 2, (255, 255, 0), 2)
        cv2.imshow('Video Face Detection', right)
    elif (check3==3):
        see_left=0
        see_right=0
        text="straight"
        print(text)
        cv2.putText(right, text, (50, 50), font, 2, (255, 255, 0), 2)
        cv2.imshow('Video Face Detection', frame)
    else:
        cv2.imshow('Video Face Detection', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
