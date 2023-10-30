import os
#print(os.getcwd()) #lấy đường dẫn chinh xác tới vị trí đang gọi file chạy
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("400x300")

photo = PhotoImage(file="cart.png")
Label(root, image=photo).pack()

root.mainloop()