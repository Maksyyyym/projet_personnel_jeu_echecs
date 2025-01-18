from case import Case


class Piece:
    def __init__(self, p_couleur, p_case):
        self.couleur = p_couleur
        self.case = p_case
        self.icone = "O"


class Roi(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♕"
        if self.couleur == "black":
            self.icone = "♛"

    def __repr__(self):
        return self.icone


class Dame(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♔"
        if self.couleur == "black":
            self.icone = "♚"

    def __repr__(self):
        return self.icone


class Fou(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♗"
        if self.couleur == "black":
            self.icone = "♝"

    def __repr__(self):
        return self.icone


class Cavalier(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♘"
        if self.couleur == "black":
            self.icone = "♞"

    def __repr__(self):
        return self.icone


class Tour(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♖"
        if self.couleur == "black":
            self.icone = "♜"

    def __repr__(self):
        return self.icone


class Pion(Piece):
    def __init__(self, p_couleur, p_case):
        super().__init__(p_couleur, p_case)
        if self.couleur == "white":
            self.icone = "♙"
        if self.couleur == "black":
            self.icone = "♟"

    def __repr__(self):
        return self.icone
