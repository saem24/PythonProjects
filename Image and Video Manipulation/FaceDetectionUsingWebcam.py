import cv2

#faceCascade = cv2.CascadeClassifier("/Users/saem/PycharmProjects/practiceProjects/Resources/haarcascades/haarcascade_frontalface_default.xml")
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)                          # 3 is for width
cap.set(4, frameHeight)                         # 4 is for height
# cap.set(10, 150)                              # 10 is for brightness

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

 #   for (x, y, w, h) in faces:
#        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       # Window closes on pressing 'q'
        break