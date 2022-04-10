from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image


# commands
def generate_qrcode():
    # retrieving inputs
    link_name = name_entry.get()
    link_url = link_entry.get()
    # generating filename
    file_name = link_name + ".png"
    # creating qr
    qr = pyqrcode.create(link_url)
    # creating file
    qr.png(file_name, scale=5)
    # displaying QR
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 370, window=image_label)


# initialization
root = Tk()
root.title("QR Code Generator")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

app_label = Label(root, text="QR Code Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)
# name & link input

name_label = Label(root, text="Title: ")
canvas.create_window(200, 100, window=name_label)

link_label = Label(root, text="QR Code URL: ")
canvas.create_window(200, 160, window=link_label)

# textboxes

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
link_entry = Entry(root)
canvas.create_window(200, 180, window=link_entry)

# create QR Code Button
button = Button(text="Generate QR Code", command=generate_qrcode)
canvas.create_window(200, 230, window=button)

root.mainloop()
