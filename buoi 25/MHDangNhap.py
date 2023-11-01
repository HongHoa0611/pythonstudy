from tkinter import *
from tkinter import ttk

def man_hinh_dang_nhap(main_ui):
    login_ui = Toplevel(main_ui)

    login_ui.title("LOGIN")

    Label(login_ui, text= "LOGIN FORM", fg="red", font="Arial 16").place(x=90, y=10)
    Label(login_ui, text="Username:").place(x=30, y=50)
    Entry(login_ui).place(x=100, y=50)

    Label(login_ui, text="Email:").place(x=30, y=90)
    Entry(login_ui).place(x=100, y=90)

    Label(login_ui, text="Password:").place(x=30, y=130)
    Entry(login_ui).place(x=100, y=130)

    Button(login_ui, text="Login").place(x=110, y=160)
    
    login_ui.mainloop()