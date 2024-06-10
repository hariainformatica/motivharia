class ProveedorDatos:
    def __init__(self):
        pass

#Pantalla Splash

    def obtenerMensajeSplash(self) ->str :
        pass

#Pantalla Principal

    def getFraseAsar(self) ->str:
        pass

#Pantalla de Acerca de

    def obtenerDatosAcercaDe(self) ->list:
        pass

#Pantalla de Autores - Tabla

    def getAutores(self) ->list:
        pass

#Pantalla de Autores - Insertar

    def insertarAutor(self, autor:str) ->str:
        pass

#Pantalla de Autores - Modificar

    def modificarAutor(self, autor:str, novo_autor:str) ->str:
        pass

#Pantalla de Autores - Eliminar

    def eliminarAutor(self, autor:str) ->str:
        pass

#Pantalla de Frases - Tabla

    def getFrases(self) ->list:
        pass

#Pantalla de Frases - Insertar

    def insertarFrase(self, frase:str, autor:str) ->str:
        pass

#Pantalla de Frases - Modificar

    def modificarFrase(self, frase:str, autor:str, nova_frase:str, novo_autor:str) ->str:
        pass

#Pantalla de Frases - Eliminar

    def eliminarFrase(self, frase:str, autor:str) ->str:
        pass