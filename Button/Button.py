from tkinter import *

def clickme():
	print('Tombol Sudah Di Tekan')


root = Tk()

button1 = Button(root,
	text='Click Me',
	command= clickme,
	font = ('Arial',30,'bold'),
	fg = 'green',
	bg = 'black',
	padx = 20,
	pady = 20,
	bd = 20,
	relief = RAISED)

button1.pack()

root.mainloop()