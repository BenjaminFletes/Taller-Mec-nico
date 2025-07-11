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
from tkinter import Toplevel, Label, Entry, Button, OptionMenu, StringVar, messagebox


class App(Tk):
    def __init__(self):  #poner usuario_id despues
        super().__init__()
        self.title("ReparacionesA")
        self.geometry("700x700")
        self.detalles = []
        contador = []
        
        #fondo con la imagen
        #self.background_image = Image.open("imagenes/ReparacionesHouse.jpg")
        #self.background_image = self.background_image.resize((700, 700), Image.Resampling.LANCZOS)
        #self.background_photo = ImageTk.PhotoImage(self.background_image)

        #canvas para el fondo
        canvas = Canvas(self, width=700, height=700)
        canvas.pack(fill=BOTH, expand=True)
        #canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        #frame para los elementos
        frame = Frame(self, bg='white', bd=10)
        frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)  

        self.piezas_var = StringVar(self)
        self.matricula_var = StringVar(self)

        piezas = self.obtener_piezas()
        matricula = self.obtener_matricula()

        if piezas:
            self.piezas_var.set(piezas[0])  
        else:
            piezas = ["No hay piezas disponibles"]  
            self.piezas_var.set(piezas[0])

        if matricula:
            self.matricula_var.set(matricula[0]) 
        else:
            matricula = ["No hay carros disponibles"]  
            self.matricula_var.set(matricula[0])

        # labels y entradas dentro del frame
        Label(frame, text="Pieza", font=("Arial", 14), bg='white').grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.piezasEntry = OptionMenu(frame, self.piezas_var, *piezas, command=self.actualizar_piezaID)
        self.piezasEntry.grid(row=0, column=1, pady=10, padx=10, sticky=W)

        self.piezaID = Text(frame, width=5, height=1, font=("Arial", 12))
        self.piezaID.grid(row=0, column=2, pady=1, padx=1, sticky=W)

        Label(frame, text="Matrícula", font=("Arial", 14), bg='white').grid(row=1, column=0, pady=10, padx=10, sticky=W)
        self.matriculaEntry = OptionMenu(frame, self.matricula_var, *matricula)
        self.matriculaEntry.grid(row=1, column=1, pady=10, padx=10, sticky=W)

        Label(frame, text="ID", font=("Arial", 14), bg='white').grid(row=2, column=0, pady=10, padx=10, sticky=W)
        self.idEntry = Entry(frame, width=30, font=("Arial", 12))
        self.idEntry.grid(row=2, column=1, pady=10, padx=10)

        Label(frame, text="Cantidad", font=("Arial", 14), bg='white').grid(row=3, column=0, pady=10, padx=10, sticky=W)
        self.cantidadEntry = Entry(frame, width=30, font=("Arial", 12))
        self.cantidadEntry.grid(row=3, column=1, pady=10, padx=10)

        Label(frame, text="Fecha de entrada", font=("Arial", 14), bg='white').grid(row=4, column=0, pady=10, padx=10, sticky=W)
        self.FechaEntradaEntry = Entry(frame, width=30, font=("Arial", 12))
        self.FechaEntradaEntry.grid(row=4, column=1, pady=10, padx=10)

        Label(frame, text="Fecha de salida", font=("Arial", 14), bg='white').grid(row=5, column=0, pady=10, padx=10, sticky=W)
        self.FechaSalidaEntry = Entry(frame, width=30, font=("Arial", 12))
        self.FechaSalidaEntry.grid(row=5, column=1, pady=10, padx=10)

        # Listbox para mostrar los detalles
        self.VentanaEntry = Listbox(frame, width=50, height=10)
        self.VentanaEntry.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

        # Botones 
        self.BAgregar = Button(frame, text="Agregar", command=self.AgregarPieza)
        self.BAgregar.grid(row=7, column=0, pady=10, padx=10, sticky=W)

        self.BEliminar = Button(frame, text="Eliminar", command=self.eliminarPieza)
        self.BEliminar.grid(row=7, column=1, pady=10, padx=10, sticky=W)

        self.BGuardarFolio = Button(frame, text="Guardar Folio", command=self.guardarFolio)
        self.BGuardarFolio.grid(row=7, column=2, pady=10, padx=10, sticky=W)

        # Botón para editar reparación
        self.BEditarFolio = Button(frame, text="Editar Reparación",command=self.editarFolio)
        self.BEditarFolio.grid(row=4, column=2, pady=10, padx=10, sticky=W)
        #vton eliminar
        self.BEliminarRep = Button(frame, text="Eliminar reparacion", command=self.eliminarReparacion)
        self.BEliminarRep.grid(row=8, column=0, pady=10, padx=10, sticky=W)
        #voton buscar
        self.BBuscarRep = Button(frame, text="Buscar reparacion", command=self.buscarReparacionPorID)
        self.BBuscarRep.grid(row=8, column=1, pady=10, padx=10, sticky=W)
        #votoneditarfechas
        self.BBuscarRep = Button(frame, text="Editar Fecha/Mat", command=self.editarFechasYMatricula)
        self.BBuscarRep.grid(row=5, column=2, pady=10, padx=10, sticky=W)


        self.dbcto = dbcto.dbcontacto()
        self.folio = self.dbcto.obtenerUltimoFolio()


    def buscarReparacionPorID(self):
        try:
            rep_id = self.idEntry.get()
            if not rep_id:
                messagebox.showerror("Error", "Por favor ingrese un ID de reparación válido.")
                return

            try:
                rep_id = int(rep_id)
            except ValueError:
                messagebox.showerror("Error", "El ID ingresado no es válido.")
                return

            reparacion = self.dbcto.buscarReparacionPorID(rep_id)
            if reparacion is None:
                messagebox.showerror("Error", "No se encontró una reparación con ese ID.")
                return

            self.matricula_var.set(reparacion['matricula'])
            self.FechaEntradaEntry.delete(0, END)  
            self.FechaEntradaEntry.insert(0, reparacion['fecha_entrada'])

            self.FechaSalidaEntry.delete(0, END)  
            self.FechaSalidaEntry.insert(0, reparacion['fecha_salida'])  

            detalles_reparacion = self.dbcto.obtenerDetallesReparacionPorRepID(rep_id)
            if detalles_reparacion:
                self.VentanaEntry.delete(0, END)  

                for detalle in detalles_reparacion:
                    pieza_id = detalle['pieza_id']
                    cantidad = detalle['cantidad']
                    pieza_desc = self.dbcto.buscarPiezaPorID(pieza_id)
                    
                    pieza_desc_str = pieza_desc.getDescripcion()  
                    
                    self.VentanaEntry.insert(END, f"Pieza: {pieza_desc_str} - Cantidad: {cantidad}")
            else:
                self.VentanaEntry.insert(END, "No se encontraron detalles de reparación para este ID.")

            folios_relacionados = self.dbcto.obtenerFoliosPorRepID(rep_id)
            if folios_relacionados:
                for folio in folios_relacionados:
                    self.VentanaEntry.insert(END, f"Folio relacionado: {folio}")
            else:
                self.VentanaEntry.insert(END, "No se encontraron folios relacionados.")

            messagebox.showinfo("Reparación encontrada", f"Se han cargado los detalles de la reparación con ID {rep_id}.")
            
        except Exception as e:
            print(f"Error al buscar la reparación: {e}")
            messagebox.showerror("Error", f"Hubo un problema al buscar la reparación: {e}")

    def editarFechasYMatricula(self):
        try:
            folio_id = self.idEntry.get()
            nueva_matricula = self.matricula_var.get() 
            nueva_fecha_entrada = self.FechaEntradaEntry.get()  
            nueva_fecha_salida = self.FechaSalidaEntry.get() 

            if not folio_id or not nueva_matricula or not nueva_fecha_entrada or not nueva_fecha_salida:
                messagebox.showerror("Error", "Todos los campos deben ser llenados correctamente.")
                return
            
            fecha_entrada = datetime.strptime(nueva_fecha_entrada, "%Y-%m-%d")
            fecha_salida = datetime.strptime(nueva_fecha_salida, "%Y-%m-%d")
            
            if fecha_entrada > fecha_salida:
                messagebox.showerror("Error", "La fecha de entrada no puede ser posterior a la fecha de salida.")
                return

            rep_id = self.dbcto.buscarREPID(folio_id)
            if not rep_id:
                messagebox.showerror("Error", f"No se encontró la reparación con el folio {folio_id}.")
                return

            matricula_id = self.dbcto.buscarMatriculaID(nueva_matricula)
            if not matricula_id:
                messagebox.showerror("Error", "La matrícula proporcionada no existe.")
                return

            self.dbcto.editarReparacion(folio_id, nueva_matricula, nueva_fecha_entrada, nueva_fecha_salida)

            messagebox.showinfo("Éxito", f"Reparación con folio {folio_id} actualizada correctamente.")
            
            self.idEntry.delete(0, END)
            self.matricula_var.set("")
            self.FechaEntradaEntry.delete(0, END)
            self.FechaSalidaEntry.delete(0, END)

        except Exception as e:
            print(f"Error al editar las fechas y matrícula: {e}")
            messagebox.showerror("Error", f"Error al editar las fechas y matrícula:")



    
    def actualizar_piezaID(self, selected_pieza):
        pieza_id = self.dbcto.buscar_id_por_descripcion(selected_pieza) 
        self.piezaID.delete(1.0, END) 
        if pieza_id: 
            self.piezaID.insert(END, str(pieza_id))  

    def obtener_piezas(self):
        try:
            db = dbcto.dbcontacto()
            piezas = db.buscarPieza() 
            if piezas is None: 
                piezas = []
            return piezas 
        except Exception as e:
            print(f"Error al obtener piezas: {e}")
            return [] 

    def obtener_matricula(self):
        try:
            db = dbcto.dbcontacto()
            matriculas = db.buscarMatriculas()  
            if matriculas is None: 
                matriculas = []
            return matriculas 
        except Exception as e:
            print(f"Error al obtener matriculas: {e}")
            return [] 

    def AgregarPieza(self):
        try:
            nuevo_folio = self.generar_folio()  

            pieza_desc = self.piezas_var.get()  
            pieza_cantidad = int(self.cantidadEntry.get()) 
            matriculaSelec = self.matricula_var.get()  

            piezaRecuperada = self.dbcto.buscarPiezaPorDescripcion(pieza_desc) 

            if piezaRecuperada:
                descripcion = piezaRecuperada.getDescripcion()
                existencias = piezaRecuperada.getExistencias() 
                print(existencias)

                nueva_existencia = existencias - pieza_cantidad
                print(nueva_existencia)
                if nueva_existencia >= 0:
                    self.dbcto.actualizarExistenciasAGG(pieza_desc, nueva_existencia)  

                    piezas_agregadas = self.dbcto.obtenerPiezasAgregadas(pieza_desc)

                    nuevas_piezas_agregadas = piezas_agregadas + pieza_cantidad
                    self.dbcto.actualizarPiezasAgregadas(pieza_desc, nuevas_piezas_agregadas)  

                    detalle = {
                        'pieza_id': piezaRecuperada.getpiezaID(),
                        'cantidad': pieza_cantidad,
                        'folio': nuevo_folio,
                        'descripcion': descripcion  
                    }
                    self.detalles.append(detalle)  

                    self.VentanaEntry.insert(END, f"Folio: {nuevo_folio} - {descripcion} - Cantidad: {pieza_cantidad}")
                else:
                    self.VentanaEntry.insert(END, "No hay suficientes piezas en existencia para agregar la cantidad solicitada.")
            else:
                self.VentanaEntry.insert(END, "No se encontró la pieza.")

        except Exception as e:
            print(f"Error: {e}")

    def eliminarPieza(self):
        try:
            pieza_desc = self.piezas_var.get()  
            pieza_cantidad = self.cantidadEntry.get()  
            print(f"Descripción ingresada: {pieza_desc}, Cantidad a regresar: {pieza_cantidad}")

            if pieza_cantidad == '':  
                self.VentanaEntry.insert(END, "Por favor ingrese una cantidad válida.\n")
                return

            pieza_cantidad = int(pieza_cantidad)

            piezaRecuperada = self.dbcto.buscarPiezaPorDescripcion(pieza_desc)

            self.idEntry.delete(0, END)

            if piezaRecuperada:
                descripcion = piezaRecuperada.getDescripcion()
                existencias = piezaRecuperada.getExistencias() 

                piezas_agregadas = self.dbcto.obtenerPiezasAgregadas(pieza_desc)

                self.VentanaEntry.insert(END, f"Descripción: {descripcion}\n")
                self.VentanaEntry.insert(END, f"Existencias actuales: {existencias}\n")
                self.VentanaEntry.insert(END, f"Piezas agregadas: {piezas_agregadas}\n")

                if pieza_cantidad > piezas_agregadas:
                    self.VentanaEntry.insert(END, "No puedes regresar más piezas de las que has agregado.")
                else:
                    nueva_existencia = existencias + pieza_cantidad  
                    self.dbcto.actualizarExistenciasAGG(pieza_desc, nueva_existencia) 

                    self.VentanaEntry.insert(END, f"Cantidad regresada: {pieza_cantidad}\n")
                    self.VentanaEntry.insert(END, f"Nuevo total de existencias: {nueva_existencia}\n")
                    
                    folio = self.generar_folio()
                    self.dbcto.guardarFolioDevolucion(folio, pieza_desc, pieza_cantidad)
                    
                    self.dbcto.actualizarPiezasAgregadas(pieza_desc, piezas_agregadas - pieza_cantidad)
            else:
                self.VentanaEntry.insert(END, "No se encontró la pieza.")

        except Exception as e:
            print(f"Error: {e}")



    def guardarFolio(self):
        try:
            fecha_entrada_str = self.FechaEntradaEntry.get()
            fecha_salida_str = self.FechaSalidaEntry.get()
            matricula = self.matricula_var.get()

            if not matricula:
                messagebox.showerror("Error", "Debe seleccionar una matrícula.")
                return

            try:
                fecha_entrada = datetime.strptime(fecha_entrada_str, "%Y-%m-%d")  # Formato de fecha: YYYY-MM-DD
                fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d")  
            except ValueError:
                messagebox.showerror("Error", "Las fechas deben estar en formato: YYYY-MM-DD")
                return

            if fecha_entrada > fecha_salida:
                messagebox.showerror("Error", "La fecha de entrada no puede ser posterior a la fecha de salida.")
                return

            folio = self.dbcto.obtenerNuevoFolio() 
            matricula = self.matricula_var.get()  

            rep_id = self.dbcto.guardarReparacion(matricula, fecha_entrada_str, fecha_salida_str)  
            if not rep_id:
                messagebox.showerror("Error", "No se pudo obtener el rep_id para la reparación.")
                return

            for detalle in self.detalles: 
                pieza_id = detalle['pieza_id']
                cantidad = detalle['cantidad']
                folio_detalle = detalle['folio']  
                self.dbcto.guardarDetallesReparacion(folio_detalle, rep_id, pieza_id, cantidad)

            messagebox.showinfo("Reparación", "Reparación y detalles guardados correctamente.")

            self.idEntry.delete(0, END)
            self.cantidadEntry.delete(0, END)
            self.matricula_var.set('')
            self.FechaEntradaEntry.delete(0, END)
            self.FechaSalidaEntry.delete(0, END)

        except Exception as e:
            print(f"Error al guardar reparación y detalles: {e}")
            messagebox.showerror("Error", f"Hubo un problema al guardar la reparación: {e}")

            

    def generar_folio(self):
        """Genera un nuevo folio asegurándose de que no exista en la base de datos"""
        self.folio += 1 
        if self.dbcto.comprobarFolioExistente(self.folio):
            print(f"Folio {self.folio} ya existe, generando un nuevo folio.")
            self.folio += 1
        return self.folio  


    #---------------

    def editarReparacion(self):
        try:
            folio_reparacion = self.idEntry.get()  
            if not folio_reparacion:
                messagebox.showerror("Error", "Por favor, ingrese un folio de reparación.")
                return

            try:
                folio_reparacion = int(folio_reparacion)
            except ValueError:
                messagebox.showerror("Error", "El folio ingresado no es válido.")
                return
            
            detalles_reparacion = self.dbcto.obtenerDetallesReparacion(folio_reparacion)  
            if not detalles_reparacion:
                messagebox.showerror("Error", "No se encontraron detalles para esta reparación.")
                return
            
            self.VentanaEntry.delete(0, END)  
            for detalle in detalles_reparacion:
                descripcion_pieza = detalle['descripcion']
                cantidad = detalle['cantidad']
                self.VentanaEntry.insert(END, f"Pieza: {descripcion_pieza} - Cantidad: {cantidad}")

            nueva_pieza = self.piezas_var.get() 
            nueva_cantidad_str = self.cantidadEntry.get()  

            try:
                nueva_cantidad = int(nueva_cantidad_str) 
            except ValueError:
                messagebox.showerror("Error", "La cantidad ingresada no es válida.")
                return

            if nueva_pieza and nueva_cantidad:
                pieza_id = self.dbcto.buscar_id_por_descripcion(nueva_pieza)
                if not pieza_id:
                    messagebox.showerror("Error", "No se encontró la pieza seleccionada.")
                    return
                
                self.dbcto.eliminarDetalleReparacion(folio_reparacion, pieza_id) 

                self.dbcto.guardarDetallesReparacion(folio_reparacion, pieza_id, nueva_cantidad) 

                self.VentanaEntry.insert(END, f"Reparación {folio_reparacion} editada con éxito. Nueva pieza: {nueva_pieza}, Cantidad: {nueva_cantidad}")

            else:
                messagebox.showerror("Error", "Por favor, ingrese una pieza y cantidad válidas.")
        except Exception as e:
            print(f"Error al editar reparación: {e}")
            messagebox.showerror("Error", f"Hubo un problema al editar la reparación: {e}")

    def eliminarReparacion(self):
        try:
            folio_reparacion = self.idEntry.get()  
            if not folio_reparacion:
                messagebox.showerror("Error", "Por favor, ingrese un folio de reparación.")
                return

            try:
                folio_reparacion = int(folio_reparacion)
            except ValueError:
                messagebox.showerror("Error", "El folio ingresado no es válido.")
                return

            rep_id = self.dbcto.obtenerRepIDPorFolio(folio_reparacion)
            if not rep_id:
                messagebox.showerror("Error", "No se encontró un rep_id válido para el folio.")
                return

            detalles_reparacion = self.dbcto.obtenerDetallesReparacionPorRepID(rep_id)
            if not detalles_reparacion:
                messagebox.showerror("Error", "No se encontraron detalles para esta reparación.")
                return

            for detalle in detalles_reparacion:
                pieza_id = detalle['pieza_id']
                cantidad = detalle['cantidad']

                pieza = self.dbcto.buscarPiezaPorID(pieza_id)
                if pieza:
                    descripcion = pieza.getDescripcion()
                    existencias = pieza.getExistencias()

                    nuevas_existencias = existencias + cantidad
                    print(nuevas_existencias)
                    self.dbcto.actualizarExistenciasAGG(descripcion, nuevas_existencias)

                    self.VentanaEntry.insert(END, f"Pieza: {descripcion} - Cantidad devuelta: {cantidad}")
                else:
                    self.VentanaEntry.insert(END, f"No se encontró la pieza con ID: {pieza_id}")

            self.dbcto.eliminarDetallesReparacion(rep_id)

            self.dbcto.eliminarReparacion(folio_reparacion)

            self.VentanaEntry.insert(END, f"Reparación con folio {folio_reparacion} eliminada correctamente.\n")
            messagebox.showinfo("Éxito", f"La reparación {folio_reparacion} y sus detalles fueron eliminados exitosamente.")

        except Exception as e:
            print(f"Error al eliminar la reparación: {e}")
            messagebox.showerror("Error", f"Hubo un problema al eliminar la reparación: {e}")

    def editarFolio(self):
        try:
            ventana_editar = Toplevel(self)
            ventana_editar.title("Editar Folio")
            ventana_editar.geometry("400x400")

            Label(ventana_editar, text="ID de Reparación (Folio):").grid(row=0, column=0, pady=10, padx=10)
            self.id_folio_entry = Entry(ventana_editar)
            self.id_folio_entry.grid(row=0, column=1, pady=10, padx=10)

            Label(ventana_editar, text="Nueva Pieza:").grid(row=1, column=0, pady=10, padx=10)
            
            self.pieza_var = StringVar(ventana_editar)
            piezas = self.obtener_piezas()  
            self.pieza_var.set(piezas[0] if piezas else "No hay piezas disponibles")
            self.pieza_menu = OptionMenu(ventana_editar, self.pieza_var, *piezas)
            self.pieza_menu.grid(row=1, column=1, pady=10, padx=10)

            Label(ventana_editar, text="Nueva Cantidad:").grid(row=2, column=0, pady=10, padx=10)
            self.cantidad_entry = Entry(ventana_editar)
            self.cantidad_entry.grid(row=2, column=1, pady=10, padx=10)

            
            Button(ventana_editar, text="Actualizar", command=self.actualizar_folio).grid(row=3, column=0, columnspan=2, pady=10, padx=10)

            ventana_editar.mainloop()

        except Exception as e:
            print(f"Error al editar folio: {e}")
            messagebox.showerror("Error", f"Hubo un problema al abrir la ventana de edición del folio: {e}")

    def actualizar_folio(self):
        try:
            folio_id = int(self.id_folio_entry.get())  
            nueva_pieza = self.pieza_var.get() 
            nueva_cantidad = int(self.cantidad_entry.get())  

            detalle_reparacion = self.dbcto.obtenerDetallesReparacion(folio_id)
            if not detalle_reparacion:
                messagebox.showerror("Error", "No se encontraron detalles para este folio.")
                return
            
            pieza_id = self.dbcto.buscar_id_por_descripcion(nueva_pieza)  
            if not pieza_id:
                messagebox.showerror("Error", "La pieza seleccionada no existe.")
                return

            pieza_original = detalle_reparacion[0]
            pieza_id_original = pieza_original['pieza_id']
            cantidad_original = pieza_original['cantidad']
            
            if pieza_id_original != pieza_id: 
                self.dbcto.actualizarExistenciasEDIT(pieza_id_original, cantidad_original) 

                self.dbcto.actualizarExistenciasEDIT(pieza_id, -nueva_cantidad)  

            else: 
                diferencia = nueva_cantidad - cantidad_original

                if diferencia > 0:
                    self.dbcto.actualizarExistenciasEDIT(pieza_id, -diferencia) 
                elif diferencia < 0:
                    self.dbcto.actualizarExistenciasEDIT(pieza_id, -diferencia) 

            self.dbcto.editarDetalleReparacion(folio_id, pieza_id, nueva_cantidad)

            messagebox.showinfo("Éxito", f"Folio {folio_id} actualizado correctamente con nueva pieza: {nueva_pieza}, Nueva cantidad: {nueva_cantidad}")

            self.VentanaEntry.delete(0, END)
            self.VentanaEntry.insert(END, f"Pieza: {nueva_pieza} - Cantidad: {nueva_cantidad}")

        except Exception as e:
            print(f"Error al actualizar el folio: {e}")
            messagebox.showerror("Error", f"Hubo un problema al actualizar el folio: {e}")



if __name__ == "__main__":
    app = App()
    app.mainloop()
