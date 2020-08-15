from tkinter import *
import tkinter.font as tkFont

lightBlue = '#EDF7F6'       #hex code for light blue color

window = Tk()

window.title("Thermodynamic Property Calculator")

photo = PhotoImage(file = "ThermoProperties/FaviconRocket2.png")
window.iconphoto(False, photo)
window.geometry('800x500')

Font1 = tkFont.Font(family="Arial", size=40)
lbl1 = Label(window, text="Hello", font = Font1)
lbl1.config(anchor=CENTER)
lbl1.pack()

btn1 = Button(window, text="This is Button widget", fg='blue')
btn1.config(x=80, y=100)



window.mainloop()