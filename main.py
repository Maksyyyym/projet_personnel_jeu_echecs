from piece import *
from case import Case
from echiquier import Echiquier
from jeu import Jeu

echiquier = Echiquier()
for piece in echiquier.liste_pieces:
    if type(piece) is Pion:
        print(piece.attaquesPossibles())

jeu = Jeu()
jeu.mainloop()
