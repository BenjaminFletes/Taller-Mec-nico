from tkinter import *
from tkinter import messagebox, OptionMenu, StringVar
import dbcontacto as dbcto
import contactop as cto
import fmContacto
import Usuarios as us
import UsersInterfaz
import InterfazSecretaria

class App(Tk):
    def __init__(self,usuario_id):
        super().__init__()
        self.title("Vehiculos")
        self.geometry("500x300")
        self.usuario_id = usuario_id
        print(usuario_id)
    

        Label(self,text="Matricula").grid(row=1, column=0, padx=5, pady=5)
        self.MatriculaEntry = Entry(self,width=30) 
        self.MatriculaEntry.grid(row=1, column=1, padx=5, pady=5)
        
        Label(self,text="New").grid(row=1, column=2, padx=5, pady=5)
        self.NewMatriculaEntry = Entry(self,width=20) 
        self.NewMatriculaEntry.grid(row=1, column=3, padx=5, pady=5)
        self.NewMatriculaEntry.config(state="disabled")

        Label(self,text="Cliente").grid(row=2, column=0, padx=5, pady=5)

        self.cliente_var = StringVar(self)
        
        clientes = self.obtener_clientes()

        if clientes:
            self.cliente_var.set(clientes[0])

        self.ClienteEntry = OptionMenu(self, self.cliente_var, *clientes, command=self.actualizar_matricula)

        self.ClienteEntry.config(width=15)
        self.ClienteEntry.grid(row=2, column=1, padx=5, pady=5)

        self.MatriculaText = Text(self,width=7,height=1) 
        self.MatriculaText.grid(row=2, column=2, padx=5, pady=5)

        Label(self,text="Marca").grid(row=3, column=0, padx=5, pady=5)
        self.MarcaEntry = Entry(self,width=30) 
        self.MarcaEntry.grid(row=3, column=1, padx=5, pady=5)

        Label(self,text="Modelo").grid(row=4, column=0, padx=5, pady=5)
        self.ModeloEntry = Entry(self,width=30) 
        self.ModeloEntry.grid(row=4, column=1, padx=5, pady=5)

        Label(self,text="Serie").grid(row=5, column=0, padx=5, pady=5)
        self.SerieEntry = Entry(self,width=30) 
        self.SerieEntry.grid(row=5, column=1, padx=5, pady=5)

        self.buttonCrear = Button(self, text="Buscar", command=self.buttonBuscarCarro)
        self.buttonCrear.place(x=10,y=200)

        self.buttonGuardar = Button(self, text="Guardar", command=lambda:self.buttonCrearr(self.cliente_var.get()))
        self.buttonGuardar.place(x=85,y=200)

        self.buttonCancelar = Button(self, text="Eliminar", command=self.buttonEliminar)
        self.buttonCancelar.place(x=160,y=200)

        self.buttonEditar = Button(self, text="Editar", command=lambda:self.buttonEditarr(self.cliente_var.get()) )
        self.buttonEditar.place(x=235,y=200)

        self.buttonEditar = Button(self, text="EditarMatricula", command=self.buttonEditarrMatricula)
        self.buttonEditar.place(x=380,y=200)

        self.buttonRemoverr = Button(self, text="Remover", command=self.buttonRemover)
        self.buttonRemoverr.place(x=310,y=200)

        print("el usuario es : ",usuario_id)

        if usuario_id != 12:
            self.deshabilitar()

        self.dbcto = dbcto.dbcontacto()

    def deshabilitar(self):
        self.buttonCrear.config(state="disabled")
        self.buttonEditar.config(state="disabled")
        self.buttonRemoverr.config(state="disabled")

    def obtener_clientes(self):
        db = dbcto.dbcontacto()
        clientes = db.buscarCliente()
        print("Clientes obtenidos:", clientes) 
        return clientes
    
    def buttonCrearr(self, cliente_seleccionado):
        try:
            matricula = self.MatriculaEntry.get() 
            if not matricula or not self.SerieEntry.get() or not self.ModeloEntry.get() or not self.MarcaEntry.get():
                messagebox.showerror("Error", "Todos los campos deben ser completados")
                return

            cliente_id = self.buscar_id_cliente(cliente_seleccionado)

            if cliente_id is None:
                messagebox.showerror("Error", "Cliente no encontrado. No se puede guardar el vehículo.")
                return

            us_ = us.usuarios()
            us_.setMatricula(self.MatriculaEntry.get()) 
            us_.setSerie(self.SerieEntry.get())
            us_.setModelo(self.ModeloEntry.get())
            us_.setMarca(self.MarcaEntry.get())
            us_.setClienteID(cliente_id) 

            if cliente_id == 0:
                messagebox.showerror("Error", "El cliente seleccionado no tiene un ID válido.")
                return

            self.dbcto.guardarCarro(us_)
            
            messagebox.showinfo("Vehículo", "Vehículo guardado correctamente")

        except ValueError:
            messagebox.showerror("Error", "Error al ingresar los datos.")

    """def buttonBuscarCarro(self):
        contd = us.usuarios()
        contd.setMatricula(self.MatriculaEntry.get()) 
        contd = self.dbcto.buscarMatricula(contd)  

        if contd is not None:
            self.MatriculaEntry.delete(0, END)
            self.MatriculaEntry.insert(0, str(contd.getMatricula()))  

            self.SerieEntry.delete(0, END)
            self.SerieEntry.insert(0, str(contd.getSerie()))  

            self.MarcaEntry.delete(0, END)
            self.MarcaEntry.insert(0, str(contd.getMarca()))  
            self.ModeloEntry.delete(0, END)
            self.ModeloEntry.insert(0, str(contd.getModelo()))  

            self.MatriculaText.delete(1.0, END)
            self.MatriculaText.insert(1.0, str(contd.getClienteID()))  

            self.cliente_var.set(str(contd.getCliente()))  

        else:
            messagebox.showerror("ERROR", "Vehículo no encontrado")"""

           
    def buttonBuscarCarro(self):
        contd = us.usuarios()
        contd.setMatricula(self.MatriculaEntry.get())  
        contd = self.dbcto.buscarMatricula(contd)  

        if contd is not None:
            self.MatriculaEntry.delete(0, END)
            self.MatriculaEntry.insert(0, str(contd.getMatricula()))  

            self.SerieEntry.delete(0, END)
            self.SerieEntry.insert(0, str(contd.getSerie()))  

            self.MarcaEntry.delete(0, END)
            self.MarcaEntry.insert(0, str(contd.getMarca()))  

            self.ModeloEntry.delete(0, END)
            self.ModeloEntry.insert(0, str(contd.getModelo())) 

            self.MatriculaText.config(state="normal")
            self.MatriculaText.delete(1.0, END)
            self.MatriculaText.insert(1.0, str(contd.getClienteID()))  
            self.MatriculaText.config(state="disabled")

            cliente_id = contd.getClienteID() 
            cliente_nombre = self.dbcto.buscarClientePorID(cliente_id)  

            if cliente_nombre:
                self.cliente_var.set(cliente_nombre) 
            else:
                messagebox.showerror("Error", "Nombre del cliente no encontrado")

        else:
            messagebox.showerror("ERROR", "Vehículo no encontrado")



    def buttonEditarr(self, cliente_seleccionado):
        cliente_id = self.buscar_id_cliente(cliente_seleccionado)

        if not self.MatriculaEntry.get() or not self.SerieEntry.get() or not self.ModeloEntry.get() or not self.MarcaEntry.get():
            messagebox.showerror("Error", "Todos los campos deben ser completados")
            return

        if cliente_id is None:
            messagebox.showerror("Error", "Cliente no encontrado. No se puede editar el vehículo.")
            return

        us_ = us.usuarios()
        us_.setMatricula(self.MatriculaEntry.get())  
        us_.setSerie(self.SerieEntry.get())
        us_.setModelo(self.ModeloEntry.get())
        us_.setMarca(self.MarcaEntry.get())
        us_.setClienteID(cliente_id)  


        self.dbcto.editarCarro(us_)

        messagebox.showinfo("Vehículo", "Vehículo editado correctamente")

    def buttonEditarrMatricula(self):
        us_ = us.usuarios()

        old_matricula = self.MatriculaEntry.get()  
        
        new_matricula = self.NewMatriculaEntry.get() 
        
        if old_matricula == new_matricula:
            messagebox.showerror("Error", "La matrícula nueva es la misma que la actual.")
            return

        us_.setMatricula(new_matricula)  
        us_.setSerie(self.NewMatriculaEntry.get())
        
        self.dbcto.editarMatricula(us_, old_matricula)  

        messagebox.showinfo("Vehículo", "Matrícula editada correctamente")


    def actualizar_matricula(self, cliente_seleccionado):
        cliente_id = self.buscar_id_cliente(cliente_seleccionado)

        if cliente_id is not None:
            self.MatriculaText.delete(1.0, END)  
            self.MatriculaText.insert(1.0, cliente_id)  
        else:
            print("Cliente no encontrado.")  

    def buscar_id_cliente(self, cliente_nombre):
        db = dbcto.dbcontacto()
        cliente_id = db.buscar_id_por_nombre(cliente_nombre)  

        if cliente_id is None:
            print(f"Error: cliente_id no válido para el cliente {cliente_nombre}")
            return None
        
        print(f"Cliente ID: {cliente_id}")  
        return cliente_id
    
    def buttonEliminar(self):
        try:
            matricula = self.MatriculaEntry.get() 

            if not matricula:
                messagebox.showerror("Error", "La matrícula no puede estar vacía.")
                return

            if self.dbcto.tieneReparacionEnCurso(matricula):
                messagebox.showerror("Error", "No se puede eliminar el vehículo, ya tiene una reparación en curso.")
                return

            us_ = us.usuarios()  
            us_.setMatricula(matricula) 

            self.dbcto.eliminarMatricula(us_)

            messagebox.showinfo("Contacto", "Vehículo eliminado correctamente")

            self.MatriculaEntry.delete(0, END)
            self.SerieEntry.delete(0, END)
            self.ModeloEntry.delete(0, END)
            self.MarcaEntry.delete(0, END)
            self.MatriculaText.delete(0, END)

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", "Hubo un problema al eliminar el vehículo.")

    def buttonRemover(self):
        self.MatriculaEntry.delete(0, END)
        self.SerieEntry.delete(0, END)
        self.ModeloEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.MatriculaText.delete("1.0", END)  
        self.cliente_var.set('')  



if __name__ == "__main__":
    app = App()
    app.mainloop()