



#


from tkinter import *
from phoneList import *
from tkinter import messagebox


def whichSelected():
    print("At %s of %d" % (select.curselection(), len(phonelist)))
    return int(select.curselection()[0])


def addEntry():
    phonelist.append([nameVar.get(), phoneVar.get()])
    setSelect()


def updateEntry():
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect()


def deleteEntry():
    del phonelist[whichSelected()]
    setSelect()


def loadEntry():
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)


def About():
    messagebox.showinfo("Om appen", "Din telefonbok....")


def makeWindow():
    global nameVar, phoneVar, select
    win = Tk()
    win.title("Telefonbok")
    win.geometry("500x300")
    w = Label(win, text="Skriv in namn och telefonummer :)", bg="green")
    win.wm_attributes('-topmost', 1)
    w.pack()
    menu = Menu(win)
    win.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Om", command=About)
    filemenu.add_separator()
    filemenu.add_command(label="Avsluta", command=win.quit)

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Namn").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Telefon").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame2 = Frame(win)
    frame2.pack()
    b1 = Button(frame2, text=" Addera  ", command=addEntry)
    b2 = Button(frame2, text="Updatera", command=updateEntry)
    b3 = Button(frame2, text="Radera", command=deleteEntry)
    b4 = Button(frame2, text=" Visa ", command=loadEntry)
    b1.pack(side=LEFT);
    b2.pack(side=LEFT)
    b3.pack(side=LEFT);
    b4.pack(side=LEFT)

    frame3 = Frame(win)
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win


def setSelect():
    phonelist.sort()
    select.delete(0, END)
    for name, phone in phonelist:
        select.insert(END, name)


win = makeWindow()
setSelect()
win.mainloop()
