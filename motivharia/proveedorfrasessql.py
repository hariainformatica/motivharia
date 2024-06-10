import sqlite3

from motivharia.proveedorfrasesi import ProveedorFrasesI
from motivharia.listafrases import ListaFrases
from motivharia.frase import Frase

from motivharia.database import Database

class ProveedorFrasesSQL(ProveedorFrasesI):
    def __init__(self) -> None:
        self.db = Database()

    def getFrases(self) -> ListaFrases:
        lista_frases = ListaFrases()
        cursor = self.db.getAll('frase')
        for row in cursor:
            frase = Frase(row[0], row[1], row[2])
            lista_frases.create(frase)
        
        self.db.close()
        return lista_frases
    
    def createFrase(self, frase) -> Frase:
        self.db.insert('frase', '(?, ?, ?)', (int(frase.id), str(frase.frase), str(frase.autor)))
        
        return frase
    
    def updateFrase(self, frase:Frase, nova_frase:str, novo_autor:str) -> Frase:
        self.db.update('frase', 'frase=?', 'autor=?', (nova_frase, novo_autor, frase.frase, frase.autor))
        
        return frase
    
    def deleteFrase(self, frase:Frase) -> Frase:
        self.db.delete('frase', 'frase=?', (frase.frase,))
        
        return frase
    
    def close(self, lista) -> None:
        pass