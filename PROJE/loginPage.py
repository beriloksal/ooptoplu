from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import guest_homepage
import signup_page
import cinema_seats
import admin
import customer
import frontdeskofficer

def signUpButton():
    signup_page.view(root)

def guestButton():
    guest_homepage.view(root)

def loginButton():
    customer.view(root)

root = Tk()
root.resizable(False, False)
rootFrame = Frame(root)
rootFrame.pack(fill=BOTH, expand=True)
root.title("Welcome")
root.geometry("1000x650")

image1 = Image.open("loginpage.png")
resize_image1 = image1.resize((1000,650))
image2 = ImageTk.PhotoImage(resize_image1)

canvas1 = Canvas(rootFrame, width=1000, height = 650)
canvas1.pack(fill=BOTH, expand= True)
canvas1.create_image(0,0, image= image2, anchor="nw")


welcome_image= Image.open("welcome.jpg")
resize_welcome_image= welcome_image.resize((400,75))
welcome_icon = ImageTk.PhotoImage(resize_welcome_image)

welcome_label = Label(canvas1, image = welcome_icon)
welcome_label.place(x=300,y=10)

login_image = Image.open("signup_icon.png")
icon_image = ImageTk.PhotoImage(login_image)
login_image_Label= Label(canvas1, image = icon_image , bg="black")
login_image_Label.place(x=444,y=100)

sign_in_label = Label(canvas1, text= "Sign In", fg="white",bg="black", font=("Lucida Sans",18,"bold"))
sign_in_label.place(x=462,y=190)

username_label= Label(canvas1, text="Username : ",  bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
username_label.place(x=360, y=230)
username_entry = Entry(canvas1,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),insertbackground="white")
username_entry.place(x=400, y=260)
username_line= Canvas(canvas1, width=300, height=2.0,bg="white",highlightthickness=0)
username_line.place(x=362, y=292)

popcorn_image = Image.open("popcorn.png")
icon_image2 = ImageTk.PhotoImage(popcorn_image)
popcorn_image_Label= Label(canvas1, image= icon_image2, bg="black")
popcorn_image_Label.place(x=362,y=257)

password_label= Label(canvas1, text="Password :", bg="black" , fg="white",font=("Lucida Sans",16,"bold"))
password_label.place(x=360,y=325)
password_entry = Entry(canvas1, highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",16,"bold"),show="*",insertbackground="white")
password_entry.place(x=400,y=355)
password_line = Canvas(canvas1, width=300, height=2.0,bg="white",highlightthickness=0)
password_line.place(x=362, y=387)
popcorn_image_Label2 = Label(canvas1, image= icon_image2, bg="black")
popcorn_image_Label2.place(x=362,y=352)

login_button  = Button( canvas1, text="     LOGIN     ", fg="black",bg="white", font=("Lucida Sans",16,"bold"),activebackground="white",command=lambda: loginButton())
login_button.place(x=430,y=420)

no_account_label = Label(canvas1,text=" No account yet? ",  bg="black" , fg="white",font=("Lucida Sans",16,"bold","underline"))
no_account_label.place(x=320, y=480)
sign_up_button = Button(canvas1, text="SIGN UP NOW", fg="white",bg="brown", font=("Lucida Sans",13,"bold"),activebackground="brown",command=lambda: signUpButton())
sign_up_button.place(x=530, y=480)
guest_button = Button(canvas1, text="GUEST", fg="white", font=("Lucida Sans",20,"bold"),bg="black",activebackground="black",activeforeground="white",command= lambda: guestButton())
guest_button.place(x=530,y=520)


mainloop()

