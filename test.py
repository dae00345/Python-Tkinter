from tkinter import *
from os import system

def cls():
    return system('cls')

def order():
    if(x.get()==0):
        cls()
        print("Anda Memesan Pizza")
    elif(x.get()==1):
        cls()
        print("Anda Memesan Martabak")
    elif(x.get()==2):
        cls()
        print("Anda Memesan Terang Bulan")
    else:
        print("huh")

root = Tk()
root.title("Testing")
root.config(background='darkgrey')

pesanan = ['PIZZA','MARTABAK','TERANG BULAN']

x = IntVar()

label1 = Label(root,
text='TESTING',
font=('Arial',
20,'bold'),
fg='lightgreen',
bg='darkgrey',
relief=RAISED,)

label1.pack(side=TOP)

for i in range(len(pesanan)):
    radioBtn = Radiobutton(root,
    text=pesanan[i],
    fg='salmon',
    bg='black',
    indicatoron=0,
    font = ('Arial',30,'bold'),
    variable= x,
    value= i,
    width=20,
    activeforeground='deepskyblue',
    activebackground='darkgrey',
    command=order)

    radioBtn.pack(side=TOP)

root.mainloop()