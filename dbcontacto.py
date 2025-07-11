import conexion as con
import contactop as cto
import Usuarios as us
import selfReparaciones as rep


class dbcontacto:
    def salvar(self,contacto):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO clientes(cliente_id,usuario_id,nombre,telefono,rfc) VALUES (%s,%s,%s,%s,%s)"
        self.datos = (contacto.getID(),
                      contacto.getUsuarioID(),
                      contacto.getNombre(),
                      contacto.getTelefono(),
                      contacto.getRFC())
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.con.close()

    def buscar(self,contacto):
        sal = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            ides = contacto.getID()
            sql = f"SELECT * FROM clientes WHERE cliente_id = {ides}"
            print(sql)
            self.cursor1.execute(sql)
            row = self.cursor1.fetchone()
            if row is not None:
                sal = cto.contacto()
                sal.setID(int(row[0]))
                sal.setUsuarioID(row[1])
                sal.setNombre(row[2])
                sal.setTelefono(row[3])
                sal.setRFC(row[4])
        except:
            pass
        return sal
    
    def editar(self,contacto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            ides = contacto.getID()
            nuevo_usuarioID = contacto.getUsuarioID()
            nuevo_nombre = contacto.getNombre()
            nuevo_telefono = contacto.getTelefono()
            nuevo_RFC = contacto.getRFC()
            sql = "UPDATE clientes SET usuario_id = %s, nombre = %s, telefono = %s, rfc = %s WHERE cliente_id = %s"
            valores = (nuevo_usuarioID,nuevo_nombre,nuevo_telefono,nuevo_RFC,ides)

            self.cursor1.execute(sql,valores)
            self.conn.commit()

        except:
            pass
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()
        
    def eliminar(self,contacto):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            ides = contacto.getID()
            
            sql = "DELETE FROM clientes WHERE cliente_id = %s"
            valores = (ides,)
            self.cursor1.execute(sql,valores)
            self.conn.commit()
        except:
            pass
    #------------------------------------------------------------------------------------
    def guardarUsuario(self,usuarios):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO usuarios(nombre,user_name,password,perfil) VALUES (%s,%s,%s,%s)"
        self.datos = (usuarios.getNombre(),
                      usuarios.getUserName(),
                      usuarios.getPassword(),
                      usuarios.getPerfil())
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.con.close()

    def editarUsuario(self,usuarios):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            ides = usuarios.getID()
            nuevo_nombre = usuarios.getNombre()
            nuevo_username = usuarios.getUserName()
            nuevo_password = usuarios.getPassword()
            nuevo_perfil = usuarios.getPerfil()
            sql = "UPDATE usuarios SET nombre = %s, user_name = %s, password = %s, perfil = %s WHERE usuario_id = %s"
            valores = (nuevo_nombre,nuevo_username,nuevo_password,nuevo_perfil,ides)

            self.cursor1.execute(sql,valores)
            self.conn.commit()

        except:
            pass
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def buscarUsuario(self,usuarios):
        sal = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            ides = usuarios.getNombre()
            sql = "SELECT * FROM usuarios WHERE nombre = %s"
            print(sql)
            self.cursor1.execute(sql,(ides,))
            row = self.cursor1.fetchone()
            if row is not None:
                sal = us.usuarios()
                sal.setID(int(row[0]))
                sal.setNombre(row[1])
                sal.setPassword(row[2])
                sal.setUserName(row[3])
                sal.setPerfil(row[4])
        except:
            pass
        return sal
    
    def eliminarUsuario(self,usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            ides = usuario.getID()
            
            sql = "DELETE FROM usuarios WHERE usuario_id = %s"
            valores = (ides,)
            self.cursor1.execute(sql,valores)
            self.conn.commit()
        except:
            pass


    def ingresar(self,usuarios):
        sal = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            names = usuarios.getNombre()
            contras = usuarios.getPassword()
            
            sql = "SELECT user_name, perfil, usuario_id FROM usuarios WHERE user_name = %s AND password = %s"
            print(sql)
            self.cursor1.execute(sql, (names,contras))
            row = self.cursor1.fetchone()
            if row is not None:
                sal = usuarios
                sal.setNombre(row[0])
                sal.setPerfil(row[1])
                sal.setID(row[2])
        except:
            pass
        return sal
    
    #----------------------------------------
    def buscarCliente(self):
        clientes = []  
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            
            sql = "SELECT nombre FROM clientes"  
            print(sql)
            
            self.cursor1.execute(sql)
            rows = self.cursor1.fetchall()  
            
            for row in rows:
                clientes.append(row[0]) 
            
        except Exception as e:
            print("Error:", e)
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()
        
        return clientes  
    
    def buscarClientePorID(self, cliente_id):
        cliente_nombre = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT nombre FROM clientes WHERE cliente_id = %s"
            self.cursor1.execute(sql, (cliente_id,))
            row = self.cursor1.fetchone()
            if row:
                cliente_nombre = row[0]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return cliente_nombre
    
    def buscarID(self, contacto_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT cliente_id FROM clientes WHERE cliente_id = %s"
            self.cursor1.execute(sql, (contacto_id,))
            row = self.cursor1.fetchone()
            if row: 
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al buscar ID: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def buscarID(self, contacto_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT cliente_id FROM clientes WHERE usuario_id = %s"
            self.cursor1.execute(sql, (contacto_id,))
            row = self.cursor1.fetchone()
            if row: 
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al buscar ID: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def buscarUSUARIOID(self, usuario_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT usuario_id FROM usuarios WHERE usuario_id = %s"
            self.cursor1.execute(sql, (usuario_id,))
            row = self.cursor1.fetchone()
            if row: 
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al buscar ID: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()



    
    def buscar_id_por_nombre(self, nombre_cliente):
        cliente_id = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT cliente_id FROM clientes WHERE nombre = %s"
            self.cursor1.execute(sql, (nombre_cliente,))
            row = self.cursor1.fetchone()
            if row:
                cliente_id = row[0]  
                print(f"Cliente ID: {cliente_id}")  
        except Exception as e:
            print("Error:", e)
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()
        return cliente_id
    
    


    #----------------------------------------

    def guardarCarro(self, carros):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO vehiculos(Matricula, Serie, Modelo, Marca, cliente_id) VALUES (%s, %s, %s, %s, %s)"
        
        # Check if cliente_id is empty
        print(f"Valores para insertar: {carros.getMatricula()}, {carros.getSerie()}, {carros.getModelo()}, {carros.getMarca()}, {carros.getClienteID()}")
        
        self.datos = (carros.getMatricula(),
                    carros.getSerie(),
                    carros.getModelo(),
                    carros.getMarca(),
                    carros.getClienteID()) 

        if not self.datos[4]:  
            print("Error: cliente_id esta vacio")
            return

        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.con.close()

    def editarCarro(self, carros):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            matricula = carros.getMatricula()
            serie = carros.getSerie()
            modelo = carros.getModelo()
            marca = carros.getMarca()
            cliente_id = carros.getClienteID()

            sql = "UPDATE vehiculos SET Serie = %s, Modelo = %s, Marca = %s, cliente_id = %s WHERE Matricula = %s"
            valores = (serie, modelo, marca, cliente_id, matricula)
            self.cursor1.execute(sql, valores)
            self.conn.commit()

        except Exception as e:
            print(f"Error al editar el vehículo: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def editarMatricula(self, carros, old_matricula):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            matricula = carros.getMatricula()
            
            sql = "UPDATE vehiculos SET Matricula = %s WHERE Matricula = %s"
            valores = (matricula, old_matricula)  

            self.cursor1.execute(sql, valores)
            self.conn.commit()

        except Exception as e:
            print(f"Error al editar el vehículo: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def buscarMatriculas(self, matricula):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT matricula FROM vehiculos WHERE matriculas = %s"
            self.cursor1.execute(sql, (matricula,))
            row = self.cursor1.fetchone()
            if row: 
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al buscar ID: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def eliminarMatricula(self, carros):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            matricula = carros.getMatricula()  
            if not matricula:
                print("Error: No se proporcionó una matrícula válida.")
                return

            sql = "DELETE FROM vehiculos WHERE Matricula = %s"
            valores = (matricula,) 
            self.cursor1.execute(sql, valores)
            self.conn.commit()

        except Exception as e:
            print(f"Error al eliminar el vehículo: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()


    def tieneReparacionEnCurso(self, matricula):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT COUNT(*) FROM reparaciones WHERE matricula = %s"
            self.cursor1.execute(sql, (matricula,))
            row = self.cursor1.fetchone()

            if row and row[0] > 0:
                return True  
            else:
                return False 
        except Exception as e:
            print(f"Error al verificar reparación en curso: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()


    def buscarMatricula(self, carros):
        sal = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            matricula = carros.getMatricula() 

            sql = "SELECT * FROM vehiculos WHERE Matricula = %s"  
            self.cursor1.execute(sql, (matricula,))  

            row = self.cursor1.fetchone()
            if row is not None:
                sal = us.usuarios() 
                sal.setMatricula(row[0])  
                sal.setSerie(row[1])
                sal.setModelo(row[2])
                sal.setMarca(row[3])
                sal.setClienteID(row[4])  

        except Exception as e:
            print(f"Error al buscar matrícula: {e}")
        return sal
    
    def guardarFolio(self,folio):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO reparaciones(folio,matricula,fecha_entrada,fecha_salida) VALUES (%s, %s, %s, %s)"
        
        print(f"Valores para insertar: {folio.getFolio()}, {folio.getMatricula()}, {folio.getfechaInicio()}, {folio.getfechaFinal()}")
        
        self.datos = (folio.getFolio(),
                    folio.getMatricula(),
                    folio.getfechaInicio(),
                    folio.getfechaFinal()) 

        if not self.datos[3]:  
            print("Error: cliente_id esta vacio")
            return

        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.con.close()


    #---------------------------------------------------------------------

    def guardarPieza(self,pieza):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO piezas(pieza_id,descripcion,existencias) VALUES (%s,%s,%s)"

        self.datos = (pieza.getpiezaID(),
                    pieza.getDescripcion(),
                    pieza.getExistencias()
                    ) 
        
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.con.close()

    def eliminarPieza(self,pieza):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            piezaID = pieza.getpiezaID()  
            if not piezaID:
                print("Error: No se proporcionó un ID valido.")
                return

            sql = "DELETE FROM piezas WHERE pieza_id = %s"
            valores = (piezaID,) 
            self.cursor1.execute(sql, valores)
            self.conn.commit()

        except Exception as e:
            print(f"Error al eliminar el vehículo: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def editarPieza(self, pieza, pieza_old):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            piezaID = pieza.getpiezaID()
            
            sql = "UPDATE piezas SET pieza_id = %s WHERE pieza_id = %s"
            valores = (piezaID, pieza_old)  

            self.cursor1.execute(sql, valores)
            self.conn.commit()

        except Exception as e:
            print(f"Error al editar el vehículo: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def buscarPieza(self):
        piezas = []  
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            
            sql = "SELECT descripcion FROM piezas" 
            print(sql)
            
            self.cursor1.execute(sql)
            rows = self.cursor1.fetchall() 
            
            for row in rows:
                piezas.append(row[0])  
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return piezas 

    def buscar_id_por_descripcion(self, pieza_desc):
        pieza_id = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT pieza_id FROM piezas WHERE descripcion = %s"
            self.cursor1.execute(sql, (pieza_desc,))
            row = self.cursor1.fetchone() 
            if row:
                pieza_id = row[0] 
                print(f"Pieza ID: {pieza_id}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return pieza_id  
    
    def actualizarExistencias(self, pieza_desc, nuevas_existencias):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "UPDATE piezas SET existencias = %s WHERE descripcion = %s"
            self.cursor1.execute(sql, (nuevas_existencias, pieza_desc))

            self.conn.commit()
            print(f"Existencias actualizadas a {nuevas_existencias} para la pieza {pieza_desc}")
        except Exception as e:
            print(f"Error al actualizar las existencias: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()


    def buscarPiezaPorDescripcion(self, pieza_desc):
        sal = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT * FROM piezas WHERE descripcion = %s" 
            self.cursor1.execute(sql, (pieza_desc,))
            row = self.cursor1.fetchone()
            if row:
                sal = rep.reparaciones()
                sal.setpiezaID(row[0])  
                sal.setDescripcion(row[1]) 
                sal.setExistencias(row[2])  
        except Exception as e:
            print(f"Error al buscar pieza por descripción: {e}")
        return sal
    
    def buscarPiezaPorID(self, piezaID):
        sal = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT * FROM piezas WHERE pieza_id = %s" 
            self.cursor1.execute(sql, (piezaID,))
            row = self.cursor1.fetchone()
            if row:
                sal = rep.reparaciones()
                sal.setpiezaID(row[0]) 
                sal.setDescripcion(row[1])  
                sal.setExistencias(row[2])  
        except Exception as e:
            print(f"Error al buscar pieza por descripción: {e}")
        return sal
    
    def guardarPiezasAgregadas(self, pieza_desc, cantidad_agregada):
        """Guardar la cantidad de piezas que han sido agregadas."""
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT piezas_agregadas FROM piezas WHERE descripcion = %s"
            self.cursor1.execute(sql, (pieza_desc,))
            row = self.cursor1.fetchone()

            if row:  
                piezas_agregadas = row[0]
                nueva_cantidad = piezas_agregadas + cantidad_agregada
                sql_update = "UPDATE piezas SET piezas_agregadas = %s WHERE descripcion = %s"
                self.cursor1.execute(sql_update, (nueva_cantidad, pieza_desc))
            else:  
                sql_insert = "INSERT INTO piezas (descripcion, piezas_agregadas) VALUES (%s, %s)"
                self.cursor1.execute(sql_insert, (pieza_desc, cantidad_agregada))

            self.conn.commit() 
        except Exception as e:
            print(f"Error al guardar piezas agregadas: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def obtenerPiezasAgregadas(self, pieza_desc):
        """Obtener la cantidad de piezas que han sido agregadas."""
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT piezas_agregadas FROM piezas WHERE descripcion = %s"
            self.cursor1.execute(sql, (pieza_desc,))
            row = self.cursor1.fetchone()
            if row:
                return row[0]
            else:
                return 0  
        except Exception as e:
            print(f"Error al obtener piezas agregadas: {e}")
            return 0
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def actualizarPiezasAgregadas(self, pieza_desc, nuevas_piezas_agregadas):
        """Actualizar la cantidad de piezas agregadas para una pieza específica."""
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            # Actualizar las piezas agregadas en la base de datos
            sql = "UPDATE piezas SET piezas_agregadas = %s WHERE descripcion = %s"
            self.cursor1.execute(sql, (nuevas_piezas_agregadas, pieza_desc))

            self.conn.commit()  # Confirmar cambios
            print(f"Piezas agregadas actualizadas a {nuevas_piezas_agregadas} para la pieza {pieza_desc}")
        except Exception as e:
            print(f"Error al actualizar las piezas agregadas: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def editarReparacion(self, reparacion_id, matricula, fecha_entrada, fecha_salida):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "UPDATE reparaciones SET matricula = %s, fecha_entrada = %s, fecha_salida = %s WHERE reparaciones_id = %s"
            valores = (matricula, fecha_entrada, fecha_salida, reparacion_id)

            self.cursor1.execute(sql, valores)
            self.conn.commit()

            print(f"Reparación {reparacion_id} actualizada correctamente.")

        except Exception as e:
            print(f"Error al editar reparación: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def editarDetalleReparacion(self, folio_id, pieza_id, nueva_cantidad):
        try:
            # Conectarse a la base de datos
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            # Actualizar el detalle de la reparación
            sql = "UPDATE detallereparacion SET pieza_id = %s, cantidad = %s WHERE folio = %s"
            valores = (pieza_id, nueva_cantidad, folio_id)
            
            self.cursor1.execute(sql, valores)  # Ejecutar la consulta
            self.conn.commit()  # Confirmar los cambios

            print(f"Detalles de reparación con folio {folio_id} actualizados.")
        except Exception as e:
            print(f"Error al actualizar los detalles de la reparación: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()


    






    def obtenerRepIDPorFolio(self, folio):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT reparaciones_id FROM reparaciones WHERE reparaciones_id = %s"
            self.cursor1.execute(sql, (folio,))  
            row = self.cursor1.fetchone()

            if row:
                return row[0] 
            else:
                print("No se encontró un rep_id válido.")
                return None
        except Exception as e:
            print(f"Error al obtener rep_id: {e}")
            return None
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def obtenerNuevoFolio(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT MAX(folio) + 1 FROM detallereparacion" 
            self.cursor1.execute(sql)
            row = self.cursor1.fetchone()
            return row[0] if row else 1 

        except Exception as e:
            print(f"Error al obtener el nuevo folio: {e}")
            return 1  # Retornar 1 si ocurre un error
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def guardarDetallesReparacion(self, folio, rep_id, pieza_id, cantidad):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "INSERT INTO detallereparacion (folio, rep_id, pieza_id, cantidad) VALUES (%s, %s, %s, %s)"
            self.cursor1.execute(sql, (folio, rep_id, pieza_id, cantidad))
            self.conn.commit()
            print(f"Detalles de la reparación guardados correctamente para el folio {folio}")

        except Exception as e:
            print(f"Error al guardar detalle de reparación: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def obtenerUltimoFolio(self):
        """Obtiene el último folio utilizado en la base de datos."""
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            
            sql = "SELECT MAX(folio) FROM detallereparacion"
            self.cursor1.execute(sql)
            row = self.cursor1.fetchone()

            if row and row[0]:
                return row[0] 
            else:
                return 0 

        except Exception as e:
            print(f"Error al obtener el último folio: {e}")
            return 0 
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def guardarReparacion(self, matricula, fecha_entrada, fecha_salida):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "INSERT INTO reparaciones (matricula, fecha_entrada, fecha_salida) VALUES (%s, %s, %s)"
            self.cursor1.execute(sql, (matricula, fecha_entrada, fecha_salida))
            self.conn.commit()
            return self.cursor1.lastrowid  

        except Exception as e:
            print(f"Error al guardar reparación: {e}")
            return None
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def comprobarFolioExistente(self, folio):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT COUNT(*) FROM detallereparacion WHERE folio = %s"
            self.cursor1.execute(sql, (folio,))
            row = self.cursor1.fetchone()

            if row and row[0] > 0:
                return True  # El folio ya existe
            else:
                return False  # El folio no existe
        except Exception as e:
            print(f"Error al comprobar folio: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def actualizarDetallesReparacion(self, folio, pieza_id, nueva_pieza_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = """
            UPDATE detallereparacion
            SET pieza_id = %s
            WHERE folio = %s AND pieza_id = %s
            """
            self.cursor1.execute(sql, (nueva_pieza_id, folio, pieza_id)) 

            self.conn.commit()
            print(f"Detalles de la reparación con folio {folio} y pieza {pieza_id} actualizados correctamente.")
        
        except Exception as e:
            print(f"Error al actualizar los detalles de la reparación: {e}")
            self.conn.rollback()  # En caso de error, revertimos la transacción.
        
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()



    def actualizarDescripcionPieza(self, pieza_desc, nueva_descripcion):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "UPDATE piezas SET descripcion = %s WHERE descripcion = %s"
            self.cursor1.execute(sql, (nueva_descripcion, pieza_desc))

            self.conn.commit()  
            print(f"Descripción de la pieza actualizada a {nueva_descripcion} para la pieza {pieza_desc}")
        except Exception as e:
            print(f"Error al actualizar la descripción de la pieza: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def guardarFolioDevolucion(self, folio, pieza_desc, cantidad):
        try:
            
            query = """
            INSERT INTO devoluciones (folio, pieza_desc, cantidad)
            VALUES (%s, %s, %s)
            """
            params = (folio, pieza_desc, cantidad)
            self.cursor1.execute(query, params)
            self.conn.commit()
            print(f"Folio de devolución {folio} guardado correctamente.")
        except Exception as e:
            print(f"Error al guardar el folio de devolución: {e}")
            self.conn.rollback()



    def obtenerDetallesReparacion(self, folio):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            query = """
            SELECT dr.pieza_id, dr.cantidad, p.descripcion
            FROM detallereparacion dr
            JOIN piezas p ON dr.pieza_id = p.pieza_id
            WHERE dr.folio = %s
            """
            self.cursor1.execute(query, (folio,))
            detalles = self.cursor1.fetchall()

            if not detalles:
                return []

            detalles_reparacion = []
            for detalle in detalles:
                pieza_id, cantidad, descripcion = detalle
                detalles_reparacion.append({
                    'pieza_id': pieza_id,
                    'cantidad': cantidad,
                    'descripcion': descripcion
                })

            return detalles_reparacion

        except Exception as e:
            print(f"Error al obtener detalles de la reparación: {e}")
            return []
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def eliminarDetalleReparacion(self, folio, pieza_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "DELETE FROM detallereparacion WHERE folio = %s AND pieza_id = %s"
            self.cursor1.execute(sql, (folio, pieza_id)) 
            self.conn.commit()

            print(f"Detalle de reparación con folio {folio} y pieza_id {pieza_id} eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar detalle de reparación: {e}")
            self.conn.rollback()  
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()



    
    def guardarDetallesReparacion(self, folio, rep_id, pieza_id, cantidad):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "INSERT INTO detallereparacion (folio, rep_id, pieza_id, cantidad) VALUES (%s, %s, %s, %s)"
            self.cursor1.execute(sql, (folio, rep_id, pieza_id, cantidad))
            self.conn.commit()
            print(f"Detalle de reparación guardado con rep_id: {rep_id}")
        except Exception as e:
            print(f"Error al guardar detalle de reparación: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def obtenerDetallesReparacionPorRepID(self, rep_id):
        detalles = []  
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT pieza_id, cantidad FROM detallereparacion WHERE rep_id = %s"
            self.cursor1.execute(sql, (rep_id,))  
            rows = self.cursor1.fetchall() 

            for row in rows:
                detalle = {
                    'pieza_id': row[0],
                    'cantidad': row[1]
                }
                detalles.append(detalle)  
        except Exception as e:
            print(f"Error al obtener los detalles de la reparación: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return detalles  

    def eliminarDetallesReparacion(self, rep_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "DELETE FROM detallereparacion WHERE rep_id = %s"
            self.cursor1.execute(sql, (rep_id,)) 

            self.conn.commit()  
            print(f"Detalles de la reparación con rep_id {rep_id} eliminados correctamente.")

        except Exception as e:
            print(f"Error al eliminar los detalles de la reparación: {e}")
            self.conn.rollback() 

        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def buscarReparacionPorID(self, rep_id):
        reparacion = None
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT matricula, fecha_entrada, fecha_salida FROM reparaciones WHERE reparaciones_id = %s"
            self.cursor1.execute(sql, (rep_id,))  

            row = self.cursor1.fetchone()  
            if row:
                reparacion = {
                    'matricula': row[0],
                    'fecha_entrada': row[1],
                    'fecha_salida': row[2]
                }

        except Exception as e:
            print(f"Error al buscar la reparación: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return reparacion  

    def obtenerFoliosPorRepID(self, rep_id):
        folios = []  
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "SELECT folio FROM detallereparacion WHERE rep_id = %s"
            self.cursor1.execute(sql, (rep_id,)) 
            rows = self.cursor1.fetchall() 

            for row in rows:
                folios.append(row[0]) 

        except Exception as e:
            print(f"Error al obtener los folios relacionados: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return folios  
    
    def buscarREPID(self, folio_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            
            sql = "SELECT reparaciones_id FROM reparaciones WHERE reparaciones_id = %s"
            self.cursor1.execute(sql, (folio_id,))
            row = self.cursor1.fetchone()
            
            if row: 
                return row[0]
            else:
                return None  
        except Exception as e:
            print(f"Error al buscar REPID: {e}")
            return None
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()



    def buscarMatriculaID(self, contacto_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            sql = "SELECT Matricula FROM vehiculos WHERE Matricula = %s"
            self.cursor1.execute(sql, (contacto_id,))
            row = self.cursor1.fetchone()
            if row: 
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al buscar ID: {e}")
            return False
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()


    def eliminarReparacion(self, rep_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql = "DELETE FROM reparaciones WHERE reparaciones_id = %s"
            self.cursor1.execute(sql, (rep_id,))  

            self.conn.commit() 
            print(f"Reparación con rep_id {rep_id} eliminada correctamente.")

        except Exception as e:
            print(f"Error al eliminar la reparación: {e}")
            self.conn.rollback()  

        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()



    def actualizarExistenciasEDIT(self, pieza_id, diferencia):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            sql_select = "SELECT existencias FROM piezas WHERE pieza_id = %s"
            self.cursor1.execute(sql_select, (pieza_id,))
            row = self.cursor1.fetchone()

            if row:
                existencias_actuales = row[0]
                nueva_existencia = existencias_actuales + diferencia  

                sql_update = "UPDATE piezas SET existencias = %s WHERE pieza_id = %s"
                self.cursor1.execute(sql_update, (nueva_existencia, pieza_id))
                self.conn.commit()  
                print(f"Existencias actualizadas a {nueva_existencia} para la pieza {pieza_id}")
            else:
                print(f"No se encontró la pieza con ID {pieza_id}")
        except Exception as e:
            print(f"Error al actualizar las existencias: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

    def actualizarExistenciasAGG(self, pieza_desc, nuevas_existencias):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()

            print(f"Actualizando existencias para la pieza: {pieza_desc}, nuevas existencias: {nuevas_existencias}")
            
            sql_verificar = "SELECT * FROM piezas WHERE descripcion = %s"
            self.cursor1.execute(sql_verificar, (pieza_desc,))
            row = self.cursor1.fetchone()

            if row:  
                sql_actualizar = "UPDATE piezas SET existencias = %s WHERE descripcion = %s"
                self.cursor1.execute(sql_actualizar, (nuevas_existencias, pieza_desc))
                self.conn.commit()
                print(f"Existencias actualizadas a {nuevas_existencias} para la pieza {pieza_desc}")
            else:
                print(f"Error: No se encontró la pieza con la descripción '{pieza_desc}' en la base de datos.")
                
        except Exception as e:
            print(f"Error al actualizar las existencias: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

                    
    







    # - -- - -- - -- - - -- -- - -- -                --------------

    def buscarMatriculas(self):
        matriculas = []  
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            
            sql = "SELECT Matricula FROM vehiculos"  
            print(sql)
            
            self.cursor1.execute(sql)
            rows = self.cursor1.fetchall()  
            
            for row in rows:
                matriculas.append(row[0]) 
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.cursor1:
                self.cursor1.close()
            if self.conn:
                self.conn.close()

        return matriculas 