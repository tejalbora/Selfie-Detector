from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import cv2 as cv
import img as img
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands()

root = tk.Tk()  # main window
root.configure(background='black')
root.geometry("800x600")
blank_space = " "
root.title(100 * blank_space + "WELCOME TO PYCAM!")

image_0 = Image.open('C:\\Users\\tejal\\OneDrive\\Desktop\\pycam.jpg')  # logo
image_0 = ImageTk.PhotoImage(image_0)
image_0_label = tk.Label(image=image_0, borderwidth=0)
image_0_label.image = image_0
image_0_label.grid(column=0, row=0)

selfie = Image.open("C:\\Users\\tejal\\OneDrive\\Desktop\\grp_selfie.jpg")  # side image of group photo
selfie = selfie.resize((300, 230))
selfie = ImageTk.PhotoImage(selfie, size="10x10")
selfie_label = tk.Label(image=selfie, borderwidth=15)
selfie_label.image = selfie
selfie_label.place(x=408, y=260)

label = tk.Label(text="Enter File Name").place(x=500, y=70)
filename = tk.Entry(root)
filename.place(x=500, y=100)


def savefile():
    global name
    name = filename.get()
    name = name + ".jpg"
    print(name)


Button(
    root,
    text="save",
    command=savefile,
    bg="light green"
).place(x=650, y=100)


def camera():
    cap = cv.VideoCapture(0)

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
        finger1 = 0
        finger2 = 0
        finger3 = 0

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    if id == 5:
                        _5, cy_5 = coordinate(5, h, w)
                    if id == 8:
                        _8, cy_8 = coordinate(8, h, w)
                    if id == 9:
                        _9, cy_9 = coordinate(9, h, w)
                    if id == 12:
                        _12, cy_12 = coordinate(12, h, w)
                    if id == 13:
                        _13, cy_13 = coordinate(13, h, w)
                    if id == 16:
                        _16, cy_16 = coordinate(16, h, w)

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
            cv.imwrite(name, img)
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


def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file")
    ''' filetype=[("Jpg File", "*.jpg")]'''
    if file:
        print("File is successfully loaded")
        read_img = Image.open(file)
        read_img.show()
    browse_text.set("== PyCam Gallery ==")


# browse button
browse_text = tk.StringVar()
camera_text = tk.StringVar()
gallery_text = tk.StringVar()

camera_btn = tk.Button(root, textvariable=camera_text, font="Raleway", bg="green")

camera_btn = tk.Button(root, textvariable=camera_text, command=lambda: camera(), font="Raleway", bg="#7F7FFF",
                       fg="white", height=3, width=25)
camera_text.set("== Camera ==")
camera_btn.grid(column=1, row=0)

browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", bg="#EEEE95",
                       fg="black", height=3, width=25)
browse_text.set("== Browse from Device ==")
browse_btn.grid(column=0, row=2)

gallery_btn = tk.Button(root, textvariable=gallery_text, command=lambda: open_file(), font="Raleway", bg="#14a76c",
                        fg="white", height=3, width=25)
gallery_text.set("== PyCam Gallery ==")
gallery_btn.grid(column=0, row=3)

root.mainloop()
