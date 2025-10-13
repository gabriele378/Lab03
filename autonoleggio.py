from automobile import Automobile
from noleggio import Noleggio
import operator

class Autonoleggio:
    def __init__(self, nome, responsabile, macchine):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.macchine = []
        self.noleggi = []



    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for riga in file:
                    campi = riga.strip().split(',')
                    codice = campi[0]
                    marca = campi[1]
                    modello = campi[2]
                    anno = int(campi[3])
                    posti = int(campi[4])
                    auto = Automobile(codice, marca, modello, anno, posti)
                    self.macchine.append(auto)
                return self.macchine


        except FileNotFoundError:
            return "File non trovato"



    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        nuovo_codice = f"A{ len(self.macchine)+1 }"
        nuova_macchina = Automobile(nuovo_codice, marca, modello, anno, num_posti)
        self.macchine.append(nuova_macchina)
        return nuova_macchina


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO
        lista_ordinata = sorted(self.macchine, key = operator.attrgetter('marca'))
        return lista_ordinata



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        for auto in self.macchine:
            if auto.codice == id_automobile:
                if auto.noleggiata:
                    raise Exception("Automobile già noleggiata")
                auto.noleggiata = True
                codice_noleggio = f"N{len(self.noleggi) + 1}"
                noleggio = Noleggio(codice_noleggio, data, auto, cognome_cliente)
                return noleggio

        raise Exception("Automobile non trovata")




    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO

        for n in self.noleggi:
            if n.codice == id_noleggio:
                n.auto.noleggiata = False
                self.noleggi.remove(n)
                return
        raise Exception("Noleggio non trovata")
