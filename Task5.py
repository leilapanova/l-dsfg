class Triangle:
    def __init__(self, site1, site2, site3):
        self.site1 = site1
        self.site2 = site2
        self.site3 = site3

    def get_type(self):
        if self.site1 == self.site2 and self.site1 != self.site3 or self.site1 == self.site3 and self.site1 != self.site2 or self.site2 == self.site3 and self.site2 != self.site1:
            print('Треугольник равнобедренный')
        elif self.site1 == self.site2 == self.site3:
            print('Треугольник равносторонний')
        else:
            print('Треугольник разностороннй')

    def s(self):
        height = ((((self.site1 / 2) ** 2) + (self.site2 ** 2)) ** 0.5)
        print(self.site1 * height * 0.5)


tr1 = Triangle(33, 23, 13)
tr1.get_type()
tr1.s()