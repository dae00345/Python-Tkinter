from tkinter import *           #import modul tkinter

window = Tk()           #deklarasi window
window.geometry("360x480")
window.title("WhatsApp")        #Judul Program
icon = PhotoImage(file="img.png") #input gambar
window.iconphoto(True,icon)             # mengganti icon gui
window.config(background="Grey")            #mengganti warna background 
window.mainloop()            #memunculkan window di layar