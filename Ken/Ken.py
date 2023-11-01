from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.geometry("500x400")
root.title('Study With Ken')
#Menu chinh (main menu)
menu_bar = Menu(root)
#nhúng menu vào màn hình chính
root.config(menu=menu_bar)

menu_file = Menu(menu_bar, tearoff=False)
menu_file.add_command(label="Game")
menu_file.add_command(label="ABC")  
menu_file.add_separator()
menu_file.add_command(label="Exit")

menu_bar.add_cascade(label="Hệ Thống", menu=menu_file)


#Menu phụ

#open image
tiger_img = ImageTk.PhotoImage(Image.open("C:\\Users\\mrblackcat\\Desktop\\pythonclass\\pythonstudy\\HH project\\tiger.jpg"))

#resize image
#resized = tiger_img.resize((100, 75), Image.ANTIALIAS)

#new_tiger = ImageTk.PhotoImage(resized)

my_Label = Label(image=tiger_img)
my_Label.pack(pady=20)












root.mainloop()