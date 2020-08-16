from tkinter import *

window = Tk()

window.title("Thermodynamic Property Calculator")

photo = PhotoImage(file = "ThermoProperties/FaviconRocket2.png")
window.iconphoto(False, photo)
window.geometry('1000x200')

lbl = Label(window, text="Hello")
lbl.grid(column=500, row=100)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

window.mainloop()