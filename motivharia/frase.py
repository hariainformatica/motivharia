class Frase:
    def __init__(self, frase, autor):
        self.frase = frase
        self.autor = autor

    def read(self):
        return self.frase + " - " + self.autor

    def update(self, frase, autor):
        self.frase = frase
        self.autor = autor

    def delete(self):
        self.frase = None
        self.autor = None