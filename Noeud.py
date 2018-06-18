import Queue
import Car
import Table
import time

# Liste où sont stockées les tables de transpositions
mem = []
# Noeud de l'arbre de recherche
class Node(object):
    move_list = Queue.LifoQueue()
    sons = Queue.Queue() 
    end = False
    
    #Initialisation/Création du noeud
    def __init__(self, parent, table, signs, move, num):
        self.parent = parent
        self.table = table.copie()
        self.signs = self.table.signs()
        self.move = move
        self.num = num
        if self.move is not None:
            s = self.move.split()
            self.signs[s[0]].Move(s[1], int(s[2]))

    # Créer les fils du noeud actuel
    def create_sons(self):
        if self.signs['R'].x == self.table.size-2:                              # Si la voiture rouge est arrivée au bout, c'est gagné
            Node.end = True
            self.path()
        elif not self.end:
            for c in self.table.cars:                                           # Pour chaque voiture on regarde si aller en avant et en arrière sont des moves valides
                if self.table.isvalidmove(self.signs[c.sign], 'f', 1):
                    m_1 = c.sign + ' b 1'
                    if self.parent is None or m_1 != self.parent.move:          # On vérifie que le mouvement n'est pas l'inverse du mouvement parent
                        mich1 = Node(self, self.table, self.signs, c.sign + ' f 1',self.num+1)      # On créer le noeud fils
                        if mich1.table.gettable() not in mem:                   # on vérifie qu'on est pas déja tombé dessus, si non, on ajoute à la queue et à la liste mem
                            mem.append(mich1.table.gettable())
                            Node.sons.put(mich1)

                if self.table.isvalidmove(self.signs[c.sign], 'b', 1):          # Pareil mais pour le mouvement arrière (b = back)
                    m_1 = c.sign + ' f 1'

                    if self.parent is None or m_1 != self.parent.move:
                        mich2 = Node(self, self.table, self.signs, c.sign + ' b 1', self.num+1)
                        if mich2.table.gettable() not in mem:
                            mem.append(mich2.table.gettable())
                            Node.sons.put(mich2)
    
    # On créer la solution en récupérant les moves de tous les parents du noeud gagnant
    def path(self):
        Node.move_list.put(self.move)
        if self.parent is not None:
            self.parent.path()