from motivharia.frase import Frase

class ListaFrases:
    def __init__(self):
        self.frases = []

    def create(self, frase, autor):
        self.frases.append(Frase(frase, autor))

    def read(self):
        return [frase.read() for frase in self.frases]

    def update(self, frase, autor, nova_frase, novo_autor):
        for f in self.frases:
            if f.frase == frase and f.autor == autor:
                f.update(nova_frase, novo_autor)

    def delete(self, frase, autor):
        for f in self.frases:
            if f.frase == frase and f.autor == autor:
                self.frases.remove(f)
                break