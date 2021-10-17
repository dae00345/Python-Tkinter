from tkinter import *
from os import system

def cls():
    return system('cls')

def submit():
    cls()
    print("SUHU SEKARANG ADALAH",str(scale.get()),"DERAJAT CELSCIUS")

root = Tk()
root.title("Scale")
root.config(background='darkgrey')

scale = Scale(root,from_=0,
to=100,
orient=HORIZONTAL,
tickinterval=10,
length= 600,
font=('consolas',20),
resolution= 1,
showvalue=0,
bg = 'darkgrey')

scale.pack()

submitBtn = Button(root,
text='Submit',
font = ('Arial',15,'bold'),
padx=2,
pady=2,
bd=3,
width = 20,
fg = 'black',
bg = 'deepskyblue',
command= submit)

submitBtn.pack()

root.mainloop()