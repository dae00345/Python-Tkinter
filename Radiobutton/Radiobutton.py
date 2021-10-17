from tkinter import *
from os import system

def cls():
	return system('cls')

def order():
	if(x.get()==0):
		cls()
		print("Anda memesan Pisang")
	elif(x.get()==1):
		cls()
		print("Anda memesan Keju"),
	elif(x.get()==2):
		cls()
		print("Anda memesan Peju")
	else:
		cls()
		print("huh?")

root = Tk()
root.title("RadioButton")
root.config(background = 'darkgrey')

#list pilihan makanan
food = ['Pisang','Keju','Peju']
x = IntVar()

label1 = Label(root,
	text='MENU PESANAN',
	font = ('Arial',40,'bold'),
	fg = 'darkblue',
	bg = 'darkgrey')

label1.pack(side=TOP)

for i in range(len(food)):
	radiobutton = Radiobutton(root,
		text = food[i],
		value = i,
		variable = x,
		font = ('impact',40),
		fg = 'lightgreen',
		bg = 'black',
		padx = 10,
		pady = 10,
		indicatoron = 0,
		width = 20,
		command = order)

	radiobutton.pack(side = TOP)

root.mainloop()