import cv2 as cv
import img as img
import mediapipe as mp

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()


def coordinate(id, h, w):
    cx, cy = lm.x * w, lm.y * h
    cv.circle(img, (int(cx), int(cy)), 2, (255, 255, 255), cv.FILLED)
    return cx, cy


Take_photo = 0

while True:
    success, img = cap.read()

    if not success:
        break

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    h, w, c = img.shape
    hands_up = 0
    finger1 = 0
    finger2 = 0
    finger3 = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                if id == 0:
                    _0, cy_0 = coordinate(0, h, w)
                if id == 2:
                    _2, cy_2 = coordinate(2, h, w)
                if id == 3:
                    _3, cy_3 = coordinate(3, h, w)
                if id == 5:
                    _5, cy_5 = coordinate(5, h, w)
                if id == 8:
                    _8, cy_8 = coordinate(8, h, w)
                if id == 9:
                    _9, cy_9 = coordinate(9, h, w)
                if id == 10:
                    _10, cy_10 = coordinate(10, h, w)
                if id == 12:
                    _12, cy_12 = coordinate(12, h, w)
                if id == 13:
                    _13, cy_13 = coordinate(13, h, w)
                if id == 16:
                    _16, cy_16 = coordinate(16, h, w)

            if cy_10 < cy_0:
                hands_up = 1
            else:
                hands_up = 0

            if cy_5 > cy_8:
                finger1 = 1
            else:
                finger1 = 0

            if cy_9 > cy_12:
                finger2 = 1
            else:
                finger2 = 0

            if cy_13 > cy_16:
                finger3 = 1
            else:
                finger3 = 0

            if finger1 == 1 and finger2 == 1 and finger3 == 1 and Take_photo == 0:
                Take_photo = 120

            elif finger1 == 1 and finger2 == 1 and Take_photo == 0:
                Take_photo = 90

            elif finger1 == 1 and Take_photo == 0:
                Take_photo = 60
    if Take_photo > 1:
        if Take_photo >= 90:
            cv.putText(img, '3', (int(w / 2), int(h / 2)), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)

        elif Take_photo >= 60:
            cv.putText(img, '2', (int(w / 2), int(h / 2)), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)

        elif Take_photo >= 30:
            cv.putText(img, '1', (int(w / 2), int(h / 2)), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)

        Take_photo -= 1

    elif Take_photo == 1:
        cv.imwrite("photo.jpg", img)
        Take_photo = 0

    cv.imshow("Image", img)

    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

img = cv.imread('photo.jpg')
cv.imshow('Selfie', img)
cv.waitkey(0)
cv.destroyAllWindow()
