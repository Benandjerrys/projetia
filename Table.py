from Car import Car

class Table(object):

    def __init__(self, cars, size=6):
        self.size = size
        self.cars = cars
        
# Créer une copie de la table
    def copie(self):
        taille = self.size
        voitures = []
        for car in self.cars:
            voitures.append(Car(car.x, car.y, car.lie, car.len, car.sign))
        return Table(voitures, taille)

    def carsring(self):
        return ','.join([c.sign for c in self.cars])

# Renvoie les lettres des voitures
    def signs(self):
        return dict([(c.sign, c) for c in self.cars])

    def GetCoordinates(self):
        d = {}
        for c in self.cars:
            d.update(c.GetCoordinatesDict())
        return d
        
# Print l'état du jeu d'un noeud
    def printtable(self):
        carcoordinates = self.GetCoordinates()
        for j in range(self.size):
            for i in range(self.size):
                if (i, j) in carcoordinates:
                    print(carcoordinates[(i, j)]),
                else:
                    print('+'),
            print

# Récupère l'état du jeu sous forme de string ("++++++AA+++C++D+++RR+++BBBB++++++")
# C'est en comparant les chaines qu'on sait si on est déjà passé sur un noeud ou non
    def gettable(self):
        carcoordinates = self.GetCoordinates()
        res = ''
        for j in range(self.size):
            for i in range(self.size):
                if (i, j) in carcoordinates:
                    res += carcoordinates[(i, j)]
                else:
                    res += '+'
        return res

# fonction qui check si c'est un déplacement valide
    def isvalidmove(self, c, direction, steps):
        carcoordinates = self.GetCoordinates()
        movingcoord = {'h': c.x, 'v': c.y}

        startpos = {'f': movingcoord[c.lie] + c.len, 'b': movingcoord[c.lie] - 1}
        endpos = {'f': movingcoord[c.lie] + c.len + steps, 'b': movingcoord[c.lie] - steps - 1}
        rangesteps = {'f': 1, 'b': -1}

        route = range(startpos[direction], endpos[direction], rangesteps[direction])
        if c.lie == 'h':
            freecoordinates = map(lambda i: (i, c.y) not in carcoordinates, route)
        elif c.lie == 'v':
            freecoordinates = map(lambda i: (c.x, i) not in carcoordinates, route)
        freecoordinates.append(True)
        return reduce(lambda a, b: a and b, freecoordinates) and endpos[direction] <= self.size and endpos[
            direction] + 1 >= 0