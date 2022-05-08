class ViajeroFrecuente:
    __nviajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millacum = 0
    def __init__(self, numviaj:int, dni:str, nomb:str, apell:str, milla:int=0):
        self.__nviajero = numviaj
        self.__dni = dni
        self.__nombre = nomb
        self.__apellido = apell
        self.__millacum = milla
    
    def __str__(self):
        cadena = "Numero: {0}\nDNI: {1}\nNombre: {2}\nApellido: {3}\nmilla: {4}".format(self.getNumero(), self.getDNI(), self.getNombre(), self.getApellido(), self.getmilla())
        return cadena

    def cantidadTotalmilla(self):
        return self.__millacum
    
    def acumularmilla(self, milla:int):
        band = False
        if isinstance(milla, int):
            self.__millacum += milla
            band = True
        else:
            print("Las milla deben ser del tipo ENTERO")
        return band
    
    
    def canjearmilla(self, milla:int):
        if isinstance(milla, int):
            if milla <= self.__millacum:
                self.__millacum -= milla
                print("milla canjeadas")
            else:
                print("No puede canjear más milla de las que tiene")
        else:
            print(" Las milla deben ser del tipo ENTERO")

    
    def getNumero(self):
        return self.__nviajero
    
    def getmilla(self):
        return self.__millacum
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    

    def __gt__(self, otro):
        resultado = None
        if isinstance(otro, ViajeroFrecuente):
            resultado = self.getmilla() > otro.getmilla()
        elif isinstance(otro, int):
            resultado = self.getmilla() > otro
        else:
            print("No se puede comparar un viajero con un {0}".format(type(otro)))
        return resultado

    
    def __eq__(self, otro):
        resultado = None
        if isinstance(otro, ViajeroFrecuente):
            resultado = self.getmilla() == otro.getmilla()
        elif isinstance(otro, int):
            resultado = self.getmilla() == otro
        else:
            print("No se puede comparar un viajero con un {0}".format(type(otro)))
        return resultado
    

    def __add__(self, milla):
        unViajero = None
        if isinstance(milla, int):
            unViajero = ViajeroFrecuente(self.getNumero(), self.getDNI(), self.getNombre(), self.getApellido(), self.getmilla()+milla)
        else:
            print("No se puede sumar una instancia de la clase viajero con un {0}".format(type(milla)))
        return unViajero
    
    def __radd__(self, milla):
        return self + milla
    

    def __sub__(self, milla):
        unViajero = self
        if isinstance(milla, int) and milla <= self.getmilla():
            unViajero = ViajeroFrecuente(self.getNumero(), self.getDNI(), self.getNombre(), self.getApellido(), self.getmilla() - milla)
        else:
            print("No se pudo efectuar la resta")
        return unViajero
    
    def __rsub__(self, milla):
        return self - milla