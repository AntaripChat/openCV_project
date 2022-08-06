import cv2 as cv 

face_cas=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv.imread('ypp.jpg')
#cv.imshow('Img',img)
cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    face = face_cas.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow("img",img)

    k = cv.waitKey(30) & 0xff
    if k ==27:
        break
cap.release()

 
