class Automobile:
    def __init__(self, codice, marca, modello, anno, num_posti):
        self.cod = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.num_posti = num_posti


class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        macchine = []
        self.nome = nome
        self.responsabile = responsabile
        self.macchine = macchine


    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for riga in file:
                    campi = riga.strip().split(',')
                    self.macchine.append(campi)

            return self.macchine


        except FileNotFoundError:
            return "File non trovato"



    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
