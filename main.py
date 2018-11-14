import numpy as np
import cv2
import pyautogui

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in hand:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 5)
        pyautogui.press('space')  # controls the space button by hand(human gui)
        print('jump')

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release
cv2.destroyAllWindows()













































        
        
        
        
