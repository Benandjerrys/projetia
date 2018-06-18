# Code venant du programme que l'on a recuperer

class Car(object):

    def __init__(self, x, y, lie, length, sign):
        """
        Stores the position datas of the car.

        (x,y): gives the position of upper left side of the car, in Descartes coordinate system.
               positive direct: x:right y:down
        direction: gives ,whether the car lie horizontally or vertically
        """
        self.x = x
        self.y = y
        self.lie = lie
        self.len = length
        self.sign = sign

    def Move(self, direction, steps):
        operator = {'f': 1, 'b': -1}
        if self.lie == 'h':
            self.x += (operator[direction] * steps)
        elif self.lie == 'v':
            self.y += (operator[direction] * steps)

    def GetCoordinates(self):
        if self.lie == 'v':
            return [(self.x, self.y + i) for i in range(self.len)]
        elif self.lie == 'h':
            return [(self.x + i, self.y) for i in range(self.len)]

    def GetCoordinatesDict(self):
        return dict(map(lambda t: (t, self.sign), self.GetCoordinates()))
