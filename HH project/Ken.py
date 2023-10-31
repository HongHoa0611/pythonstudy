from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.geometry("500x400")
root.title('Study With Ken')
#Menu chinh (main menu)




#Menu phụ

#open image
tiger_img = ImageTk.PhotoImage(Image.open("C:\\Users\\mrblackcat\\Desktop\\pythonclass\\pythonstudy\\HH project\\tiger.jpg"))

#resize image
resized = tiger_img.resize((100, 75), Image.ANTIALIAS)

new_tiger = ImageTk.PhotoImage(resized)

my_Label = Label(image=new_tiger)
my_Label.pack(pady=20)












root.mainloop()