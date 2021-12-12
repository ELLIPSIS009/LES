from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import datetime
from police_viewProfile import police
import sqlite3
import os

def police_dashboard(j):
    connection = sqlite3.connect('LES.db')
    cursor = connection.cursor()
    q = cursor.execute('SELECT * FROM POLICE where POLICEID=?', (j,))
    u = q.fetchall()
    t = tk.Tk()
    t.title('LES ACP HOME')
    t.configure(background='white')
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(t, image=bg)
    label1.place(x=-10, y=-10)
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    fing = tkFont.Font(family="Times New Roman", size=20)

    def enter_profile():
        photo = u[0][5]
        photoPath = "acp" + j + ".jpg"
        with open(photoPath, 'wb') as file:
            file.write(photo)
        t.destroy()
        police(j, photoPath)
        return

    def search():
        t.destroy()
        from police_search import worst
        worst(j)

    def add():
        t.destroy()
        from police_addData import wii
        wii(j)

    def logout():
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE POLICE set LASTLOGIN=? where POLICEID=?", (b, j))
        connection.commit()
        t.destroy()
        os.system('python index_login.py')

    name=Label(t, text=str(u[0][2]).upper()+' '+str(u[0][4]).upper(),bg='white', fg='grey', borderwidth=2, relief="solid")

    profile=Button(t, text='MY PROFILE',font=fing, command=enter_profile, borderwidth=2, relief="solid")
    access=Button(t, text='ACCESS RECORDS',font=fing, command=search, borderwidth=2, relief="solid")
    logout=Button(t, text='LOGOUT', command=logout,font=fing, borderwidth=2, relief="solid")
    add=Button(t, text='ADD DATA',command=add,font=fing, borderwidth=2, relief="solid")
    name.configure(font=("Times New Roman",50 , 'bold'))
    name.place(x=0, y=90, width=w, height=100)
    access.place(x=300, y=350, width=400, height=100)
    add.place(x=300, y=500, width=400, height=100)
    profile.place(x=750, y=350, width=400, height=100)
    logout.place(x=750, y=500, width=400, height=100)
    mainloop()