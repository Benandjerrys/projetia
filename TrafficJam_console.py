import os
from Table import Table
from Car import Car
import Noeud
from Noeud import Node
import time
import Queue
from math import *
import sys
from decimal import Decimal


debut = time.time()


def main():
    #puzzle = 'puzzles/' + raw_input('What puzzle do you want to solve? (Level: 1-8)') + '.txt'
    puzzle = 'puzzles/7.txt'
    mytable = reedpuzzle(puzzle)
    signs = mytable.signs()
    carstring = mytable.carsring()

    print "Tableau initial : "
    mytable.printtable()
    # Appel de l'IA
    ia(mytable, signs)
    sys.exit()

    # Boucle de jeu (inutile car l'ia est executee avant)
    while signs['R'].x != (mytable.size - 2):
        os.system('cls' if os.name == 'nt' else 'clear')
        mytable.printtable()
        print
        m = raw_input('What is your next move? (format: car(' + carstring + ') dir(f/b) steps) ').split()
        m = Node.move_list.get()
        if mytable.isvalidmove(signs[m[0]], m[1], int(m[2])):
            signs[m[0]].Move(m[1], int(m[2]))
        else:
            print
        print("Invalid move!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        mytable.printtable()
        print
        print "You win!"


def reedpuzzle(puzzle):
    cars = []
    with open(puzzle, "r") as puzzle:
        for sor in puzzle:
            c = sor.split()
            cars.append(Car(int(c[0]), int(c[1]), c[2], int(c[3]), c[4]))
    return Table(cars)

# fonction principale de l'IA
def ia(mytable, signs):
    # initailisation du noeud racine
    root = Node(None, mytable, signs, None, 0)
    Node.sons.put(root)
    Noeud.mem.append(root.table.gettable())

    cpt = 0
    n = 0
    # boucle d'exploration de l'arbre
    while not Node.end:
        # incrementatiion du nombre de noeuds explores
        cpt += 1
        # recuperation du noeud courant
        temp = Node.sons.get()
        # recuperation de la profondeur dans l'arbre
        if(temp.num != n):
            n = temp.num
        # creation des fils du noeud courant et ajout dans la queue
        temp.create_sons()
    print "\nNombre de noeuds parcourus : "+str(cpt)
    print "Nombre de mouvements de la solution : "+str(n)+"\n"
    Node.move_list.get()
    # affichage de la solution
    print "Solution : "
    while not Node.move_list.empty():
        print Node.move_list.get()

    print "\nEtat final : "
    temp.table.printtable()
    fin = time.time()
    temps = fin - debut
    print "\nTemps d'execution : "+str(round(temps,3))+" secondes"


if __name__ == "__main__":
    main()