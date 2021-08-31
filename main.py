import cv2 as cv
import screen_brightness_control as sbc

camera_id = 1

camera = cv.VideoCapture(camera_id)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    
    ret, frame = camera.read()

    if ret:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, 1.05, 15, minSize=(50, 50))


        for (x, y, w, h) in face:
            cv.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)

            if (y+h)-y < 250: sbc.set_brightness(100)
            elif (y+h)-y > 250 and (y+h)-y < 290: sbc.set_brightness(80)
            elif (y+h)-y > 290 and (y+h)-y < 330: sbc.set_brightness(60)
            elif (y+h)-y > 330 and (y+h)-y < 370: sbc.set_brightness(40)
            elif (y+h)-y > 370: sbc.set_brightness(20)

        # cv.imshow("Brightness Control", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv.destroyAllWindows()
