from tkinter import *

def display():
	if(x.get()==1):
		print("Kamu Setuju")
	else:
		print("Kamu tidak setuju")

root = Tk()
root.title("Check Button")

x = IntVar()


checkbutton1 = Checkbutton(root,
	text='Setuju',
	variable = x,
	onvalue = 1,
	offvalue = 0,
	command = display,
	font = ('Arial',20,'bold'),
	fg = 'lightgreen',
	bg = 'black',
	activebackground = 'black',
	padx = 20,
	pady = 10)

checkbutton1.pack(side=RIGHT)


root.mainloop()