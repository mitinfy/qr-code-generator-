import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
import sys
root=tk.Tk()
root.geometry('450x600+0+0')
root.title('QR Code generator')
root.configure(bg='khaki')
#root.state('zoomed')
lb=tk.Label(root, text='QR Code generator',font='sans 14',bg='#8207f5', fg='white').pack(fill='both')
lb3=tk.Label(root, text='Machine Learning app',font='sans 14',bg='#f0f288', fg='blue').pack(fill='both')

image=PhotoImage(file="myQr.jpg")
lbi=Label(image=image)
lbi.pack()

def callRead():
    import qrgen as cl
b1=tk.Button(root, text='Open QR Code generator App', command=callRead,bg='#a67e07', fg='white', font='sans 14',height=2, width=25).pack()

b3=tk.Button(root, text='Close Application', command=root.destroy,bg='red', fg='white',font='sans 14',height=2, width=25).pack()
lb2=tk.Label(root, text='Developed by MIT India',font='sans 14',bg='green', fg='white').pack(fill='both', side=tk.BOTTOM)

root.mainloop()
