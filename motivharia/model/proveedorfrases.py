from motivharia.model.proveedorfrasessql import ProveedorFrasesSQL
from motivharia.model.proveedorfrasescsv import ProveedorFrasesCSV
from motivharia.model.listafrases import ListaFrases
from motivharia.model.frase import Frase

from motivharia.model.proveedorautores import ProveedorAutores

class ProveedorFrases:
    def __init__(self, tipo, autosave=False):
        self.proveedorAutores = ProveedorAutores(tipo, autosave)

        if tipo == 'sql':
            self.proveedor = ProveedorFrasesSQL(self.proveedorAutores)
        elif tipo == 'csv':
            self.proveedor = ProveedorFrasesCSV(self.proveedorAutores)

        self.tipo       = tipo
        self.autosave   = autosave
        self.frases     = self.proveedor.getFrases()

    def getFrases(self)->ListaFrases:
        return self.frases

    def getFrase(self, frase, autor)->Frase:
        return self.frases.getFrase(frase, autor)

    def getFrasePorId(self, id)->Frase:
        return self.frases.getFrasePorId(id)

    def createFrase(self, frase:str, aut:str)->Frase:
        resultado = None
        autor = self.proveedorAutores.getAutor(aut)
        if autor == None:
            autor = self.proveedorAutores.createAutor(aut)
            self.proveedorAutores.close()

        if (self.getFrase(frase, autor) == None):
            resultado = self.frases.create(Frase(self.frases.getNewId(), frase, autor))
        
            if self.tipo == 'sql':
                self.proveedor.createFrase(resultado)

        if self.autosave:
            self.proveedor.close(self.frases)
            self.frases = self.proveedor.getFrases()
        
        return resultado

    def updateFrase(self, frase, autor, nova_frase, novo_autor)->Frase:
        resultado = None
        if (self.getFrase(nova_frase, novo_autor) == None):
            resultado = self.frases.update(frase, autor, nova_frase, novo_autor)

            if self.tipo == 'sql':
                self.proveedor.updateFrase(frase, autor, nova_frase, novo_autor)
        
        if self.autosave:
            self.proveedor.close(self.frases)
            self.frases = self.proveedor.getFrases()
        
        return resultado

    def deleteFrase(self, frase, autor)->Frase:
        resultado = self.frases.delete(frase, autor)
        
        if self.autosave and resultado != None:
            self.proveedor.close(self.frases)
            self.frases = self.proveedor.getFrases()

            if self.tipo == 'sql':
                self.proveedor.deleteFrase(resultado)

    def close(self):
        self.proveedor.close(self.frases)