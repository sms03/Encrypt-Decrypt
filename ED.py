from tkinter import *
from tkinter import messagebox
import base64
import os

global screen
global code
global text1

def decrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="Lightgreen")

        message=text1.get(1.0, END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")


        Label(screen2, text="DECRYPT", font="Arial", fg="white", bg="Lightgreen").place(x=10, y=0)
        text2=Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=350, height=150)

        text2.insert(END, decrypt)
    
    elif password=="":
        messagebox.showerror("decryption", "Input Passcode")
    
    elif password != "1234":
        messagebox.showerror("decryption", "Invalid Passcode")


def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0, END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")


        Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2=Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=350, height=150)

        text2.insert(END, encrypt)
    
    elif password=="":
        messagebox.showerror("encryption", "Input Passcode")
    
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Passcode")


def main_screen():
    
    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("400x400")

    #icon=PhotoImage(file=".jpg")
    #screen.iconphoto(False,icon)

    screen.title("ED")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for Encryption or Decryption", fg="black", font=("Times New Roman",16)).place(x=10,y=10)
    text1=Text(font="Arial 22", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=380, height=100)

    Label(text="Enter secret ED key", fg="black", font=("Times New Roman",16)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code, width=18, bd=0, font=("Calibri", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=24, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=24, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=215, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=25, y=300)

    screen.mainloop()

main_screen()        