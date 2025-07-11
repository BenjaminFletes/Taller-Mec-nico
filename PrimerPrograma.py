from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")
root.title("Practica Hola mundo")

Nombre = Label(root,text="Ingrese su nombre")
Nombre.place(x=10,y=20)

txNombre = Entry(root, width=20)
txNombre.place(x=10,y=50)

BotonMostrar = Button(root,text="Mostrar",command=lambda:mensaje(txNombre.get()))
BotonMostrar.place(x=10,y=80)

def mensaje(nombre):
    messagebox.showinfo(title="Resultado",message="Hola: "+nombre)


root.mainloop()