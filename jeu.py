from tkinter import *
from echiquier import Echiquier
from case import Case


class Jeu(Tk):
    def __init__(self):
        super().__init__()

        self.pixels_par_case = 60
        self.geometry(f"{self.pixels_par_case * 10}x{self.pixels_par_case * 10}")
        self.title("Jeu d'échecs")
        self.canvas = Canvas(self, width=self.pixels_par_case * 10, height=self.pixels_par_case * 10)
        self.canvas.grid(sticky=NSEW)
        self.canvas.bind('<Button-1>', self.selectionner)
        self.echiquier = Echiquier()
        self.dessiner_cases()
        self.dessiner_pieces()

    def selectionner(self, event):
        return 0

    def dessiner_cases(self):
        for i in range(0, 10):
            for j in range(0, 10):

                lettre = ""
                match i:
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

                x0 = i * self.pixels_par_case
                y0 = j * self.pixels_par_case
                xf = x0 + self.pixels_par_case
                yf = y0 + self.pixels_par_case
                if i == 0 or i == 9 or j == 0 or j == 9:
                    if (i == 0 or i == 9) and (j != 0 and j != 9):
                        self.canvas.create_text(x0+self.pixels_par_case/2, y0+self.pixels_par_case/2, text=f"{9-j}", fill="black", font="Calibri 14")
                    elif (j == 0 or j == 9) and (i != 0 and i != 9):
                        self.canvas.create_text(x0+self.pixels_par_case/2, y0+self.pixels_par_case/2, text=f"{lettre}", fill="black", font="Calibri 14")
                else:
                    case = Case(lettre, j)
                    self.canvas.create_rectangle(x0, y0, xf, yf, fill=case.couleur)

    def dessiner_pieces(self):
        for piece in self.echiquier.liste_pieces:
            case = piece.case
            ligne = 0
            colonne = case.numero
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
            y = (9-colonne)*self.pixels_par_case + self.pixels_par_case/2
            x = ligne*self.pixels_par_case + self.pixels_par_case/2
            self.canvas.create_text(x, y, text=piece.icone, fill=piece.couleur, font="Calibri 20 bold")