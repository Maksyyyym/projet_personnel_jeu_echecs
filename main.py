from piece import *
from case import Case
from echiquier import Echiquier
from jeu import Jeu

echiquier = Echiquier()
piece = Pion("white", Case('a', 2))
print(echiquier.casesH(piece))
print(echiquier.deplacementsPermis(piece))

jeu = Jeu()
jeu.mainloop()
