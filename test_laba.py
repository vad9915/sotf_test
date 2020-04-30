class Formulas():
    def __init__(self, x):
        self.x = x

    def calculation(self):
        try:
            if self.x <= 1.186 or self.x >= 186.501:
                calculation_1 = self.x**4 * 1.871 + self.x**3 * 2.317 - self.x**2 * 4.367 + self.x * 3.851
                calculation_2 = self.x**3 * 5.661 - self.x**2 * 3.485 + self.x * 6.331
                calculation_3 = self.x**2 * 2.642 + self.x * 2.796
                calculation_4 = self.x*2.965
                return calculation_1, calculation_2, calculation_3, calculation_4
        except TypeError:
            return "Error"
if __name__ == '__main__':
    F = Formulas("Ж")
    print(F.calculation())