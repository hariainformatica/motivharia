import csv

from motivharia.proveedorfrasesi import ProveedorFrasesI
from motivharia.listafrases import ListaFrases
from motivharia.frase import Frase

class ProveedorFrasesCSV(ProveedorFrasesI):

    def getFrases(self) -> ListaFrases:
        lista_frases = ListaFrases()
        with open('data/frases.csv', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                lista_frases.create(row[0], row[1])
        return lista_frases

    def close(self, lista):
        with open('data/frases.csv', 'w') as file:
            writer = csv.writer(file, delimiter='|')
            for frase in lista.read():
                writer.writerow([frase.frase, frase.autor])
        file.close()