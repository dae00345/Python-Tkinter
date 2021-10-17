from tkinter import *

window = Tk()
window.geometry("480x360")
window.config(background='grey')
window.title("Whatsapp")
icon = PhotoImage(file='C:\\Users\\Administrator\\Documents\\Ngoding\python\\Tkinter\\Window\\img.png')
window.iconphoto(True,icon)

label1 = Label(window,
	text = 'Shut Up!!',
	font = ('Arial',40,'bold'),
	fg = 'green',
	bg = 'black',
	pady = 20,
	padx = 20,
	relief = RAISED,
	bd = 20)

label2 = Label(window,
	text = 'Erick',
	font = ('Arial',20,'bold'),
	fg = 'black',
	bg = 'yellow',
	pady = 20,
	padx = 30,
	relief = RAISED,
	bd = 20,) 

label1.pack()
label2.pack()
label1.place(x=80,y=0)
label2.place(x=80,y=150)



window.mainloop()