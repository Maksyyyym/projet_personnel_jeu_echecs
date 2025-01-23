from case import Case

lettres = "  abcdefgh  "


class Piece:
    def __init__(self, p_couleur, p_case):
        self.couleur = p_couleur
        self.case = p_case
        self.case.caseDevientOccupee()
        self.icone = "O"

    def __repr__(self):
        return self.icone

    def deplacementsPossibles(self):
        return


    def informationsCase(self):
        liste_cases = []

        lettre = self.case.lettre
        position_lettre = lettres.index(lettre)

        numero = self.case.numero

        numero_haut = 0
        numero_bas = 0
        lettre_gauche = ''
        lettre_droite = ''

        numero_haut = numero + 1
        numero_bas = numero - 1
        lettre_gauche = lettres[position_lettre - 1]
        lettre_droite = lettres[position_lettre + 1]
        return lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases

    def casesHG(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre_gauche
        prochain_numero = numero_haut
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre - 1]
            prochain_numero = prochain_numero + 1
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases


    def casesH(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre
        prochain_numero = numero_haut
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            prochain_numero = prochain_numero + 1
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases


    def casesHD(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre_droite
        prochain_numero = numero_haut
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre + 1]
            prochain_numero = prochain_numero + 1
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases

    def casesD(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre_droite
        prochain_numero = numero
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre + 1]
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases

    def casesBD(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre_droite
        prochain_numero = numero_bas
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre + 1]
            prochain_numero = prochain_numero - 1
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases

    def casesB(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre
        prochain_numero = numero_bas
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            prochain_numero = prochain_numero - 1
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases

    def casesBG(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre_gauche
        prochain_numero = numero_bas
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre - 1]
            prochain_numero = prochain_numero - 1
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases

    def casesG(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = self.informationsCase()

        prochaine_lettre = lettre_gauche
        prochain_numero = numero
        case = Case(prochaine_lettre, prochain_numero)
        while case.estValide():
            liste_cases.append(case)
            ancienne_pos_lettre = lettres.index(prochaine_lettre)
            prochaine_lettre = lettres[ancienne_pos_lettre - 1]
            case = Case(prochaine_lettre, prochain_numero)
        return liste_cases


class Roi(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♕"
        if self.couleur == "black":
            self.icone = "♛"

    def deplacementsPossibles(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = super().informationsCase()

        caseHG = Case(lettre_gauche, numero_haut)
        if caseHG.estValide():
            liste_cases.append(caseHG)
        caseH = Case(lettre, numero_haut)
        if caseH.estValide():
            liste_cases.append(caseH)
        caseHD = Case(lettre_droite, numero_haut)
        if caseHD.estValide():
            liste_cases.append(caseHD)
        caseD = Case(lettre_droite, numero)
        if caseD.estValide():
            liste_cases.append(caseD)
        caseBD = Case(lettre_droite, numero_bas)
        if caseBD.estValide():
            liste_cases.append(caseBD)
        caseB = Case(lettre, numero_bas)
        if caseB.estValide():
            liste_cases.append(caseB)
        caseBG = Case(lettre_gauche, numero_bas)
        if caseBG.estValide():
            liste_cases.append(caseBG)
        caseG = Case(lettre_gauche, numero)
        if caseG.estValide():
            liste_cases.append(caseG)

        return liste_cases


class Dame(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♔"
        if self.couleur == "black":
            self.icone = "♚"

    def deplacementsPossibles(self):
        return (super().casesHG() + super().casesH() + super().casesHD() + super().casesD() + super().casesBD() +
                super().casesB() + super().casesBG() + super().casesG())


class Fou(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♗"
        if self.couleur == "black":
            self.icone = "♝"

    def deplacementsPossibles(self):
        return super().casesHG() + super().casesHD() + super().casesBD() + super().casesBG()


class Cavalier(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♘"
        if self.couleur == "black":
            self.icone = "♞"

    def deplacementsPossibles(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = super().informationsCase()

        prochaine_lettre = lettres[lettres.find(lettre_gauche) - 1]
        prochain_numero = numero_haut
        caseHGG = Case(prochaine_lettre, prochain_numero)
        if caseHGG.estValide():
            liste_cases.append(caseHGG)

        prochaine_lettre = lettre_gauche
        prochain_numero = numero_haut + 1
        caseHGH = Case(prochaine_lettre, prochain_numero)
        if caseHGH.estValide():
            liste_cases.append(caseHGH)

        prochaine_lettre = lettre_droite
        prochain_numero = numero_haut + 1
        caseHDH = Case(prochaine_lettre, prochain_numero)
        if caseHDH.estValide():
            liste_cases.append(caseHDH)

        prochaine_lettre = lettres[lettres.find(lettre_droite) + 1]
        prochain_numero = numero_haut
        caseHDD = Case(prochaine_lettre, prochain_numero)
        if caseHDD.estValide():
            liste_cases.append(caseHDD)

        prochaine_lettre = lettres[lettres.find(lettre_droite) + 1]
        prochain_numero = numero_bas
        caseBDD = Case(prochaine_lettre, prochain_numero)
        if caseBDD.estValide():
            liste_cases.append(caseBDD)

        prochaine_lettre = lettre_droite
        prochain_numero = numero_bas - 1
        caseBDB = Case(prochaine_lettre, prochain_numero)
        if caseBDB.estValide():
            liste_cases.append(caseBDB)

        prochaine_lettre = lettre_gauche
        prochain_numero = numero_bas - 1
        caseBGB = Case(prochaine_lettre, prochain_numero)
        if caseBGB.estValide():
            liste_cases.append(caseBGB)

        prochaine_lettre = lettres[lettres.find(lettre_gauche) - 1]
        prochain_numero = numero_bas
        caseBGG = Case(prochaine_lettre, prochain_numero)
        if caseBGG.estValide():
            liste_cases.append(caseBGG)

        return liste_cases


class Tour(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♖"
        if self.couleur == "black":
            self.icone = "♜"

    def deplacementsPossibles(self):
        return super().casesH() + super().casesD() + super().casesB() + super().casesG()


class Pion(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♙"
        if self.couleur == "black":
            self.icone = "♟"

    def deplacementsPossibles(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = super().informationsCase()

        if self.couleur == "white":
            caseH = Case(lettre, numero_haut)
            if caseH.estValide():
                liste_cases.append(caseH)
        if self.couleur == "black":
            caseB = Case(lettre, numero_bas)
            if caseB.estValide():
                liste_cases.append(caseB)

        return liste_cases

    def attaquesPossibles(self):
        lettre, numero, lettre_gauche, numero_haut, lettre_droite, numero_bas, liste_cases \
            = super().informationsCase()

        if self.couleur == "white":
            caseHG = Case(lettre_gauche, numero_haut)
            if caseHG.estValide():
                liste_cases.append(caseHG)
            caseHD = Case(lettre_droite, numero_haut)
            if caseHD.estValide():
                liste_cases.append(caseHD)
        if self.couleur == "black":
            caseBG = Case(lettre_gauche, numero_bas)
            if caseBG.estValide():
                liste_cases.append(caseBG)
            caseBD = Case(lettre_droite, numero_bas)
            if caseBD.estValide():
                liste_cases.append(caseBD)

        return liste_cases
