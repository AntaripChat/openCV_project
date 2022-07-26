import cv2 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.C
img = cv2.imread('img.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)

cv2.imshow('img',img)
cv2.waitKey()
#123
