from motivharia.frase import Frase

class ListaFrases:
    def __init__(self):
        self.frases = []

    def create(self, frase, autor)->Frase:
        self.frases.append(Frase(frase, autor))

    def read(self)->list:
        return self.frases
    
    def __str__(self)->str:
        result = ""
        for frase in self.frases:
            result += str(frase) + "\n"
        return result
    
    def getFrase(self, frase, autor)->Frase:
        for f in self.frases:
            if f.frase == frase and f.autor == autor:
                return f
        return None
    
    def getFrasePorId(self, id:int)->Frase:
        for f in self.frases:
            if int(f.id) == int(id):
                return f
        return None

    def update(self, frase, autor, nova_frase, novo_autor):
        for f in self.frases:
            if f.frase == frase and f.autor == autor:
                f.update(nova_frase, novo_autor)
                return f
        return None

    def delete(self, frase, autor):
        for f in self.frases:
            if f.frase == frase and f.autor == autor:
                self.frases.remove(f)
                return f
        return None
    
    def getNewId(self) -> int:
        max_id = 0
        for f in self.frases:
            if f.id > max_id:
                max_id = f.id
        return max_id + 1