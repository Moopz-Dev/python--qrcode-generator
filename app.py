from tkinter import *

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
button = Button(text="Generate QR Code")
canvas.create_window(200, 230, window=button)

root.mainloop()
