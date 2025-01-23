from case import Case, Etat
from piece import Piece, Roi, Dame, Fou, Cavalier, Tour, Pion


class Echiquier:
    def __init__(self):
        self.nombre_rangees = 8
        self.nombre_colonnes = 8
        self.liste_pieces = [Tour("black", Case("a", 8)),
                             Cavalier("black", Case("b", 8)),
                             Fou("black", Case("c", 8)),
                             Roi("black", Case("e", 8)),
                             Dame("black", Case("d", 8)),
                             Fou("black", Case("f", 8)),
                             Cavalier("black", Case("g", 8)),
                             Tour("black", Case("h", 8)),
                             Pion("black", Case("a", 7)),
                             Pion("black", Case("b", 7)),
                             Pion("black", Case("c", 7)),
                             Pion("black", Case("d", 7)),
                             Pion("black", Case("e", 7)),
                             Pion("black", Case("f", 7)),
                             Pion("black", Case("g", 7)),
                             Pion("black", Case("h", 7)),
                             Tour("white", Case("a", 1)),
                             Cavalier("white", Case("b", 1)),
                             Fou("white", Case("c", 1)),
                             Roi("white", Case("e", 1)),
                             Dame("white", Case("d", 1)),
                             Fou("white", Case("f", 1)),
                             Cavalier("white", Case("g", 1)),
                             Tour("white", Case("h", 1)),
                             Pion("white", Case("a", 2)),
                             Pion("white", Case("b", 2)),
                             Pion("white", Case("c", 2)),
                             Pion("white", Case("d", 2)),
                             Pion("white", Case("e", 2)),
                             Pion("white", Case("f", 2)),
                             Pion("white", Case("g", 2)),
                             Pion("white", Case("h", 2))]
        self.liste_cases_occupees = [Case("a", 8, Etat.OCCUPEE),
                             Case("b", 8, Etat.OCCUPEE),
                             Case("c", 8, Etat.OCCUPEE),
                             Case("e", 8, Etat.OCCUPEE),
                             Case("d", 8, Etat.OCCUPEE),
                             Case("f", 8, Etat.OCCUPEE),
                             Case("g", 8, Etat.OCCUPEE),
                             Case("h", 8, Etat.OCCUPEE),
                             Case("a", 7, Etat.OCCUPEE),
                             Case("b", 7, Etat.OCCUPEE),
                             Case("c", 7, Etat.OCCUPEE),
                             Case("d", 7, Etat.OCCUPEE),
                             Case("e", 7, Etat.OCCUPEE),
                             Case("f", 7, Etat.OCCUPEE),
                             Case("g", 7, Etat.OCCUPEE),
                             Case("h", 7, Etat.OCCUPEE),
                             Case("a", 1, Etat.OCCUPEE),
                             Case("b", 1, Etat.OCCUPEE),
                             Case("c", 1, Etat.OCCUPEE),
                             Case("e", 1, Etat.OCCUPEE),
                             Case("d", 1, Etat.OCCUPEE),
                             Case("f", 1, Etat.OCCUPEE),
                             Case("g", 1, Etat.OCCUPEE),
                             Case("h", 1, Etat.OCCUPEE),
                             Case("a", 2, Etat.OCCUPEE),
                             Case("b", 2, Etat.OCCUPEE),
                             Case("c", 2, Etat.OCCUPEE),
                             Case("d", 2, Etat.OCCUPEE),
                             Case("e", 2, Etat.OCCUPEE),
                             Case("f", 2, Etat.OCCUPEE),
                             Case("g", 2, Etat.OCCUPEE),
                             Case("h", 2, Etat.OCCUPEE)]

    def obtenirPiece(self, case):
        for piece in self.liste_pieces:
            if piece.case == case:
                return piece
        else:
            return None

    def cotesBloquesPiece(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()
        caseHG = Case(lettre_gauche, numero_haut)
        caseH = Case(lettre, numero_haut)
        caseHD = Case(lettre_droite, numero_haut)
        caseD = Case(lettre_droite, numero)
        caseBD = Case(lettre_droite, numero_bas)
        caseB = Case(lettre, numero_bas)
        caseBG = Case(lettre_gauche, numero_bas)
        caseG = Case(lettre_gauche, numero)

        for case in self.liste_cases_occupees:
            if case == caseHG or case == caseH or case == caseHD or case == caseD or case == caseBD or case == caseB or case == caseBG or case == caseBG or case == caseG:
                liste_cases.append(case)

        return liste_cases
    def enlever_piece(self, piece):
        piece.case.caseDevientLibre()
        self.liste_pieces.remove(piece)

    def afficher_echiquier(self):
        print(" abcdefgh \n")
        print(8)
        for piece in self.liste_pieces:
            while piece.case.numero == 8:
                print(piece)
            print("\n")
            while piece.case.numero == 7:
                print(piece)