from case import Case, Etat
from piece import Piece, Roi, Dame, Fou, Cavalier, Tour, Pion

lettres = "  abcdefgh  "


class Echiquier:
    def __init__(self):
        self.nombre_rangees = 8
        self.nombre_colonnes = 8
        self.dictionnaire_cases = {}
        for numero in range(1, 9):
            for lettre in "abcdefgh":
                self.dictionnaire_cases[Case(lettre, numero)] = None
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
        for piece in self.liste_pieces:
            self.dictionnaire_cases[piece.case] = piece

    def modifierCasePiece(self, piece, case):
        for p in self.liste_pieces:
            if p == piece:
                piece.case = case
                break

    def retirerPiece(self, piece):
        for p in self.liste_pieces:
            if p == piece:
                self.liste_pieces.remove(p)
                break

    def casesHG(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre_gauche
        prochain_numero = numero_haut
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre - 1]
            prochain_numero = prochain_numero + 1
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesH(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre
        prochain_numero = numero_haut
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            prochain_numero = prochain_numero + 1
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesHD(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre_droite
        prochain_numero = numero_haut
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre + 1]
            prochain_numero = prochain_numero + 1
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesD(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre_droite
        prochain_numero = numero
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre + 1]
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesBD(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre_droite
        prochain_numero = numero_bas
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre + 1]
            prochain_numero = prochain_numero - 1
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesB(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre
        prochain_numero = numero_bas
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            prochain_numero = prochain_numero - 1
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesBG(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre_gauche
        prochain_numero = numero_bas
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre - 1]
            prochain_numero = prochain_numero - 1
            case = Case(prochaine_lettre, prochain_numero)

        return liste_cases

    def casesG(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()

        prochaine_lettre = lettre_gauche
        prochain_numero = numero
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            if self.dictionnaire_cases[case] is not None:
                break
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre - 1]
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases

    def obtenirPiece(self, case):
        for piece in self.liste_pieces:
            if piece.case == case:
                return piece
        else:
            return None

    def deplacementsPermis(self, piece):
        if type(piece) is Cavalier:
            return piece.deplacementsPossibles()
        else:
            liste_cases = piece.deplacementsPossibles()
            for case in piece.deplacementsPossibles():
                if (case not in self.casesHG(piece) and case not in self.casesH(piece) and case not in self.casesHD(piece)
                        and case not in self.casesD(piece) and case not in self.casesBD(piece)
                        and case not in self.casesB(piece) and case not in self.casesBG(piece)
                        and case not in self.casesG(piece)):
                    liste_cases.pop(liste_cases.index(case))
            return liste_cases

    def casesBloqueesPiece(self, piece):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = piece.informationsCase()
        liste_lettres = [lettre_gauche, lettre, lettre_droite]
        liste_numeros = [numero_haut, numero, numero_bas]

        caseHG = Case(lettre_gauche, numero_haut)
        caseH = Case(lettre, numero_haut)
        caseHD = Case(lettre_droite, numero_haut)
        caseD = Case(lettre_droite, numero)
        caseBD = Case(lettre_droite, numero_bas)
        caseB = Case(lettre, numero_bas)
        caseBG = Case(lettre_gauche, numero_bas)
        caseG = Case(lettre_gauche, numero)

        for l in liste_lettres:
            for n in liste_numeros:
                case = Case(l, n)
                if case.estValide():
                    p = self.dictionnaire_cases[case]
                    if case != piece.case and p is not None:
                        liste_cases.append(case)
                        if case == caseHG:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesHG()
                        if case == caseH:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesH()
                        if case == caseHD:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesHD()
                        if case == caseD:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesD()
                        if case == caseBD:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesBD()
                        if case == caseB:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesB()
                        if case == caseBG:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesBG()
                        if case == caseG:
                            liste_cases = liste_cases + self.dictionnaire_cases[case].casesG()

        return liste_cases

    def enleverPiece(self, piece):
        piece.case.caseDevientLibre()
        self.liste_pieces.remove(piece)

    def afficherEchiquier(self):
        print(" abcdefgh \n")
        print(8)
        for piece in self.liste_pieces:
            while piece.case.numero == 8:
                print(piece)
            print("\n")
            while piece.case.numero == 7:
                print(piece)

    def detectionEchec(self, couleur):
        caseR = None
        for case in self.dictionnaire_cases:
            if self.dictionnaire_cases[case] is not None and type(self.dictionnaire_cases[case]) is Roi:
                if self.dictionnaire_cases[case].couleur == couleur:
                    caseR = case
        return self.roiMenace(caseR, couleur)

    def roiMenace(self, caseR, couleur):
        print(caseR)
        for piece in self.dictionnaire_cases.values():
            if piece is not None and piece.couleur != couleur:
                if type(piece) is Pion and caseR in piece.attaquesPossibles():
                    # print("ÉCHEC")
                    return True
                elif caseR in self.deplacementsPermis(piece):
                    # print("ÉCHEC")
                    return True
        return False
