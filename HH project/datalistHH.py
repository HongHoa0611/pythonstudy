from tkinter import *
from tkinter import ttk
from MHDangNhap import man_hinh_dang_nhap

root = Tk()
root.title("X1 datalist")
root.geometry("1000x400")
#menu chính (main menu)
menu_bar = Menu(root)
#nhúng menu vào màn hình chính
root.config(menu=menu_bar)

menu_file = Menu(menu_bar, tearoff=False)
menu_file.add_command(label="log in", command=lambda: man_hinh_dang_nhap(root))
menu_file.add_command(label="log out")  
menu_file.add_separator()
menu_file.add_command(label="Exit")

menu_bar.add_cascade(label="Menu", menu=menu_file)

#gắn menu export:
mnu_export = Menu(menu_bar, tearoff=False)
mnu_export.add_command(label="Export excel file")
menu_bar.add_cascade(label="Export", menu=mnu_export)

# Chia làm 3 frame: Danh sách (TreeView), thao tác (Button), chi tiết (nhiều widget bên trong...)
frame_danh_sach = ttk.Frame(root)
frame_tac_vu = ttk.Frame(root)
frame_chi_tiet = ttk.Frame(root)
frame_danh_sach.grid(row=0, column=0)
frame_tac_vu.grid(row=1, column=0)
frame_chi_tiet.grid(row=2, column=0)

# Vùng danh sách
data_columns = ('data_id', 'data_name', 'specimen', 'data_type', 'image_size')
tv = ttk.Treeview(frame_list, columns=data_columns, show='headings', height=4)
tv.pack()

# Vùng tác vụ (gồm các button)
ttk.Button(frame_tac_vu, text="Add").pack()

root.mainloop()