
from ctypes import resize
from os import name
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from turtle import width

def view(pencere):


    root = tk.Toplevel()
    root.resizable(False, False)
    root.title("Homepage")
    root.geometry("1000x650")

    image1 = Image.open("loginpage.png")
    resize_image2 = image1.resize((1000, 650))
    image2 = ImageTk.PhotoImage(resize_image2)

    canvas = Canvas(root, width=1000, height=650)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0,0, image=image2, anchor="nw")
    pencere.withdraw()

    login_image = Image.open("signup_icon.png")
    icon_image = ImageTk.PhotoImage(login_image)
    login_image_Label= Label(canvas, image = icon_image , bg="black")
    login_image_Label.place(x=444,y=30)

    name_label= Label(canvas, text="Name : ",  bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
    name_label.place(x=360, y=120)
    name_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),insertbackground="white")
    name_entry.place(x=400, y=150)
    name_line= Canvas(canvas, width=300, height=2.0,bg="white",highlightthickness=0)
    name_line.place(x=362, y=182)

    popcorn_image = Image.open("popcorn.png")
    icon_image2 = ImageTk.PhotoImage(popcorn_image)
    popcorn_image_Label= Label(canvas, image= icon_image2, bg="black")
    popcorn_image_Label.place(x=362,y=147)

    surname_label=Label(canvas, text="Surname :", bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
    surname_label.place(x=360, y=200)
    surname_entry=Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),insertbackground="white")
    surname_entry.place(x=400, y=230)
    surname_line = Canvas(canvas, width=300, height=2.0,bg="white",highlightthickness=0 )
    surname_line.place(x=362, y=262)
    popcorn_image_Label2 = Label(canvas, image= icon_image2, bg="black")
    popcorn_image_Label2.place(x=362,y=227)

    username_label= Label(canvas, text="Username : ",  bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
    username_label.place(x=360, y=280)
    username_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),insertbackground="white")
    username_entry.place(x=400, y=310)
    username_line= Canvas(canvas, width=300, height=2.0,bg="white",highlightthickness=0)
    username_line.place(x=362, y=342)
    popcorn_image_Label3 = Label(canvas, image= icon_image2, bg="black")
    popcorn_image_Label3.place(x=362,y=307)

    password_label= Label(canvas, text="Password :", bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
    password_label.place(x=360,y=360)
    password_entry = Entry(canvas, highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),show="*",insertbackground="white")
    password_entry.place(x=400,y=390)
    password_line = Canvas(canvas, width=300, height=2.0,bg="white",highlightthickness=0)
    password_line.place(x=362, y=422)
    popcorn_image_Label3 = Label(canvas, image= icon_image2, bg="black")
    popcorn_image_Label3.place(x=362,y=387)

    passwordconfirm_label= Label(canvas, text="Password Confirm :", bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
    passwordconfirm_label.place(x=360,y=440)
    passwordconfirm_entry = Entry(canvas, highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),show="*",insertbackground="white")
    passwordconfirm_entry.place(x=400,y=470)
    passwordconfirm_line = Canvas(canvas, width=300, height=2.0,bg="white",highlightthickness=0)
    passwordconfirm_line.place(x=362, y=502)
    popcorn_image_Label4 = Label(canvas, image= icon_image2, bg="black")
    popcorn_image_Label4.place(x=362,y=467)

    sign_up_button = Button(canvas, text="SIGN UP", fg="white",bg="brown", font=("Lucida Sans",18,"bold"),activebackground="brown")
    sign_up_button.place(x=445, y=520)

    back_icon_image = Image.open("back_icon.png")
    icon_image4 = ImageTk.PhotoImage(back_icon_image)
    back_icon_buton = Button(canvas, image=icon_image4,bg="black",activebackground="black")
    back_icon_buton.place(x=10,y=10)






mainloop()
