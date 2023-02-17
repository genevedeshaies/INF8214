__author__ = "Alix Boc"

from personne import Personne

class Etudiant (Personne):

    __nbEtudiants = 0

    def __init__ (self, nom=None, prenom=None, nas=None):
        super().__init__(nom,prenom,nas)
        self.__codePermanent =  self.nom[:3].upper() + self.prenom[:1] + self.nas[:8]
        Etudiant.__nbEtudiants += 1

    def nbEtudiants():
        return str(Etudiant.__nbEtudiants)

    @property
    def codePermanent(self):
        return self.__codePermanent

    @property
    def nom2(self):
        return super().nom + "[Étudiant]"

    def __str__(self):
        return super().__str__() + " et un etudiant [" + self.__codePermanent + "]"
