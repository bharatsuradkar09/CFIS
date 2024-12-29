from tkinter import *
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from subprocess import call


def register():
    call(["python", "registerGUI.py"])
def VideoSurveillance():
    call(["python", "surveillance.py"])


def resize_image(image,width,height):
    return image.resize((width,height),ImageTk.Image.Resampling.LANCZOS)
root = Tk()
root.geometry('860x500')
root.minsize(200,200)
root.maxsize(900,900)

root.title("Criminal Face Identification System")
# image1=Image.open("background_image/bg1.jpg")
# photo=ImageTk.PhotoImage(image1)
# image1 = resize_image(image1,860,500)
# photo1 = ImageTk.PhotoImage(image1)
# label0 = Label(root,image=photo1)
# label0.place(relwidth=1,relheight=1)
root.configure(bg="#c6cfcf")

Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""
image=Image.open("image.jpg")
photo=ImageTk.PhotoImage(image)
image = resize_image(image,860,120)
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=800,height=0,bg='#c6cfcf').place(relwidth=1,y=0)
photo_label

label_0 = Label(root, text="Criminal Face Identification System",width=50,font=("bold", 20),anchor=CENTER,bg="#386184",fg="white")
label_0.place(relwidth=1,y=100)

Button(root, text='REGISTER CRIMINAL',width=25,height=2,bg='#05415b',fg='white',font=("bold", 13),command=register).place(x=280,y=180)
Button(root, text='VIDEO SURVEILLANCE',width=25,height=2,bg='#952f68',fg='white',font=("bold", 13),command=VideoSurveillance).place(x=280,y=260)
root.mainloop()