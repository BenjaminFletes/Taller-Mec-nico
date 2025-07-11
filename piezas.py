from tkinter import *
from tkinter import messagebox, OptionMenu, StringVar
import dbcontacto as dbcto
import contactop as cto
import fmContacto
import Usuarios as us
import UsersInterfaz
import InterfazSecretaria
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk    
from tkinter import Menu, Toplevel, messagebox, Frame
from tkinter import ttk
from datetime import date
from tkcalendar import Calendar
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import selfReparaciones as rep
import re


class App(Tk):
    def __init__(self):
        super().__init__() 
        self.geometry("500x500")
        self.title("Gestión de Piezas")
        
        #self.background_image = Image.open("FondoCaricatura.png") 
        #self.background_image = self.background_image.resize((500, 500), Image.Resampling.LANCZOS)
        #self.background_photo = ImageTk.PhotoImage(self.background_image)

        #canvas = Canvas(self, width=500, height=500)
        #canvas.pack(fill=BOTH, expand=True)
        #canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        frame = Frame(self, bg="white", bd=10)
        frame.place(relwidth=0.85, relheight=0.75, relx=0.075, rely=0.1) 

        Label(frame, text="ID", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.piezaIDEntry = Entry(frame, width=20, font=("Arial", 12))
        self.piezaIDEntry.grid(row=0, column=1, padx=10, pady=10)

        Label(frame, text="Descripción", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.DescripcionEntry = Text(frame, width=20, height=3, font=("Arial", 12))
        self.DescripcionEntry.grid(row=1, column=1, padx=10, pady=10)

        Label(frame, text="Existencias", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.ExistenciasEntry = Entry(frame, width=20, font=("Arial", 12))
        self.ExistenciasEntry.grid(row=2, column=1, padx=10, pady=10)

        # Botones
        self.BGuardarPieza = Button(frame, text="Guardar", command=self.guardar, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.BGuardarPieza.grid(row=3, column=0, padx=10, pady=20)

        self.BEliminarPieza = Button(frame, text="Eliminar", command=self.eliminar, font=("Arial", 12), bg="#FF5722", fg="white")
        self.BEliminarPieza.grid(row=3, column=1, padx=10, pady=20)

        self.BEditarPieza = Button(frame, text="Editar", command=self.editar, font=("Arial", 12), bg="#FF9800", fg="white")
        self.BEditarPieza.grid(row=3, column=2, padx=10, pady=20)

        self.dbcto = dbcto.dbcontacto()

    def guardar(self):
        try:
            pieza_ = rep.reparaciones()
            pieza_.setpiezaID(self.piezaIDEntry.get())
            pieza_.setDescripcion(self.DescripcionEntry.get("1.0", "end-1c"))
            pieza_.setExistencias(self.ExistenciasEntry.get())

            self.dbcto.guardarPieza(pieza_)
            messagebox.showinfo("Pieza","Pieza guardado correctamente")
            
            self.DescripcionEntry.delete(0, END)
            self.ExistenciasEntry.delete(0, END)

        except Exception as e:
            print(f"Error: {e}")

    def eliminar(self):
        try:
            pieza_ = rep.reparaciones()
            pieza_.setpiezaID(self.piezaIDEntry.get())

            self.dbcto.eliminarPieza(pieza_)
            messagebox.showinfo("Pieza","Contacto eliminado correctamente")
            
            self.DescripcionEntry.delete(0, END)
            self.ExistenciasEntry.delete(0, END)

        except Exception as e:
            print(f"Error: {e}")

    def editar(self):
        try:
            pieza_ = rep.reparaciones()
            pieza_.setDescripcion(self.DescripcionEntry.get("1.0", "end-1c"))
            pieza_.setExistencias(self.ExistenciasEntry.get())
            
            self.dbcto.editarPieza(pieza_)
            print("Exito")
        except ValueError:
            print("Error")


if __name__ == "__main__":
    app = App()
    app.mainloop()