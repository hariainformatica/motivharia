import csv

from motivharia.model.proveedorfrasesi import ProveedorFrasesI
from motivharia.model.listafrases import ListaFrases
from motivharia.model.frase import Frase
from motivharia.model.autor import Autor

from motivharia.model.proveedorautores import ProveedorAutores

class ProveedorFrasesCSV(ProveedorFrasesI):
    def __init__(self, proveedorAutores):
        self.proveedorAutores = proveedorAutores

    def getFrases(self) -> ListaFrases:
        lista_frases = ListaFrases()
        with open('data/frases.csv', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                lista_frases.create(Frase(lista_frases.getNewId(), str(row[0]), self.proveedorAutores.getAutorPorId(int(row[1]))))
        return lista_frases

    def close(self, lista):
        with open('data/frases.csv', 'w') as file:
            writer = csv.writer(file, delimiter='|')
            for frase in lista.read():
                writer.writerow([frase.frase, self.proveedorAutores.getAutor(frase.autor.nombre).id])
        file.close()