from abc import ABC
from .constants import AccountStatus
import pymysql
import signup_page
import admin

conn = pymysql.connect(host="localhost", user="root", password="123456", db="homework")




# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes ae private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        check_password = input(__prompt="Enter your current password:") #get input from check_password_entry
        if check_password == self.__password:
            print("Password Correct! Type your new password:")
            new_password = input()
            print("Type your new password one more time:")
            new_password2 = input()
            if new_password == new_password2:
                self.__password = new_password
                return "Password Changed!"
            else:
                print("The passwords don't match.")
                i = 1
                for i in range(3):
                    print("Type your new password one more time:")
                    new_password2 = input()
                    if new_password == new_password2:
                        self.__password = new_password
                        return "Password Changed!"
                    else:
                        print("The passwords don't match.")
                        i -= 1
                return "Failed to change the password."

        else:
            print("Wrong Password.")
            return "Failed to change the password."


# from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Customer(Person):
    def make_booking(self, booking):
        None

    def get_bookings(self):
        None


class Admin(Person):
    def add_movie(self, movie):
        title = admin.title_entry()
        language = admin.language_entry()
        genre = admin.genre_entry()
        release_date = admin.releaseDate_entry()


        cursor = conn.cursor()
        sql = "INSERT INTO movie (title, language, releaseDate, genre) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, language, release_date, genre))
        conn.commit()
    conn.close()

    def add_show(self, show):
        None


    def block_user(self, customer):
        None

class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        None


class Guest:
    def register_account(self):
        username = signup_page.username_entry()
        password = signup_page.password_entry()
        cursor = conn.cursor()
        int : idnum = 8 #1 admin + 1 frontdesk + grup üyelerinin her biri için databasede zaten üye oluşturduk o yüzden 8
        sql = "INSERT INTO account (id, username, password, status) VALUES (idnum, %s, %s, customer)"
        cursor.execute(sql, (username, password))
        idnum =+1
        conn.commit()
    conn.close()
