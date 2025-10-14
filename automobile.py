class Automobile:
    def __init__(self, codice, marca, modello, anno, num_posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.num_posti = num_posti
        self.noleggiata = False

    def __str__(self):
        return f"{self.codice} {self.marca} {self.modello} {self.anno} {self.num_posti}"
