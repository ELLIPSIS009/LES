from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import os
import sqlite3
from civilian_viewProfile import display_details

def civ_home(id):
    t=tk.Tk()
    t.title('LES Civilian')
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(t, image=bg)
    label1.place(x=-10, y=-10)
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    connection = sqlite3.connect('LES.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY, PASSWORD text NOT NULL, FNAME text, MNAME text, LNAME text, DOB date, GENDER text, MARITALSTATUS text, EMAILID text NOT NULL, OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)')
    cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN2 (USERID text PRIMARY KEY, CONTACT number)')
    retrieve=cursor.execute('SELECT * FROM CIVILIAN1 WHERE USERID = (?) ',(id,))
    temp=retrieve.fetchall()
    retrieve2=cursor.execute('SELECT * FROM CIVILIAN2 WHERE USERID = (?) ',(id,))
    temp2=retrieve2.fetchall()

    def enter_profile():
        t.destroy()
        display_details(temp[0],temp2[0])
        return

    def complaint():
        t.destroy()
        import civilian_complaintForm as tty
        tty.comp(id)
        return

    def status():
        t.destroy()
        import civilian_complaintStatus as tty
        tty.stat(id)
        return

    def logout():
        import datetime
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE CIVILIAN1 set LASTLOGIN=? where USERID=?", (b,id))
        connection.commit()
        t.destroy()
        os.system('python index_login.py')

    t.configure(background = 'white')

    name=Label(t, text=temp[0][2].upper()+' '+temp[0][3].upper()+' '+temp[0][4].upper(), fg='grey',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
    profile=Button(t, text='YOUR PROFILE'.upper(), font=tkFont.Font(family="Times New Roman", size=16),command=enter_profile, borderwidth=2, relief="solid")
    complain=Button(t, text='REGISTER COMPLAINT'.upper(), command=complaint, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    track=Button(t, text='TRACK COMPLAINT STATUS'.upper(), command=status, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    logout=Button(t, text='LOGOUT '.upper(), command=logout, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))

    name.place(x=0, y=90, width=w, height=100)
    profile.place(x=750, y=350, width=400, height=100)
    logout.place(x=750, y=500, width=400, height=100)
    complain.place(x=300, y=350, width=400, height=100)
    track.place(x=300, y=500, width=400, height=100)
    
    mainloop()