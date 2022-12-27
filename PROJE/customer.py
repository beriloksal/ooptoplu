from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
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

    searchMovie =  Button(canvas,text="Search Movie",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    searchMovie.place(x=345,y=150, relwidth= 0.33)

    createBooking = Button(canvas,text="Create Booking",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    createBooking.place(x=345,y=200, relwidth= 0.33)

    viewBooking = Button(canvas,text="View Booking",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    viewBooking.place(x=345,y=250, relwidth= 0.33)

    cancelBooking = Button(canvas,text="Cancel Booking",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    cancelBooking.place(x=345,y=300, relwidth= 0.33)

    resetPassword = Button(canvas,text="Reset Password",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    resetPassword.place(x=345,y=350, relwidth= 0.33)

    logout = Button(canvas,text="Logout",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    logout.place(x=345,y=400, relwidth= 0.33)





    mainloop()