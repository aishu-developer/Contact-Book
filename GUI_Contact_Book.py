#IMPORTING LIBRARY:-
from tkinter import *
#INITIALIZE WINDOW:-
root=Tk()
root.geometry('400x400')
root.config(bg='SlateGray3')
root.title("Contact Book")
root.resizable(0,0)
#CREATE DICTIONARY:-
contactList=[
    ['sample','1234567890'],
    ['sita','44567832255']
    ]
Name=StringVar()
Number=StringVar()
#CREATE FRAME:-
frame=Frame(root)
frame.pack(side=RIGHT)
scroll=Scrollbar(frame,orient=VERTICAL)
select=Listbox(frame,yscrollcommand=scroll.set,height=12)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
scroll.pack(side=LEFT,fill=BOTH,expand=1)
#FUNCTIONS REQUIRED:-
def Selected():
    return int(select.curselection()[0])
def AddContact():
    contactList.append([Name.get(),Number.get()])
    Select_set()
def EDIT():
    contactList[Selected()]=[Name.get(),Number.get()]
    Select_set()
def DELETE():
    del contactList[Selected()]
    Select_set()
def VIEW():
    NAME,PHONE=contactList[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
def EXIT():
    root.destroy()
def RESET():
    Name.set('')
    Number.set('')
def Select_set():
    contactList.sort()
    select.delete(0,END)
    for name,phone in contactList:
        select.insert(END,name)
Select_set()
#BUTTONS,LABELS,ENTRY WIDGET:-
Label(root,text='NAME',font='arial  12 bold').place(x=30,y=20)
Entry(root,textvariable=Name).place(x=100,y=20)
Label(root,text='PHONE NO.',font='arial  12 bold').place(x=30,y=70)
Entry(root,textvariable=Number).place(x=130,y=70)
Button(root,text="ADD",font='arial  12 bold',bg='Grey',command=AddContact).place(x=50,y=110)
Button(root,text="EDIT",font='arial  12 bold',bg='Grey',command=EDIT).place(x=50,y=260)
Button(root,text="DELETE",font='arial  12 bold',bg='Grey',command=DELETE).place(x=50,y=210)
Button(root,text="VIEW",font='arial  12 bold',bg='Grey',command=VIEW).place(x=50,y=160)
Button(root,text="EXIT",font='arial  12 bold',bg='Grey',command=EXIT).place(x=300,y=320)
Button(root,text="RESET",font='arial  12 bold',bg='Grey',command=REST).place(x=50,y=310)

root.mainloop()
       
