from tkinter import *
from tkinter import messagebox
import dbcontacto as dbcto
import contactop as cto
import fmContacto
import Usuarios as us
import UsersInterfaz
import Vehiculos
from PIL import Image, ImageTk


class App(Tk):
    def __init__(self, usuario_id):
        super().__init__()
        self.usuario_id = usuario_id
        self.title("Interfaz Secretaria")
        self.geometry("400x300")

        self.background_image = Image.open("Marco.jpg")  
        self.background_image = self.background_image.resize((400, 300), Image.Resampling.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        canvas = Canvas(self, width=400, height=300)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        Label(self, text="BIENVENIDO", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#333").place(x=130, y=20)
        
        self.Barra = Menu(self)

        self.menu = Menu(self.Barra, tearoff=0)
        self.menu.add_command(label="Customer", command=self.customer)
        self.menu.add_command(label="Cars", command=self.cars)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.exit_app)

        self.Barra.add_cascade(label="File", menu=self.menu)

        self.config(menu=self.Barra)

    def users(self, rol):
        messagebox.showinfo("Usuarios", f"Formulario de contacto /  {rol}")
        users_form = UsersInterfaz.App(rol) 
        users_form.mainloop()


    def customer(self):
        messagebox.showinfo("Customer", "Customer")
        contact_form = fmContacto.App(self.usuario_id)  
        contact_form.mainloop()

    def cars(self):
        messagebox.showinfo("Cars", "Cars")
        Carros = Vehiculos.App(self.usuario_id)
        Carros.mainloop()

    def parts(self):
        messagebox.showinfo("Parts", "Parts")

    def exit_app(self):
        self.quit()


if __name__ == "__main__":
    app = App()
    app.mainloop()
