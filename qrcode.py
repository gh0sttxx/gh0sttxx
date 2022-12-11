from tkinter import *
from tkinter import messagebox
import pyqrcode

qrcodegnr = Tk()
qrcodegnr.title("QrCode by @gh0stxx")
qrcodegnr.config(bg='#F25252')

def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning('AVISO!', 'você deve inserir um link.')
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="scan qrcode ")


lbl = Label(
    qrcodegnr,
    text="adiciona aqui o url",
    bg='#F25252'
    )
lbl.pack()

user_input = StringVar()
entry = Entry(
    qrcodegnr,
    textvariable = user_input
    )
entry.pack(padx=10)


button = Button(
    qrcodegnr,
    text = "Gerar QrCode",
    width=15,
    command = generate_QR
    )
button.pack(pady=10)

img_lbl = Label(
    qrcodegnr,
    bg='#F25252')
img_lbl.pack()
output = Label(
    qrcodegnr,
    text="",
    bg='#F25252'
    )
output.pack()
 
qrcodegnr.mainloop()