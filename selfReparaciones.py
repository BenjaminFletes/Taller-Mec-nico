class reparaciones():
    def __init__(self):
        self.folio = ""
        self.matricula = ""
        self.fechaInicio = ""
        self.fechaFinal = ""
        self.piezaID = ""
        self.descripcion = ""
        self.existencias = 0
        self.existencias_originales = 0 

    def setExistencias(self, existencias):
        """Establece tanto las existencias actuales como las originales."""
        self.existencias = existencias
        if self.existencias_originales == 0:
            self.existencias_originales = existencias  

    def getExistenciasOriginales(self):
        return self.existencias_originales  

    def getExistencias(self):
        return self.existencias

    def setFolio(self,folio):
        self.folio = folio

    def getFolio(self):
        return self.folio
    
    def setMatricula(self,matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula
    
    def setfechaInicio(self,fechaInicio):
        self.fechaInicio = fechaInicio

    def getfechaInicio(self):
        return self.fechaInicio
    
    def setfechaFinal(self,fechaFinal):
        self.fechaFinal = fechaFinal

    def getfechaFinal(self):
        return self.fechaFinal

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion
    
    def setExistencias(self,existencias):
        self.existencias = existencias

    def getExistencias(self):
        return self.existencias
    
    def setpiezaID(self,piezaID):
        self.piezaID = piezaID

    def getpiezaID(self):
        return self.piezaID