from motivharia.autor import Autor
class Frase:
    def __init__(self, id:id, frase:str, autor:Autor):
        self.id = int(id)
        self.frase = frase
        self.autor = autor

    def read(self) -> str:
        return str(self.id) + "|" + self.frase + "|" + self.autor

    def __str__(self) -> str:
        return str(self.frase) + "|" + str(self.autor)
    
    def update(self, frase, autor):
        self.frase = frase
        self.autor = autor

    def delete(self):
        self.frase = None
        self.autor = None