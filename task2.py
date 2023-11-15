class Rectagle:

    def __init__(self, wight, height):
        self.height = height
        self.wight = wight

    def S(self):
        print ('Площадь прямоугольника:')
        print(self.wight * self.height)

    def P(self):
        print ('Периметр прямоугольника:', )
        print((self.wight + self.height) * 2)



rec1 = Rectagle(12, 8)
rec1.S()
rec1.P()

