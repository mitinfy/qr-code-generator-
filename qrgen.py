import tkinter as tk
import qrcode
from tkinter import messagebox
root=tk.Tk()
root.geometry('450x600+0+0')
root.title('QR Code generator')
root.configure(bg='khaki')
#root.state('zoomed')
lb=tk.Label(root, text='QR Code generator',font='sans 14',bg='#8207f5', fg='white').pack(fill='both')
lb3=tk.Label(root, text='Machine Learning Application',font='sans 14',bg='#f0f288', fg='blue').pack(fill='both')
lb4=tk.Label(root, text='Enter text or URL to make QR Code',font='sans 14',bg='yellow', fg='blue').pack(fill='both')

sam=tk.StringVar()  

tx=tk.Entry(root, textvariable=sam,font='sans 14',bg='cyan', fg='blue').pack(fill='both')


def genQR():
    t=(sam.get())
    img = qrcode.make(t)
    #or img = qrcode.make("MIT India.")
    img.save("myQR.jpg")
    messagebox.showinfo("QR Code", "QR Code generated Successfully!")
    
b1=tk.Button(root, text='Generate QR Code',command=genQR,bg='#a67e07', fg='white', font='sans 14',height=2, width=25).pack()

def showReport():
    import qrdec as co
b2=tk.Button(root, text='Decode QR code', command=showReport,bg='#155ad1', fg='white', font='sans 14',height=2, width=25).pack()

b3=tk.Button(root, text='Close Application', command=root.destroy,bg='red', fg='white',font='sans 14',height=2, width=25).pack()
lb2=tk.Label(root, text='Developed by MIT India',font='sans 14',bg='green', fg='white').pack(fill='both', side=tk.BOTTOM)


'''
img = qrcode.make("https://www.youtube.com/")
# or img = qrcode.make("MIT India.")
img.save("youtubeQR.jpg")
'''
