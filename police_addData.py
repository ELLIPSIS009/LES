import tkinter.messagebox
from police_addCrime import *
from police_addCriminal import *
from police_addCase import *

def wii(p):
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("LES ADD DATA")
    bg = PhotoImage(file="wallpaper.png")
    label1 = Label(root, image=bg)
    label1.place(x=-10, y=-10)
    fing = tkFont.Font(family="Times New Roman", size=20)
    fins = tkFont.Font(family="Times New Roman", size=10)
    finm = tkFont.Font(family="Times New Roman", size=16)
    OptionList = ['CRIMINAL', 'FIR', 'CASE']
    v = tk.StringVar(root)
    v.set('ADD BY')
    opti = tk.OptionMenu(root, v, *OptionList)
    opti.place(x=615, y=300, width=350, height=80)
    opti.configure(font=finm, relief="solid")

    def nex():
        if v.get() == 'FIR':
            root.destroy()
            add1(p)
        elif v.get() == 'CRIMINAL':
            root.destroy()
            add2(p)
        elif v.get() == 'CASE':
            root.destroy()
            import police_addData_searchComplaint as tty
            tty.selcomp(p)
        else:
            tkinter.messagebox.showinfo('Title', 'CHOOSE RECORD TYPE')

    def back():
        root.destroy()
        from police_dashboard import police_dashboard
        police_dashboard(p)

    submit = Button(root, text='Submit', font=fing, command=nex, borderwidth=2, relief="solid")
    submit.place(x=680, y=450, width=200, height=70)
    back_button = Button(root, text='BACK', command=back, font=fins, borderwidth=2, relief="solid", width=10, height=2).place(x=50, y=50)
    mainloop()
