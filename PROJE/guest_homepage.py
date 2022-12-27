from tkinter import *
from turtle import width
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk



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


    movie_search_list = ["Search Movie By City Name","Search Movie By Genre","Search Movie By Language",
                         "Search Movie By Release Date","Search Movie By Title",]

    style = ttk.Style()
    style.theme_use('alt')
    ebg = 'white'
    fg = 'black'
    root.option_add('*TCombobox*Listbox*Background', ebg)
    root.option_add('*TCombobox*Listbox*Foreground', fg)
    root.option_add('*TCombobox*Listbox*selectBackground', fg)
    root.option_add('*TCombobox*Listbox*selectForeground', ebg)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])

    search_movie_button = ttk.Combobox(canvas,values= movie_search_list,font=("Lucida Sans",20,"bold"), state="readonly",width= 25)
    search_movie_button.set("Select...")
    search_movie_button.place(x=265, y=125)

    select_button = Button(canvas,text="Submit",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    select_button.place(x=725,y=121)

    getSelect_button = search_movie_button.get()

    movies_image= Image.open("movies.png")
    resize_movies_image= movies_image.resize((450,95))
    movies_icon = ImageTk.PhotoImage(resize_movies_image)

    movies_label = Label(canvas, image = movies_icon, bg="black")
    movies_label.place(x=275,y=10)

    popcorn_image = Image.open("popcorn2.png")
    icon_image2 = ImageTk.PhotoImage(popcorn_image)
    popcorn_image2 = Image.open("popcorn3.png")
    icon_image3 = ImageTk.PhotoImage(popcorn_image2)
    popcorn_image_Label= Label(canvas, image= icon_image3, bg="black")
    popcorn_image_Label.place(x=690,y=20)
    popcorn_image_Label2= Label(canvas, image= icon_image2, bg="black")
    popcorn_image_Label2.place(x=260,y=20)

    back_icon_image = Image.open("back_icon.png")
    icon_image4 = ImageTk.PhotoImage(back_icon_image)
    back_icon_buton = Button(canvas, image=icon_image4,bg="black",activebackground="black")
    back_icon_buton.place(x=10,y=10)

    pencere.withdraw()
    mainloop()
