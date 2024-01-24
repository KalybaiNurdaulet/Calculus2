from tkinter import *
from tkinter import messagebox

import numpy as np
from scipy.integrate import quad
from scipy import integrate

root = Tk()

def btn_click():
    func1 = func.get()
    a = a_num.get()
    b = b_num.get()
    n = n_num.get()
    x = np.linspace(int(a), int(b), int(n))

    func2 = lambda x: eval(func1)
    reta, reta_error = integrate.quad(func2, int(a), int(b) )

    info_str = f'''Trapezoid  = {integrate.trapezoid(eval(func1), x)}
Trapezoid Error = {reta - integrate.trapezoid(eval(func1), x)}
    
Simpson = {integrate.simpson(eval(func1), x)}
Simpson Error = {reta - integrate.simpson(eval(func1), x)}
'''
    messagebox.showinfo(title='Name', message=info_str)

root['bg'] = '#fafafa'
root.title('TrapaSymp')
root.wm_attributes('-alpha')
root.geometry('500x500')


root.resizable(width=False,height=False)

canvas = Canvas(root, height=500, width=500)
canvas.pack()

frame = Frame(root, bg='blue')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame,text='Text sample', bg='gray', font=40)
title.pack()

btn = Button(frame, text='Button', bg='yellow', command=btn_click)
btn.pack()

func = Entry(frame, bg='white')
func.pack()

a_num = Entry(frame, bg='white')
a_num.pack()

b_num = Entry(frame, bg='white')
b_num.pack()

n_num = Entry(frame, bg='white')
n_num.pack()

root.mainloop()