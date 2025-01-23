from tkinter import *
from echiquier import Echiquier
from case import Case


class Jeu(Tk):
    def __init__(self):
        super().__init__()

        self.pixels_par_case = 60
        # self.geometry(f"{self.pixels_par_case * 10}x{self.pixels_par_case * 11}")
        self.title("Jeu d'échecs")

        self.canvas = Canvas(self, width=self.pixels_par_case * 10, height=self.pixels_par_case * 10)
        self.canvas.grid(sticky=NSEW)
        self.canvas.bind('<Button-1>', self.selectionner)

        self.joueur = "white"
        self.label_tour = Label(self, background='white', text=f"Tour du joueur blanc", font="Arial 10 bold")
        self.label_tour.grid(sticky=NSEW)

        self.menu = Menu(self)
        self.options_menu = Menu(self.menu, tearoff=0)
        self.options_menu.add_command(label="Nouvelle partie")
        self.options_menu.add_command(label="Enregistrer partie")
        self.options_menu.add_command(label="Charger partie")
        self.options_menu.add_command(label="Quitter")
        self.menu.add_cascade(label="Options", menu=self.options_menu)

        self.case_choisie = None
        self.etat = "choix_piece"

        self.echiquier = Echiquier()
        self.dessiner_cases()
        self.dessiner_pieces()

        self.config(menu=self.menu)

    def selectionner(self, event):
        self.actualiser_echiquier()
        self.etat = "choix piece"
        position_x = event.x // self.pixels_par_case
        position_y = event.y // self.pixels_par_case
        lettre, numero = self.traduction_coordonnees_vers_case(position_x, position_y)
        case_choisie = Case(lettre, numero)
        piece_choisie = None
        if case_choisie.estValide():
            for piece in self.echiquier.liste_pieces:
                if piece.case == case_choisie and piece.couleur == self.joueur:
                    self.case_choisie = case_choisie
                    self.souligner_case(self.case_choisie, "yellow")
                    piece_choisie = piece
                    self.etat = "choix déplacement"
                    break
            if self.etat == "choix déplacement":
                liste_cotes_bloques = self.echiquier.cotesBloquesPiece(piece_choisie)
                for case in piece_choisie.deplacementsPossibles():
                    if case not in self.echiquier.liste_cases_occupees:
                        self.souligner_case(case, "green")
                    elif self.echiquier.obtenirPiece(case).couleur != self.joueur:
                        self.souligner_case(case, "red")


    def souligner_case(self, case, couleur):
        ligne, colonne = self.traduction_case_vers_coordonnees(case)
        print(ligne)
        print(colonne)
        x0 = ligne * self.pixels_par_case
        y0 = colonne * self.pixels_par_case
        xf = x0 + self.pixels_par_case
        yf = y0 + self.pixels_par_case
        self.canvas.create_rectangle(x0, y0, xf, yf, outline=couleur, width=3,
                                     tags="case")
    def changement_tour(self):
        if self.joueur == "white":
            self.joueur = "black"
        else:
            self.joueur = "white"

    def actualiser_echiquier(self):
        self.canvas.delete("case")
        self.canvas.delete("piece")
        self.dessiner_cases()
        self.dessiner_pieces()
        if self.joueur == "white":
            self.label_tour['text'] = f"Tour du joueur blanc"
        else:
            self.label_tour['text'] = f"Tour du joueur noir"

    def traduction_coordonnees_vers_case(self, position_x, position_y):
        numero = 9-position_y
        lettre = ""
        match position_x:
            case 1:
                lettre = "a"
            case 2:
                lettre = "b"
            case 3:
                lettre = "c"
            case 4:
                lettre = "d"
            case 5:
                lettre = "e"
            case 6:
                lettre = "f"
            case 7:
                lettre = "g"
            case 8:
                lettre = "h"

        return lettre, numero

    def traduction_case_vers_coordonnees(self, case):
        ligne = 0
        colonne = 9 - case.numero
        match case.lettre:
            case "a":
                ligne = 1
            case "b":
                ligne = 2
            case "c":
                ligne = 3
            case "d":
                ligne = 4
            case "e":
                ligne = 5
            case "f":
                ligne = 6
            case "g":
                ligne = 7
            case "h":
                ligne = 8

        return ligne, colonne


    def dessiner_cases(self):
        for i in range(0, 10):
            for j in range(0, 10):
                lettre, numero = self.traduction_coordonnees_vers_case(i, j)
                x0 = i * self.pixels_par_case
                y0 = (9-j) * self.pixels_par_case
                xf = x0 + self.pixels_par_case
                yf = y0 + self.pixels_par_case
                if i == 0 or i == 9 or j == 0 or j == 9:
                    if (i == 0 or i == 9) and (j != 0 and j != 9):
                        self.canvas.create_text(x0+self.pixels_par_case/2, y0+self.pixels_par_case/2, text=f"{9-numero}", fill="black", font="Calibri 20")
                    elif (j == 0 or j == 9) and (i != 0 and i != 9):
                        self.canvas.create_text(x0+self.pixels_par_case/2, y0+self.pixels_par_case/2, text=f"{lettre}", fill="black", font="Calibri 20")
                else:
                    case = Case(lettre, j)
                    self.canvas.create_rectangle(x0, y0, xf, yf, fill=case.couleur, tags="case")



    def dessiner_pieces(self):
        for piece in self.echiquier.liste_pieces:
            ligne, colonne = self.traduction_case_vers_coordonnees(piece.case)
            y = colonne*self.pixels_par_case + self.pixels_par_case/2
            x = ligne*self.pixels_par_case + self.pixels_par_case/2
            police = ('Arial', 20, 'bold')
            self.canvas.create_text(x, y, text=piece.icone, fill=piece.couleur, font=police, tags="piece")
