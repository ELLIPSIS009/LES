import tkinter.messagebox
from police_search_criminal import test
from police_search_crime import best
from police_search_criminalEdit import*
from police_search_case import fest

connection = sqlite3.connect('LES.db')
cursor = connection.cursor()

def worst(wi):
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("LES SEARCH")
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(root, image=bg)
    label1.place(x=-10, y=-10)
    fing = tkFont.Font(family="Times New Roman", size=20)
    fins = tkFont.Font(family="Times New Roman", size=10)
    finm = tkFont.Font(family="Times New Roman", size=16)

    OptionList = ['CRIMINAL ID', 'FIR NUMBER', 'CASE ID']
    v = tk.StringVar(root)
    v.set('SEARCH BY')
    opt = tk.OptionMenu(root, v, *OptionList)
    opt.place(x=615, y=300, width=350, height=80)
    opt.configure(font=finm, relief="solid")
    e1 = Entry(root, borderwidth=2, relief="solid",font=tkFont.Font(family="Times New Roman", size=20))
    e1.place(x=642.5, y=450, width=275, height=70)

    def next():
        if v.get() == 'CRIMINAL ID':
            x = e1.get()
            u = cursor.execute('SELECT * FROM CRIMINAL1 where CRIMINALID=(?)', (x,))
            j = u.fetchall()
            q = cursor.execute('SELECT * FROM CRIMINAL2 where CRIMINALID=(?)', (x,))
            j2 = q.fetchall()
            p = cursor.execute('SELECT * FROM CRIMINAL3 where CRIMINALID=(?)', (x,))
            j3 = p.fetchall()
            photo = j[0][7]
            photoPath = "D:\z" + str(20180829_004758) + ".jpg"
            with open(photoPath, 'wb') as file:
                file.write(photo)
            print("Stored blob data into: ", photoPath, "\n")
            if len(j) == 1:
                root.destroy()
                test(wi, j, j2, j3, photoPath)
            else:
                tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')
        elif v.get() == 'FIR NUMBER':
            x = e1.get()
            z = cursor.execute('SELECT * FROM CRIME where FIRNO=(?)', (x,))
            k = z.fetchall()
            z1 = cursor.execute('SELECT * FROM CRIME2 where FIRNO=(?)', (x,))
            k1 = z1.fetchall()
            z2 = cursor.execute('SELECT * FROM CRIME3 where FIRNO=(?)', (x,))
            k2 = z2.fetchall()
            if len(k) == 1:
                root.destroy()
                best(wi, k, k1, k2)
            else:
                tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')
        elif v.get() == 'CASE ID':
            x = e1.get()
            w = cursor.execute('SELECT * FROM CASE1 where CASENO=(?)', (x,))
            i = w.fetchall()
            w1 = cursor.execute('SELECT * FROM CASE2 where CASENO=(?)', (x,))
            i1 = w1.fetchall()
            w2 = cursor.execute('SELECT * FROM CASE3 where CASENO=(?)', (x,))
            i2 = w2.fetchall()
            w3 = cursor.execute('SELECT * FROM CASE4 where CASENO=(?)', (x,))
            i3 = w3.fetchall()
            if len(i) == 1:
                root.destroy()
                fest(wi, i, i1, i2, i3)
            else:
                tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')
        return

    submit = Button(root, text='Submit', font=fing,command=next, borderwidth=2, relief="solid")
    submit.place(x=680, y=600, width=200, height=70)

    def back():
        root.destroy()
        from police_dashboard import police_dashboard
        police_dashboard(wi)

    back = Button(root, text='BACK',font=fins,command=back, borderwidth=2, relief="solid", width=10, height=2)
    back.place(x=50, y=50)

    root.mainloop()