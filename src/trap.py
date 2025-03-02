class Trap:
    def __init__(self, penalty=10, symbol="T"):
        self.penalty = penalty
        self.symbol = symbol

    def __str__(self):
        return self.symbol