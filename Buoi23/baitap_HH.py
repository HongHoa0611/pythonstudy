#demo widget: Text
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning, askquestion

root = Tk()
root.title("DEMO WITGET CONTROL")
root.geometry("400x300")

mytext = Text(root, height=5) #height: số dòng của text, nếu nhiều hơn sẽ scroll
mytext.pack()
#gán dữ liệu ban đầu cho text
mytext.insert('1.0', 'Đây là dòng đầu') #cú pháp mytext.insert('line.column','nội dung')
mytext.insert('2.12', '2.12')

#lấy giá trị của widget 'text': mytext.get('line.column', 'end')
def show_info():
    showinfo(title="Result", message=mytext.get('1.0','end'))
ttk.Button(root, text="click", command=show_info).pack()


root.mainloop()