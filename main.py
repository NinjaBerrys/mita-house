from tkinter import *
from PIL import Image
from PIL import ImageTk

# image as a clickable button
master = Tk()

width = 1133
height = 564
reference_img = Image.open("img/wireframe.png")
reference_img = reference_img.resize((width, height))
reference_photoImg = ImageTk.PhotoImage(reference_img)
b = Label(master, image=reference_photoImg)
b.pack()
mainloop()
