from tkinter import *
from PIL import ImageTk, Image


def forward(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=List_images[img_no - 1])

    label.grid(row=1, column=0, columnspan=3)
    button_for = Button(new, text="forward",
                        command=lambda: forward(img_no + 1))

    if img_no == 4:
        button_forward = Button(new, text="Forward",
                                state=DISABLED)

    button_back = Button(new, text="Back",
                         command=lambda: back(img_no - 1))

    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_for.grid(row=5, column=2)


def back(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(new, text="forward",
                            command=lambda: forward(img_no + 1))
    button_back = Button(new, text="Back",
                         command=lambda: back(img_no - 1))
    print(img_no)

    if img_no == 1:
        button_back = Button(new, Text="Back", state=DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


new = Tk()
new.title("Image Viewer")
new.geometry("700x700")

image_no_1 = ImageTk.PhotoImage(Image.open("photo1.jpg"))
image_no_2 = ImageTk.PhotoImage(Image.open("photo2.jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open("photo3.jpg"))
image_no_4 = ImageTk.PhotoImage(Image.open("photo4.jpg"))

List_images = [image_no_1, image_no_2, image_no_3, image_no_4]

label = Label(image=image_no_1)
label.grid(row=1, column=0, columnspan=3)

button_back = Button(new, text="Back", command=back,
                     state=DISABLED)

button_exit = Button(new, text="Exit",
                     command=new.quit)

button_forward = Button(new, text="Forward",
                        command=lambda: forward(1))

button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

new.mainloop()
