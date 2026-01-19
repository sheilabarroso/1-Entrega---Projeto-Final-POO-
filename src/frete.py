class Frete:
    def __init__(self, uf: str):
        self.uf = uf.upper()

    def calcular(self):
        if self.uf == "CE":
            return 20.0, 3
        elif self.uf == "SP":
            return 15.0, 5
        else:
            return 30.0, 10
