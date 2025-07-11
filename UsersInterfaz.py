from tkinter import *
from tkinter import messagebox
import dbcontacto as dbcto
import contactop as cto
import fmContacto as fm
import Usuarios as us
import InterfazMenu

flag = 0

class App(Tk):
    def __init__(self,rol="Nuevo"):
        super().__init__()
        self.title("Registrar usuario")
        self.geometry("300x300")
        self.rol_actual = rol

        Label(self, text="User ID").grid(row=0,column=0,padx=5,pady=5)
        self.entry_ID = Entry(self, width=30,state="disabled")
        self.entry_ID.grid(row=0, column=1, padx=5, pady=5)

        Label(self, text="Nombre").grid(row=1,column=0,padx=5,pady=5)
        self.entry_nombre = Entry(self, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        Label(self, text="User name").grid(row=2,column=0,padx=5,pady=5)
        self.entry_username = Entry(self, width=30)
        self.entry_username.grid(row=2, column=1, padx=5, pady=5)

        Label(self, text="Password").grid(row=3,column=0,padx=5,pady=5)
        self.entry_password = Entry(self, width=30)
        self.entry_password.grid(row=3, column=1, padx=5, pady=5)

        Label(self, text="Perfil").grid(row=4,column=0,padx=5,pady=5)
        self.entry_perfil = Entry(self, width=30,state="readonly")
        self.entry_perfil.grid(row=4, column=1, padx=5, pady=5)
        self.entry_perfil.insert(0, self.rol_actual)

        self.buttonGuardar = Button(self, text="Guardar",command=self.Guardar)
        self.buttonGuardar.grid(row=5,column=0,padx=5,pady=5)

        self.buttonEditarBien = Button(self,text="Confirmar cambio",command=self.EditarBIEN,state="disabled")
        self.buttonEditarBien.grid(row=6,column=1,padx=5,pady=5)
        
        self.buttonEditar1 = Button(self,text="Editar",command=self.Editar1)
        self.buttonEditar1.grid(row=5,column=1,padx=5,pady=5)

        self.buttonVisualizar = Button(self,text="Buscar",command=self.visualizar)
        self.buttonVisualizar.grid(row=6,column=0,padx=5,pady=5)

        self.buttonEliminar1 = Button(self,text="Eliminar",command=self.Eliminar1)
        self.buttonEliminar1.grid(row=7,column=0,padx=5,pady=5)

        self.buttonEliminar = Button(self,text="Confirmar eliminacion",command=self.eliminar,state="disabled")
        self.buttonEliminar.grid(row=7,column=1,padx=5,pady=5)

        

        self.dbcto = dbcto.dbcontacto()
    

    def Guardar(self):
        try:
            us_ = us.usuarios()
            us_.setNombre(self.entry_nombre.get())
            us_.setUserName(self.entry_username.get())
            us_.setPassword(self.entry_password.get())
            us_.setPerfil(self.rol_actual)


            print(us_.setNombre(self.entry_nombre.get()))

            if(self.entry_nombre.get()) == "":
               messagebox.showerror("Error","Escribe un nombre") 
               return
            if(self.entry_username.get()) == "":
               messagebox.showerror("Error","Escribe un username") 
               return
            if(self.entry_password.get()) == "":
               messagebox.showerror("Error","Escribe un pass") 
               return
            print("ola")

            self.dbcto.guardarUsuario(us_)
            messagebox.showinfo("Contacto","Contacto guardado correctamente")
            
            self.entry_nombre.delete(0, END)
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)
            

        except ValueError:
            messagebox.showerror("Error","Ingresa un número en el campo ID")
            print("Error: Ingresa un número válido en el campo ID.")

    def EditarBIEN(self):
        try:
            us_ = us.usuarios()
            us_.setID(self.entry_ID.get())
            us_.setNombre(self.entry_nombre.get())
            us_.setUserName(self.entry_username.get())
            us_.setPassword(self.entry_password.get())
            us_.setPerfil(self.entry_perfil.get())
            
            self.dbcto.editarUsuario(us_)
            print("Exito")
            messagebox.showinfo("Edit","Editado correctamente")

            self.entry_ID.delete(0,END)
            self.entry_nombre.delete(0, END)
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)
            self.entry_perfil.delete(0, END)

            self.entry_ID.config(state="disabled")
            self.buttonEditarBien.config(state="disabled")
            self.buttonEditar1.config(state="normal")
            self.entry_perfil.config(state="readonly")

        except ValueError:
            print("Error")
    
    def Editar1(self):
        self.buttonEditarBien.config(state="normal")
        self.buttonEditar1.config(state="disabled")
        self.entry_ID.config(state="normal")
        self.entry_perfil.config(state="normal")

    def visualizar(self):
        contd = us.usuarios()
        contd.setNombre(self.entry_nombre.get())
        contd = self.dbcto.buscarUsuario(contd)

        print("ola")
        if contd != None:
            self.entry_ID.config(state="normal")
            self.entry_ID.delete(0,END)
            self.entry_ID.insert(0,str(contd.getID()))
            self.entry_ID.config(state="disabled")
            self.entry_nombre.delete(0,END)
            self.entry_nombre.insert(0,str(contd.getNombre()))
            self.entry_username.delete(0,END)
            self.entry_username.insert(0,contd.getUserName())
            self.entry_password.delete(0,END)
            self.entry_password.insert(0,contd.getPassword())
            self.entry_perfil.config(state="normal")
            self.entry_perfil.delete(0,END)
            self.entry_perfil.insert(0,contd.getPerfil())
            self.entry_perfil.config(state="readonly")

        else:
            messagebox.showerror("ERROR","Contacto no encontrado")
        
    def eliminar(self):
        try:
            us_ = us.usuarios()
            us_.setID(int(self.entry_ID.get()))
            
            self.dbcto.eliminarUsuario(us_)
            messagebox.showinfo("Contacto","Contacto eliminado")

            self.entry_ID.delete(0,END)
            self.entry_nombre.delete(0,END)
            self.entry_username.delete(0,END)
            self.entry_password.delete(0,END)
            self.entry_perfil.config(state="normal")
            self.entry_perfil.delete(0,END)
            self.entry_perfil.config(state="readonly")

            self.buttonEliminar1.config(state="normal")
            self.buttonEliminar.config(state="disabled")
            self.entry_ID.config(state="disabled")
            self.buttonEditarBien.config(state="disabled")
            self.buttonEditar1.config(state="normal")
            
        except ValueError:
            print("Error")

    def Eliminar1(self):
        self.buttonEliminar1.config(state="disabled")
        self.buttonEliminar.config(state="normal")
        self.buttonEditar1.config(state="disabled")
        self.entry_ID.config(state="normal")

if __name__ == "__main__":
    Users = App()
    Users.mainloop()