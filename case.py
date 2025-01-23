from enum import Enum


class Etat(Enum):
    OCCUPEE = 1
    LIBRE = 0


class Case:

    def __init__(self, p_lettre, p_numero, p_etat=Etat.LIBRE):
        self.lettre = str(p_lettre)
        self.numero = int(p_numero)
        self.etat = p_etat
        if (self.numero % 2 == 0 and self.lettre in "aceg") or (self.numero % 2 != 0 and self.lettre in "bdfh"):
            self.couleur = "#e2cebc"
        else:
            self.couleur = "#a05e21"

    def caseDevientOccupee(self):
        self.etat = Etat.OCCUPEE

    def caseDevientLibre(self):
        self.etat = Etat.LIBRE

    def estOccupee(self):
        return self.etat == Etat.OCCUPEE

    def estValide(self):
        return self.lettre in "abcdefgh" and self.lettre != '' and self.numero in range(1, 9)

    def __eq__(self, p_case):
        return self.lettre == p_case.lettre and self.numero == p_case.numero

    def __repr__(self):
        return '({}, {})'.format(self.lettre, self.numero)

    def __hash__(self):
        return hash(str(self))
