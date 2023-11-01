from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('demo image by codemy.com')


my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\mrblackcat\\Desktop\\pythonclass\\pythonstudy\\HH project\\GUI.png"))
my_Label = Label(image=my_img)
my_Label.pack()















root.mainloop()