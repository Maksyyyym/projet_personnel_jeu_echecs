from case import Case
from piece import Piece, Roi, Dame, Fou, Cavalier, Tour, Pion


class Echiquier:
    def __init__(self):
        self.nombre_rangees = 8
        self.nombre_colonnes = 8
        self.liste_pieces = [Tour("black", Case("a", 8)),
                             Cavalier("black", Case("b", 8)),
                             Fou("black", Case("c", 8)),
                             Roi("black", Case("d", 8)),
                             Dame("black", Case("e", 8)),
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
                             Roi("white", Case("d", 1)),
                             Dame("white", Case("e", 1)),
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
    
    def afficher_echiquier(self):
        print(" abcdefgh \n")
        print(8)
        for piece in self.liste_pieces:
            while piece.case.numero == 8:
                print(piece)
            print("\n")
            while piece.case.numero == 7:
                print(piece)