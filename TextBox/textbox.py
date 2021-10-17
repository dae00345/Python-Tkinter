from tkinter import *
from os import system

def cls():
	return system('cls')

def submit():
	username = entry.get()
	cls()
	print("Hallo:",username,"Anda Keren Sekali")
	entry.config(state=DISABLED)

def delete():
	entry.delete(0,END)

def backspace():
	entry.delete(len(entry.get())-1,END)

root = Tk()
root.title('TextBox')
root.config(background='dark grey')

label1 = Label(root,text='TEXTBOX',fg = 'deepskyblue',font = ('Forte',20,'bold'),bg = 'dark grey',bd = 20)
label1.pack()


entry = Entry(root,font = ('Arial',20,'bold'),fg = 'lightgreen',bg = 'black',relief = RAISED,bd=10)
entry.pack(side=LEFT)

submitBtn = Button(root,text='Sumbit',fg = 'black',bg = 'yellow',command = submit)
submitBtn.pack(side=TOP)

delBtn = Button(root,text='Delete',fg = 'black',bg='salmon',command = delete)
delBtn.pack(side=RIGHT)

backspaceBtn = Button(root,text='Backspace',fg='black',bg='salmon',command = backspace)
backspaceBtn.pack(side=RIGHT)

root.mainloop()