from piece import *
from case import Case
from echiquier import Echiquier
from jeu import Jeu

echiquier = Echiquier()
piece = Pion("black", Case('b', 7))
print(echiquier.casesB(piece))
print(echiquier.deplacementsPermis(piece))

jeu = Jeu()
jeu.mainloop()
