class usuarios:
    def __init__(self):
        self.usuarioID = ""
        self.nombre = ""
        self.UserName = ""
        self.password = ""
        self.perfil = ""
        self.cliente = ""
        self.matricula = ""
        self.serie = ""
        self.marca = ""
        self.clienteID = ""
        self.color = ""

    def setID(self,usuarioID):
        self.usuarioID = usuarioID

    def getID(self):
        return self.usuarioID

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setUserName(self, UserName):
        self.UserName = UserName

    def getUserName(self):
        return self.UserName
    
    def setPassword(self,password):
        self.password = password

    def getPassword(self):
        return self.password
    
    def setPerfil(self, perfil):
        self.perfil = perfil

    def getPerfil(self):
        return self.perfil
    
    def setCliente(self,cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
         return self.matricula
    
    def setSerie(self,serie):
        self.serie = serie

    def getSerie(self):
        return self.serie
    
    def setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def setClienteID(self,clienteID):
        self.clienteID = clienteID
    
    def getClienteID(self):
        return self.clienteID
    
    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color


    
    
