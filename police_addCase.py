from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import sqlite3
connection = sqlite3.connect('LES.db')
cursor = connection.cursor()

def add4(p,cid):
    t = tk.Tk()
    t.title('LES ADD CASE')
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(t, image=bg)
    label1.place(x=-10, y=-10)
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def add5():
        cursor.execute("INSERT INTO CASE1  VALUES(?,?,?,?,?,?,?,?)", (case_id1.get(), pno1.get(), sn1.get(), ps1.get(), desc1.get(), od1.get(), cd1.get(), cid))
        connection.commit()
        cursor.execute("INSERT INTO CASE2 VALUES(?,?)", (case_id1.get(), pi1.get()))
        connection.commit()
        cursor.execute("INSERT INTO CASE3 VALUES(?,?,?,?,?,?)", (case_id1.get(), victim1.get(),victim2.get(),victim3.get(),age1.get(),address1.get()))
        connection.commit()
        cursor.execute("INSERT INTO CASE4 VALUES(?,?)", (case_id1.get(), fr1.get()))
        cursor.execute('UPDATE COMPLAINT set STATUS="Case Accepted" where COMPLAINT_NO=?', (cid,))
        connection.commit()
        tkinter.messagebox.showinfo('Confirmation', 'created')
        t.destroy()
        from police_dashboard import police_dashboard
        police_dashboard(p)

    def back():
        t.destroy()
        from police_dashboard import police_dashboard
        police_dashboard(p)

    fi= tkFont.Font(family="Times New Roman", size=16)
    fih = tkFont.Font(family="Times New Roman", size=20)
    victim = Label(t, text='Name of victim',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    od = Label(t, text='OPENING DATE',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    address = Label(t, text='ADDRESS', font=fi,borderwidth=2, relief="solid", width=15,height=2)
    victim1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid", width = 10)
    victim2 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid", width = 10)
    victim3 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid", width = 10)
    od1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    address1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  relief="solid")
    case_id = Label(t, text='CASE ID',font= fi ,borderwidth=2, relief="solid",width=15, height=2)
    status = Label(t, text='COMPLAINTID',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    case_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    status1 = Label(t, text=cid,font=fi, borderwidth=2, relief="solid", width=15,height=2)
    desc = Label(t, text='DESCRIPTION', font=fi,borderwidth=2, relief="solid", width=15,height=2)
    desc1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    cd = Label(t, text='CLOSING DATE',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    cd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    fr = Label(t, text='FIR NUMBER',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    fr1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    pi = Label(t, text='POLICE ID',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    pi1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    pno = Label(t, text='PENAL NUMBER',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    pno1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,relief="solid")
    sn = Label(t, text='SECTION NUMBER',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,relief="solid")
    back_button = Button(t, text='GO BACK',font=fih, command=back, borderwidth=2, relief="solid", width=20, height=2).place(x=950, y=700)
    ps = Label(t, text='POLICE STATION',font=fi ,borderwidth=2, relief="solid", width=15,height=2)
    ps1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    age = Label(t, text='AGE',font=fi ,borderwidth=2, relief="solid", width=15,height=2)
    age1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    submit = Button(t, text='SUBMIT', command=add5,font=fih, borderwidth=2, relief="solid", width=20,height=2)

    victim.place(x=50,y=465)
    age.place(x=50,y=140)
    address.place(x=50,y=205)
    victim1.place(x=300,y=465)
    victim2.place(x=550,y=465)
    victim3.place(x=800,y=465)
    age1.place(x=300, y=140)
    address1.place(x=300, y=205)
    case_id.place(x=50, y=75)
    fr.place(x=50, y=400)
    fr1.place(x=300,y=400)
    case_id1.place(x=300, y=75)
    pi.place(x=850,y=75)
    pi1.place(x=1100,y=75)
    status.place(x=850,y=205)
    status1.place(x=1100,y=205)
    desc.place(x=50, y=530)
    desc1.place(x=300,y=530)
    ps.place(x=850,y=140)
    ps1.place(x=1100,y=140)
    od.place(x=50, y=270)
    od1.place(x=300,y=270)
    cd.place(x=50, y=270)
    cd1.place(x=300,y=270)
    submit.place(x=950, y=600)
    mainloop()