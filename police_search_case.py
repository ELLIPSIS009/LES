from police_search_caseEdit import*

def fest(p,i,i1,i2,i3):
    t=tk.Tk()
    t.title('LES CASE')
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(t, image=bg)
    label1.place(x=-10, y=-10)
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def edit():
        t.destroy()
        fest1(p,i, i1, i2, i3)

    def back():
        t.destroy()
        from police_dashboard import police_dashboard
        police_dashboard(p)

    fih = tkFont.Font(family="Times New Roman", size=20)
    victim=Label(t, text='Name of victim',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    od=Label(t, text='OPENING DATE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    address=Label(t, text='CASE ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    victim1=Label(t,text=i2[0][1],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid" ,width=27,height=2)
    od1=Label(t,text=i[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    address1=Label(t,text=i2[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=27,height=2)
    case_id=Label(t, text='Criminal ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    status=Label(t, text='COMPLAINT ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    case_id1=Label(t,text=i2[0][0],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    status1=Label(t,text=i[0][7],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    desc=Label(t, text='DESCRIPTION',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    desc1=Label(t,text=i[0][4],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    cd=Label(t, text='CLOSING DATE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    cd1=Label(t,text=i[0][6],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    OptionList=[i3[0][1]]
    v = tk.StringVar(t)
    v.set('FIR NUMBER ')
    fir= tk.OptionMenu(t, v, *OptionList)
    OptionList2=[i1[0][1]]
    v2 = tk.StringVar(t)
    v2.set('POLICE ID')
    police_id= tk.OptionMenu(t, v2, *OptionList2)
    # v3 = tk.StringVar(t)
    # v3.set('PENAL NUMBER')
    ps=Label(t, text='POLICE STATION',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    ps1=Label(t,text=i[0][3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    age=Label(t, text='AGE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    age1=Label(t,text=i2[0][4] ,font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    editt = Button(t, text='EDIT',font=tkFont.Font(family="Times New Roman", size=16), command=edit, borderwidth=2, relief="solid", width=15,height=2)
    back_button = Button(t, text='GO BACK',font=fih, command=back, borderwidth=2, relief="solid", width=26, height=2).place(x=950, y=700)
    victim.place(x=50, y=500)
    victim1.place(x=300, y=500)
    age.place(x=50, y=175)
    age1.place(x=300, y=175)
    address.place(x=50, y=240)
    address1.place(x=300, y=240)
    case_id.place(x=50, y=110)
    case_id1.place(x=300, y=110)
    status.place(x=50, y=630)
    status1.place(x=300, y=630)
    police_id.place(x=850, y=110, width=300, height=70)
    fir.place(x=850, y=210, width=300, height=70)
    desc.place(x=50, y=565)
    desc1.place(x=300, y=565)
    ps.place(x=50, y=430)
    ps1.place(x=300, y=430)
    od.place(x=50, y=305)
    od1.place(x=300, y=305)
    cd.place(x=50, y=370)
    cd1.place(x=300, y=370)
    editt.place(x=950, y=600)
    mainloop()