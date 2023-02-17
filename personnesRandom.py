__author__ = "Alix Boc"

""" illustration de l'utilisation de Personne """

import random
from personne import Personne
from etudiant import Etudiant
from employe  import Employe



#== creation d'une Liste de Personnes
mesPersonnes = []
nbPersonnes = 10
for i in range (0,nbPersonnes):
    if random.randint(0,10) % 2 == 0:
        mesPersonnes.append(Etudiant())
    else:
        mesPersonnes.append(Employe())


for i in range (0,nbPersonnes):
    print ( mesPersonnes[i] )

print ( "Nombre de personnes =", Personne.nbPersonnes())
print ( "Nombre d'étudiants =", Etudiant.nbEtudiants())
print ( "Nombre d'employés =", Employe.nbEmployes())
