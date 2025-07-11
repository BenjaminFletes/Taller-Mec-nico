from tkinter import *
from tkinter import messagebox
import dbcontacto as dbcto
import contactop as cto
import fmContacto 
import Usuarios as us
import InterfazMenu
import InterfazSecretaria
import InterfazMecanico
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Inicio de sesión")
        self.geometry("400x300")
        self.config(bg="#f7f7f7")
        self.resizable(False, False) 

        self.background_image = Image.open("Marco.jpg") 
        self.background_image = self.background_image.resize((400, 300), Image.Resampling.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        canvas = Canvas(self, width=400, height=300)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        Label(self, text="Iniciar sesión", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#333").place(x=130, y=20)

        Label(self, text="Nombre", font=("Arial", 12), bg="#f7f7f7", fg="#333").place(x=40, y=80)
        self.NameEntry = Entry(self, width=20, font=("Arial", 12), bd=2, relief=SOLID)
        self.NameEntry.place(x=140, y=80)

        Label(self, text="Contraseña", font=("Arial", 12), bg="#f7f7f7", fg="#333").place(x=40, y=120)
        self.PassEntry = Entry(self, width=20, font=("Arial", 12), bd=2, relief=SOLID, show="*")
        self.PassEntry.place(x=140, y=120)

        IngresarButton = Button(self, text="Ingresar", command=self.buttonIngresar, font=("Arial", 12), bg="#4CAF50", fg="white", relief=SOLID, width=12, height=2)
        IngresarButton.place(x=140, y=160)

        self.dbcto = dbcto.dbcontacto()
        self.usuario_id = None  # Para guardar el usuario_id


    def buttonIngresar(self):
        try:
            us_ = us.usuarios()
            us_.setNombre(self.NameEntry.get())
            us_.setPassword(self.PassEntry.get())

            u = self.dbcto.ingresar(us_)
            if u:
                perfil = u.getPerfil()
                self.usuario_id = u.getID()
                print("Usuario ID: ", perfil)
                print("Usuario ID: ", self.usuario_id)
                messagebox.showinfo("Contacto","Se logro")
                if perfil == "Secretaria":
                    self.AbrirSecretaria()
                elif perfil == "Admin":
                    self.abrirVentana()
                elif perfil == "Mecanico":
                    self.AbrirMecanico()
            else: 
                messagebox.showerror("Contacto","Falso")

        except:
            messagebox.showerror("ERROR","Usuario no encontrado")
    

    def abrirVentana(self):
        self.destroy()
        InterfazMenu.App(self.usuario_id).mainloop()

    def AbrirSecretaria(self):
        self.destroy()
        InterfazSecretaria.App(self.usuario_id).mainloop()

    def AbrirMecanico(self):
        self.destroy()
        InterfazMecanico.App(self.usuario_id).mainloop()

if __name__ == "__main__":
    Inter = App()
    Inter.mainloop()
