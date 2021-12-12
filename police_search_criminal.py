from police_search_criminalEdit import*
import datetime

def test(p,j, j2, j3,photoPath):
    t = tk.Tk()
    t.title('LES CRIMINAL')
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(t, image=bg)
    label1.place(x=-10, y=-10)
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    born1 = j[0][4]
    sss = born1.split('-')
    mmm = datetime.datetime.today()
    b = mmm.year - int(sss[0])

    def edit():
     t.destroy()
     test1(p,j, j2, j2,photoPath)
     return

    def back():
        t.destroy()
        from police_dashboard import police_dashboard
        police_dashboard(p)

    fih = tkFont.Font(family="Times New Roman", size=20)
    fname = Label(t, text='First Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    fname1 = Label(t, text=j[0][1], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    c_id = Label(t, text='Criminal ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    status = Label(t, text='status',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    c_id1 = Label(t, text=j[0][0], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    status1 = Label(t, text=j[0][5], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    gender = Label(t, text='Gender', font=tkFont.Font(family="Times New Roman", size=16),borderwidth=2, relief="solid",width=18,height=2)
    gender1 = Label(t, text=j[0][6], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid",width=15,height=2)
    v = tk.StringVar(t)
    OptionList2 = [j2[0][1]]
    OptionList3 = [j3[0][1]]
    v2 = tk.StringVar(t)
    v2.set('ADDRESS')
    address = tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('CONTACT')
    hideout = tk.OptionMenu(t, v3, *OptionList3)
    dob = Label(t, text='DATE OF BIRTH',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    dob1 = Label(t, text=j[0][4], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    age = Label(t, text='AGE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    age1 = Label(t, text=b, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid",width=15,height=2)
    editt = Button(t, text='EDIT',font=tkFont.Font(family="Times New Roman", size=20), command=edit, borderwidth=2, relief="solid")
    back_button = Button(t, text='GO BACK', font=fih,command=back, borderwidth=2, relief="solid", width=26, height=2).place(x=950,y=700)
    t.load = Image.open(photoPath)
    t.load = t.load.resize((600, 450), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Label(t, image=t.photo1)
    t.img1.image = t.photo1
    t.img1.place(x=800, y=100, width=600, height=450)
    fname.place(x=50, y=125)
    fname1.place(x=300, y=125)
    c_id.place(x=50, y=190)
    c_id1.place(x=300, y=190)
    status.place(x=50, y=585)
    status1.place(x=300, y=585)
    address.place(x=50, y=485, width=300, height=70)
    hideout.place(x=50, y=400, width=300, height=70)
    gender.place(x=50, y=330)
    gender1.place(x=300, y=330)
    dob.place(x=50, y=260)
    dob1.place(x=300, y=260)
    age.place(x=50, y=650)
    age1.place(x=300, y=650)
    editt.place(x=850, y=720)
    mainloop()