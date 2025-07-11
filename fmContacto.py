from tkinter import *
from tkinter import messagebox
import dbcontacto as dbcto
import contactop as cto
import re

class App(Tk):
    def __init__(self, usuario_id):
        super().__init__()
        self.title("Formulario de Contacto")
        self.geometry("400x300")

        self.usuario_id = usuario_id
        
        print("ID del Usuario en InterfazSecretaria: ", self.usuario_id)  

        Label(self, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = Entry(self, width=30)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        Label(self, text="Usuario ID").grid(row=1, column=0, padx=5, pady=5)
        self.entry_usuarioID = Entry(self, width=30)
        self.entry_usuarioID.grid(row=1, column=1, padx=5, pady= 5)
        self.entry_usuarioID.insert(0, str(self.usuario_id))
        self.entry_usuarioID.config(state="disabled")

        Label(self, text="Nombre:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_nombre = Entry(self, width=30)
        self.entry_nombre.grid(row=2, column=1, padx=5, pady=5)

        Label(self, text="Telefono:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_telefono = Entry(self, width=30)
        self.entry_telefono.grid(row=3, column=1, padx=5, pady=5)

        Label(self, text="RFC").grid(row=4, column=0, padx=5, pady=5)
        self.entry_RFC = Entry(self, width=30)
        self.entry_RFC.grid(row=4, column=1, padx=5, pady=5)

        

        self.buttonSalvar = Button(self, text="Guardar", command=self.buttonSalvarclik)
        self.buttonSalvar.grid(row=5, column=2, columnspan=2, pady=10)

        Label(self, text="Buscar ID:").grid(row=6, column=0, padx=5, pady=5)
        self.entry_IDE = Entry(self, width=30)
        self.entry_IDE.grid(row=6, column=1, padx=5, pady=5)

        self.buttonBus = Button(self, text="Buscar", command=self.btn_bus_cl)
        self.buttonBus.grid(row=7, column=1, padx=5, pady=5)

        self.buttonEditarr = Button(self, text="Editar", command=self.buttonEditar)
        self.buttonEditarr.grid(row=7,column=0,padx=5, pady=5)

        self.buttonEliminarr = Button(self, text="Eliminar", command=self.buttonEliminar)
        self.buttonEliminarr.grid(row=8,column=0,padx=5,pady=5)

        self.buttonConfirmar = Button(self,text="Confirmar edit", command=self.confirmarEdit)
        self.buttonConfirmar.grid(row=8,column=1,padx=5,pady=5)

        self.buttonCrear = Button(self,text="Crear",command=self.CrearCliente)
        self.buttonCrear.grid(row=5, column=0, columnspan=2, pady=10)

        if usuario_id != 1:
            self.deshabilitar()

        self.dbcto = dbcto.dbcontacto()

    def deshabilitar(self):
        self.buttonConfirmar.config(state="disabled")
        self.buttonEditarr.config(state="disabled")
        self.buttonEliminarr.config(state="disabled")

    def CrearCliente(self):
        self.entry_usuarioID.config(state="normal")
        self.entry_usuarioID.delete(0, END)
        self.entry_usuarioID.insert(0, str(self.usuario_id))
        self.entry_usuarioID.config(state="disabled")


    def buttonEditar(self):
        try:
            print()
            cto_ = cto.contacto()
            cto_.setNombre(self.entry_nombre.get())
            cto_.setID(int(self.entry_IDE.get()))
            cto_.setUsuarioID(self.entry_usuarioID.get())
            cto_.setTelefono(self.entry_telefono.get())
            cto_.setRFC(self.entry_RFC.get())
            
            self.dbcto.editar(cto_)
            print("Exito")

        except ValueError:
            messagebox.showerror("Error","Ingresa un ID")

    def buttonEliminar(self):
        try:
            cto_ = cto.contacto()
            cto_.setID(int(self.entry_IDE.get()))
            
            self.dbcto.eliminar(cto_)
            messagebox.showinfo("Contacto","Contacto eliminado")
            
            self.entry_id.delete(0, END)
            self.entry_usuarioID.delete(0, END)
            self.entry_nombre.delete(0, END)
            self.entry_telefono.delete(0, END)
            self.entry_RFC.delete(0, END)

        except ValueError:
            print("Error")

    def buttonSalvarclik(self):
        try:
            cto_ = cto.contacto()
            self.entry_usuarioID.insert(0, str(self.usuario_id))
            cto_.setID(int(self.entry_id.get())) 
            nombre = self.entry_nombre.get()
            if not self.validar_nombre(nombre):
                return  

            if self.dbcto.buscarID(int(self.entry_id.get())):  
                messagebox.showerror("ERROR", "Se repite el ID. Este contacto ya existe.")
                return

            cto_.setUsuarioID(self.entry_usuarioID.get())
            cto_.setNombre(self.entry_nombre.get())
            cto_.setTelefono(self.entry_telefono.get())
            cto_.setRFC(self.entry_RFC.get())

            if(self.entry_telefono.get) == "":
                messagebox.showerror("Error","Ingresa un nombre")
                return
            if(self.entry_RFC.get) == "":
                messagebox.showerror("Error","Ingresa un nombre")
                return
            if(self.entry_nombre.get) == "":
                messagebox.showerror("Error","Ingresa un nombre")
                return

            self.dbcto.salvar(cto_)
            messagebox.showinfo("Contacto", "Contacto guardado correctamente")

            self.entry_id.delete(0, END)
            self.entry_nombre.delete(0, END)
            self.entry_telefono.delete(0, END)
            self.entry_RFC.delete(0, END)

        except ValueError:
            print("Error: Ingresa un número válido en el campo ID.")


    def btn_bus_cl(self):
        contd = cto.contacto()
        contd.setID(int(self.entry_IDE.get()))
        contd = self.dbcto.buscar(contd)

        print("ola")
        if contd != None:
            self.entry_id.delete(0,END)
            self.entry_id.insert(0,str(contd.getID()))
            self.entry_usuarioID.config(state="normal")
            self.entry_usuarioID.delete(0,END)
            self.entry_usuarioID.insert(0,str(contd.getUsuarioID()))
            self.entry_usuarioID.config(state="disabled")
            self.entry_nombre.delete(0,END)
            self.entry_nombre.insert(0,contd.getNombre())
            self.entry_telefono.delete(0,END)
            self.entry_telefono.insert(0,contd.getTelefono())
            self.entry_RFC.delete(0,END)
            self.entry_RFC.insert(0,contd.getRFC())
            

        else:
            messagebox.showerror("ERROR","Contacto no encontrado")

    def validar_nombre(self, nombre):
        if re.search(r'\d', nombre):
            messagebox.showerror("Error", "El nombre no puede tener numeros")
            return False
        return True
    
    def confirmarEdit(self):
        self.entry_usuarioID.config(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()
