class Case:
    def __init__(self, p_lettre, p_numero):
        self.lettre = str(p_lettre)
        self.numero = int(p_numero)
        if (self.numero % 2 == 0 and self.lettre in "aceg") or (self.numero % 2 != 0 and self.lettre in "bdfh"):
            self.couleur = "#e2cebc"
        else:
            self.couleur = "#a05e21"

    def __eq__(self, p_case):
        return self.lettre == p_case.lettre and self.numero == p_case.lettre

    def __repr__(self):
        return '({}, {})'.format(self.lettre, self.numero)

    def __hash__(self):
        return hash(str(self))