import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)                          # 3 is for width
cap.set(4, frameHeight)                         # 4 is for height
# cap.set(10, 150)                              # 10 is for brightness

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       # Window closes on pressing 'q'
        break
