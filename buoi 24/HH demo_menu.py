from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()  #root là biến
root.geometry("400x300")

'''============màn hình con: TKINTER CHILD WINDOW============'''
def man_hinh_con(man_hinh_cha):
    mh_con = Toplevel(man_hinh_cha)
    mh_con.geometry("300x300")
    mh_con.title("MÀN HÌNH CON")

    ttk.Label(mh_con, text="ĐÂY LÀ MÀN HÌNH CON").pack(fill=X)
    mh_con.mainloop()

'''============màn hình con: TKINTER CHILD WINDOW============'''

#Menu chính (main menu)
menu_bar = Menu(root)
#nhúng menu vào màn hình chính
root.config(menu=menu_bar)

#Menu nhóm File
menu_file = Menu(menu_bar, tearoff=False) #con của những menu chính, bỏ cái đường gạch bên trên
menu_file.add_command(label='Mở MH con', command=lambda: man_hinh_con(root)) #nếu ko có tham số man_hinh_con thì ko cần hàm lambda
menu_file.add_command(label='New') #có thể thêm lệnh bằng ( , commad= lệnh)
menu_file.add_command(label='Open')
menu_file.add_command(label='Save')
menu_file.add_command(label='Close')
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.destroy) 

menu_bar.add_cascade(label='File', menu=menu_file)


# Nhóm menu Help
mnu_help = Menu(menu_bar, tearoff=0)
mnu_help.add_command(label='About Jupyter', command=lambda:showinfo(title="ABOUT", message="MY APP"))
menu_bar.add_cascade(label='Help', menu=mnu_help)


root.mainloop()