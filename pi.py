import string
import random
from tkinter import *
import os


root = Tk()
root.title("Генератор гениальных паролей")
root.geometry("400x300+300+200")
root["bg"] = "#bae6f2"

e = Entry(width=20)
l = Entry(width=20)
label1 = Label(text="Генератор паролей гениальных", fg="#FF00FF", bg="#FFFF00")

WORK_PATH=os.path.abspath(os.getcwd())
bg_image=PhotoImage(file=os.path.join(WORK_PATH,'hot.gif'))
bg=Label(root,image=bg_image)
bg.place(x=0, y=0, relwidth=1, relheight=1) 


btn = Button(text="Сгенерировать",          # текст кнопки 
             background="#FF1493",     # фоновый цвет кнопки
             foreground="#FFFFFF",     # цвет текста
             padx="120",             # отступ от границ до содержимого по горизонтали
             pady="20",              # отступ от границ до содержимого по вертикали
             font="16"
             )
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return (random.choice(chars) for _ in range(size))

def strToSortlist(event):
    l.delete(0, END) 
    s = int(e.get())
    l.insert(1, ''.join(id_generator(s)))


def clear():
    e.delete(0, END)
    l.delete(0, END)

clear_button = Button(text="Clear", command=clear)
clear_button.place(relx=.50, rely=.50, anchor="c", height=30, width=60, bordermode=OUTSIDE)

btn.bind('<Button-1>', strToSortlist)
clear_button.bind('<Button-2>', clear)


label1.pack()
e.pack()
btn.pack()
l.pack()
bg.pack()
clear_button.pack()
root.mainloop()
