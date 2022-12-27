from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from turtle import width




def addMovie():
    root = tk.Toplevel()
    root.resizable(False, False)
    root.title("Homepage")
    root.geometry("550x450")

    image1 = Image.open("loginpage.png")
    resize_image2 = image1.resize((550, 450))
    image2 = ImageTk.PhotoImage(resize_image2)

    canvas = Canvas(root, width=550, height=450)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0,0, image=image2, anchor="nw")

    title_label= Label(canvas, text="-Title : ",  bg="black" , fg="white",font=("Lucida Sans",14,"bold"))
    title_label.place(x=120, y=120)
    title_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",14,"bold"),insertbackground="white")
    title_entry.place(x=194, y=120)
    title_line= Canvas(canvas, width=250, height=2.0,bg="white",highlightthickness=0)
    title_line.place(x=194, y=144)

    genre_label = Label(canvas, text="-Genre : ",  bg="black" , fg="white",font=("Lucida Sans",14,"bold"))
    genre_label.place(x=110, y=160)
    genre_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",14,"bold"),insertbackground="white")
    genre_entry.place(x=194, y=160)
    genre_line = Canvas(canvas, width=250, height=2.0,bg="white",highlightthickness=0)
    genre_line.place(x=194, y=184)

    language_label = Label(canvas, text="-Language : ",  bg="black" , fg="white",font=("Lucida Sans",14,"bold"))
    language_label.place(x=70, y=200)
    language_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",14,"bold"),insertbackground="white")
    language_entry.place(x=194, y=200)
    language_line = Canvas(canvas, width=250, height=2.0,bg="white",highlightthickness=0)
    language_line.place(x=194, y=224)

    releaseDate_label = Label(canvas, text="-Release Date : ",  bg="black" , fg="white",font=("Lucida Sans",14,"bold"))
    releaseDate_label.place(x=40, y=240)
    releaseDate_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",14,"bold"),insertbackground="white")
    releaseDate_entry.place(x=194, y=240)
    releaseDate_line = Canvas(canvas, width=250, height=2.0,bg="white",highlightthickness=0)
    releaseDate_line.place(x=194, y=264)

    cityName_label =Label(canvas, text="-City Name : ",  bg="black" , fg="white",font=("Lucida Sans",14,"bold"))
    cityName_label.place(x=63, y=280)
    cityName_entry = Entry(canvas,highlightthickness=0, relief= FLAT , bg="black", fg="white",font=("Lucida Sans",14,"bold"),insertbackground="white")
    cityName_entry.place(x=194, y=280)
    cityName_line = Canvas(canvas, width=250, height=2.0,bg="white",highlightthickness=0)
    cityName_line.place(x=194, y=304)

    text = Label(canvas, text="MOVIE ADD : ",  bg="black" , fg="white",font=("Lucida Sans",20,"bold"))
    text.place(x=200,y=50)

    save = Button( canvas, text="    Save    ", fg="black",bg="white", font=("Lucida Sans",16,"bold"),activebackground="white")
    save.place(x=225,y=325)

    mainloop()

def view(pencere):
    global x

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

    admin_image = Image.open("admin.png")
    resize_admin_image = admin_image.resize((100,100))
    icon_image = ImageTk.PhotoImage(resize_admin_image)
    admin_image_Label= Label(canvas, image = icon_image , bg="black")
    admin_image_Label.place(x=455,y=30)

    back_icon_image = Image.open("back_icon.png")
    icon_image4 = ImageTk.PhotoImage(back_icon_image)
    back_icon_buton = Button(canvas, image=icon_image4,bg="black",activebackground="black")
    back_icon_buton.place(x=10,y=10)

    #search_list = ["Add movie","Modify movie","Add show","Cancel show","Modify show","Update/Cancel booking"]

    #style = ttk.Style()
    #style.theme_use('alt')
    #ebg = 'white'
    #fg = 'black'
    #root.option_add('*TCombobox*Listbox*Background', ebg)
    #root.option_add('*TCombobox*Listbox*Foreground', fg)
    #root.option_add('*TCombobox*Listbox*selectBackground', fg)
    #root.option_add('*TCombobox*Listbox*selectForeground', ebg)
    #style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    #style.map('TCombobox', selectbackground=[('readonly', ebg)])
    #style.map('TCombobox', selectforeground=[('readonly', fg)])
    #style.map('TCombobox', background=[('readonly', ebg)])
    #style.map('TCombobox', foreground=[('readonly', fg)])
    #current_table = tk.StringVar()
    #search_movie_button = ttk.Combobox(canvas,values= search_list,font=("Lucida Sans",20,"bold"), state="readonly",width= 25,textvariable = current_table)
    #search_movie_button.set("Select...")
    #search_movie_button.place(x=265, y=140)

    #select_button = Button(canvas,text="Submit",font=("Lucida Sans",18,"bold"),foreground="white",background="black",command=lambda:buttonSelect())
    #select_button.place(x=725,y=136)

    #value = search_movie_button.get()

    addMovieButton =  Button(canvas,text="Add Movie",font=("Lucida Sans",18,"bold"),foreground="white",background="black",command= lambda: addMovie())
    addMovieButton.place(x=345,y=200, relwidth= 0.33)

    modifyMovie = Button(canvas,text="Modify Movie",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    modifyMovie.place(x=345,y=250, relwidth= 0.33)

    addShow = Button(canvas,text="Add Show",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    addShow.place(x=345,y=300, relwidth= 0.33)

    cancelShow = Button(canvas,text="Cancel Show",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    cancelShow.place(x=345,y=350, relwidth= 0.33)

    modifyShow = Button(canvas,text="Modify Show",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    modifyShow.place(x=345,y=400, relwidth= 0.33)

    updateCancel = Button(canvas,text="Update/Cancel Booking",font=("Lucida Sans",18,"bold"),foreground="white",background="black")
    updateCancel.place(x=345,y=450, relwidth= 0.33)



    mainloop()