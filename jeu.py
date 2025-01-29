from tkinter import *
from echiquier import Echiquier
from case import Case
from piece import *


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

        self.case_depart = None
        self.case_arrivee = None
        self.piece_amie = None
        self.piece_ennemie = None
        self.deplacements = []
        self.etat = "P"
        self.echec = False

        self.echiquier = Echiquier()
        self.dessiner_cases()
        self.dessiner_pieces()

        self.config(menu=self.menu)

    def selectionner(self, event):
        position_x = event.x // self.pixels_par_case
        position_y = event.y // self.pixels_par_case
        lettre, numero = self.traduction_coordonnees_vers_case(position_x, position_y)
        case_choisie = Case(lettre, numero)

        if case_choisie.estValide():
            if self.etat == "P":
                piece_choisie = self.echiquier.dictionnaire_cases[case_choisie]
                if piece_choisie is not None and piece_choisie.couleur == self.joueur:
                    self.choix_piece(case_choisie, piece_choisie)
                    self.etat = "D"

            if self.etat == "D":
                piece_choisie = self.echiquier.dictionnaire_cases[case_choisie]
                if piece_choisie is not None and piece_choisie.couleur == self.joueur:
                    self.actualiser_echiquier()
                    self.choix_piece(case_choisie, piece_choisie)

                elif case_choisie in self.deplacements or (type(self.piece_amie) is Pion and case_choisie in
                                                           self.piece_amie.attaquesPossibles()):
                    if type(self.piece_amie) is Pion:
                        if (case_choisie not in self.piece_amie.attaquesPossibles() or
                                (case_choisie in self.piece_amie.attaquesPossibles() and piece_choisie is not None)):
                            self.deplacement_piece(case_choisie, piece_choisie)
                            self.piece_amie.n_deplacement = 1

                    else:
                        self.deplacement_piece(case_choisie, piece_choisie)
        self.echiquier.detectionEchec(self.joueur)

    def choix_piece(self, case_choisie, piece_choisie):
        self.piece_amie = piece_choisie
        self.case_depart = case_choisie

        self.deplacements = self.echiquier.deplacementsPermis(self.piece_amie)
        if type(self.piece_amie) is Roi:
            print(self.deplacements)
            temp = []
            for depl in self.deplacements:
                print(depl)
                if not self.echiquier.roiMenace(depl, self.joueur):
                    temp.append(depl)
                    #print(temp)
                    #liste_cases.pop(liste_cases.index(case))
                    print("REMOVE")
                    print(depl)
            self.deplacements = temp

        for depl in self.deplacements:
            if (self.echiquier.dictionnaire_cases[depl] is not None and
                    self.echiquier.dictionnaire_cases[depl].couleur != self.joueur):
                if type(self.piece_amie) is not Pion:
                    self.colorier_case(depl, "red")
            elif self.echiquier.dictionnaire_cases[depl] is None:
                self.colorier_case(depl, "#8cf15d")
        if type(self.piece_amie) is Pion:
            for depl in self.piece_amie.attaquesPossibles():
                if (self.echiquier.dictionnaire_cases[depl] is not None and
                        self.echiquier.dictionnaire_cases[depl].couleur != self.joueur):
                    self.colorier_case(depl, "red")
        self.colorier_case(self.case_depart, "#cece4f")
        self.canvas.delete('piece')
        self.dessiner_pieces()

    def deplacement_piece(self, case_choisie, piece_choisie):
        self.case_arrivee = case_choisie
        self.echiquier.dictionnaire_cases[self.case_arrivee] = self.piece_amie
        self.echiquier.dictionnaire_cases[self.case_depart] = None
        self.echiquier.modifierCasePiece(self.piece_amie, self.case_arrivee)
        if piece_choisie is not None:
            self.piece_ennemie = piece_choisie
            self.echiquier.retirerPiece(self.piece_ennemie)
        self.actualiser_echiquier()
        self.changement_tour()
        self.etat = "P"

    def detection_echec(self, piece_choisie):
        if type(piece_choisie) is Roi:
            self.echec = True
        else:
            self.echec = False

    def souligner_case(self, case, couleur):
        ligne, colonne = self.traduction_case_vers_coordonnees(case)
        x0 = ligne * self.pixels_par_case
        y0 = colonne * self.pixels_par_case
        xf = x0 + self.pixels_par_case
        yf = y0 + self.pixels_par_case
        self.canvas.create_rectangle(x0, y0, xf, yf, outline=couleur, width=4,
                                     tags='case')

    def colorier_case(self, case, couleur):
        ligne, colonne = self.traduction_case_vers_coordonnees(case)
        x0 = ligne * self.pixels_par_case
        y0 = colonne * self.pixels_par_case
        xf = x0 + self.pixels_par_case
        yf = y0 + self.pixels_par_case
        self.canvas.create_rectangle(x0, y0, xf, yf, fill=couleur, width=1,
                                     tags='case')

    def changement_tour(self):
        if self.joueur == "white":
            self.joueur = "black"
            self.label_tour['text'] = f"Tour du joueur noir"
        else:
            self.joueur = "white"
            self.label_tour['text'] = f"Tour du joueur blanc"

    def supprimer_echiquier(self):
        self.canvas.delete('piece')
        self.canvas.delete('case')

    def actualiser_echiquier(self):
        self.canvas.delete('piece')
        self.canvas.delete('case')
        self.dessiner_cases()
        self.dessiner_pieces()

    def traduction_coordonnees_vers_case(self, position_x, position_y):
        numero = 9 - position_y
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
                y0 = (9 - j) * self.pixels_par_case
                xf = x0 + self.pixels_par_case
                yf = y0 + self.pixels_par_case
                if i == 0 or i == 9 or j == 0 or j == 9:
                    if (i == 0 or i == 9) and (j != 0 and j != 9):
                        self.canvas.create_text(x0 + self.pixels_par_case / 2, y0 + self.pixels_par_case / 2,
                                                text=f"{9 - numero}", fill="black", font="Calibri 20")
                    elif (j == 0 or j == 9) and (i != 0 and i != 9):
                        self.canvas.create_text(x0 + self.pixels_par_case / 2, y0 + self.pixels_par_case / 2,
                                                text=f"{lettre}", fill="black", font="Calibri 20")
                else:
                    case = Case(lettre, j)
                    self.canvas.create_rectangle(x0, y0, xf, yf, fill=case.couleur, tags='case')

    def dessiner_piece(self, piece):
        ligne, colonne = self.traduction_case_vers_coordonnees(piece.case)
        y = colonne * self.pixels_par_case + self.pixels_par_case / 2
        x = ligne * self.pixels_par_case + self.pixels_par_case / 2
        police = ('Arial', 20, 'bold')
        self.canvas.create_text(x, y, text=piece.icone, fill=piece.couleur, font=police, tags='piece')

    def dessiner_pieces(self):
        for piece in self.echiquier.dictionnaire_cases.values():
            if piece is not None:
                ligne, colonne = self.traduction_case_vers_coordonnees(piece.case)
                y = colonne * self.pixels_par_case + self.pixels_par_case / 2
                x = ligne * self.pixels_par_case + self.pixels_par_case / 2
                police = ('Arial', 20, 'bold')
                self.canvas.create_text(x, y, text=piece.icone, fill=piece.couleur, font=police, tags='piece')


