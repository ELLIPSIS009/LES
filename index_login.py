from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import sqlite3
from ui import *
from civilian_dashboard import civ_home
from police_dashboard import police_dashboard

connection = sqlite3.connect('LES.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS POLICE(POLICEID TEXT PRIMARY KEY CHECK(POLICEID <> ""), PASSWORD TEXT NOT NULL CHECK(PASSWORD <> ""),FNAME TEXT NOT NULL CHECK(FNAME <> ""), MNAME TEXT, LNAME TEXT NOT NULL CHECK(LNAME <> ""), PHOTO BLOB NOT NULL, LASTLOGIN TEXT, EMAILID TEXT NOT NULL CHECK(EMAILID <> ""), JURISDICTION TEXT NOT NULL CHECK(JURISDICTION <> ""), ADDRESS TEXT NOT NULL CHECK(ADDRESS <> ""), GENDER TEXT NOT NULL CHECK(GENDER <> ""), DOB TEXT NOT NULL CHECK(DOB <> ""), BATCH TEXT NOT NULL CHECK(BATCH <> ""), RANK TEXT NOT NULL CHECK(RANK <> ""), MARITALSTATUS TEXT NOT NULL)')
cursor.execute("""CREATE TABLE IF NOT EXISTS POLICE1(POLICEID TEXT, CONTACT TEXT NOT NULL, FOREIGN KEY (POLICEID) REFERENCES POLICE(POLICEID))""")
cursor.execute("""CREATE TABLE IF NOT EXISTS COMPLAINT (COMPLAINT_NO text PRIMARY KEY, PLACEOFCRIME text NOT NULL CHECK(PLACEOFCRIME <> ''), TIMEOFCRIME text, CRIMEDESCRIPTION text, CITY text, POLICESTATION text, STATUS text, VFNAME text, VMNAME text, VLNAME text, AFNAME text, AMNAME text, ALNAME text, USERID text, FOREIGN KEY(USERID) REFERENCES CIVILIAN1(USERID))""")
cursor.execute("""CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY CHECK(USERID <> ''), PASSWORD text NOT NULL CHECK(PASSWORD <> ''), FNAME text, MNAME text, LNAME text, DOB text, GENDER text, MARITALSTATUS text, EMAILID text NOT NULL, OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)""")
cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN2 (USERID text , CONTACT number,FOREIGN KEY (USERID) REFERENCES CIVILIAN1(USERID))')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY, FNAME text, MNAME text, LNAME text, DOB text, STATUS text, GENDER text, PHOTO BLOB NOT NULL)')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE1 (CASENO number PRIMARY KEY, PENALCODETYPE text, SECTIONNUMBER number, POLICESTATION text, DESCRIPTION text NOT NULL, OPENDATE text NOT NULL, CLOSEDATE text, COMPLAINT_NO TEXT, FOREIGN KEY (COMPLAINT_NO) REFERENCES COMPLAINT(COMPLAINT_NO))')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3 (CRIMINALID text, CONTACT text, FOREIGN KEY (CRIMINALID) REFERENCES CRIMINAL1(CRIMINALID))')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE2(CASENO number, POLICEID text, FOREIGN KEY (POLICEID) REFERENCES POLICE(POLICEID), FOREIGN KEY(CASENO) REFERENCES CASE1(CASENO))')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE3(CASENO number , VFNAME text, VMNAME text, VLNAME text, VAGE number, VADDRESS text, FOREIGN KEY (CASENO) REFERENCES CASE1(CASENO))')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE4(CASENO number, FIRNO number, FOREIGN KEY(CASENO) REFERENCES CASE1(CASENO), FOREIGN KEY(FIRNO) REFERENCES CRIME(FIRNO))')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID text, ADDRESS text, FOREIGN KEY (CRIMINALID) REFERENCES CRIMINAL1(CRIMINALID))')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2 (FIRNO number, CRIMINALID number, FOREIGN KEY(FIRNO) REFERENCES CRIME(FIRNO), FOREIGN KEY(CRIMINALID) REFERENCES CRIMINAL(CRIMINALID))')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIME3 (FIRNO number, PENALCODETYPE text, SECTIONNUMBER number, FOREIGN KEY (FIRNO) REFERENCES CRIME(FIRNO))')
cursor.execute( 'CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY, DAMAGEAMOUNT number, INJURED number, DEATHS number, DATEOFCRIME text NOT NULL, PLACEOFCRIME text)')
connection.commit()

t=tk.Tk()
t.title('LES')
t.configure(background = 'white')
bg = PhotoImage(file="wallpaper.png")
label1 = Label(t, image=bg)
label1.place(x=-10, y=-10)
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def enter():
    getuid = uid.get()
    getpswd = pswd.get()
    if v.get()=='Civilian':
        u = cursor.execute('SELECT USERID FROM CIVILIAN1 where USERID=(?) and PASSWORD=(?)', (getuid,getpswd))
        temp=u.fetchall()
        if getuid == temp[0][0] and len(temp)>0:
            clear()
            t.destroy()
            civ_home(getuid)
        else:
            tkinter.messagebox.showinfo('Alert','Incorrect Username or Password')
    elif v.get()=='Police':
        u = cursor.execute('SELECT POLICEID,RANK FROM POLICE where POLICEID=(?) and PASSWORD=(?)', (getuid,getpswd))
        temp=u.fetchall()
        if len(temp)>0:
            if getuid == temp[0][0]:
                if temp[0][1] == 'ACP' or 'CONSTABLE':
                    clear()
                    t.destroy()
                    police_dashboard(getuid)
                else:
                    tkinter.messagebox.showinfo('Alert','Incorrect Username or Password')
        else:
            tkinter.messagebox.showinfo('Alert','Incorrect Username or Password')
    else:
        tkinter.messagebox.showinfo('Title','Choose User Type')

def clear():
    uid.delete(0, 'end')
    pswd.delete(0, 'end')
    v.set('User Type')
    return

def register():
    t.destroy()
    os.system('python registration_page.py')
    return

OptionList=['Police','Civilian']
v = tk.StringVar(t)
v.set('Select User Type'.upper())
opt = tk.OptionMenu(t, v, *OptionList)
fing=tkFont.Font(family="Times New Roman", size=16)
opt.configure(relief="solid",font=tkFont.Font(family="Times New Roman", size=20))
impmsg=Label(t, text='Law Enforcement System',bg='black', fg='white',font=tkFont.Font(family="Times New Roman", size=60), borderwidth=2, relief="solid")
user = Label(t, text='USER ID ',font=fing,borderwidth=2, relief="solid")
password = Label(t, text='PASSWORD',font=fing, borderwidth=2,relief="solid")
uid = Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd = Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
submit = Button(t, text='SUBMIT', command=enter, borderwidth=2, relief="solid")
reset = Button(t, text='CLEAR', command=clear,font=fing, borderwidth=2, relief="solid")
signup = Button(t, text='REGISTER', command=register,font=fing, borderwidth=2, relief="solid")
submit.configure(font=("Times New Roman", 25, 'bold'))
impmsg.place(x=0, y=5, width=w, height=145)
opt.place(x = w/3, y = 300 , width=410, height=70)
user.place(x = w/3, y = 380 , width=200, height=70)
uid.place(x = w/3 + 210, y = 380 , width=200, height=70)
password.place(x = w/3, y = 460 , width=200, height=70)
pswd.place(x = w/3 + 210, y = 460 , width=200, height=70)
submit.place(x = w/3, y = 630, width=410, height=70)
reset.place(x = w/3 + 210, y = 540 , width=200, height=70)
signup.place(x= w/3, y = 540, width = 200, height = 70)
mainloop()