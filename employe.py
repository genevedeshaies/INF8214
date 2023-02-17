__author__ = "Alix Boc"

from personne import Personne

class Employe (Personne):

    __nbEmployes = 0

    def __init__ (self, nom=None, prenom=None, nas=None):

        super().__init__(nom,prenom,nas)
        self.__codeEmploye =  self.nom[:3].upper() + "_" + self.prenom[:1]
        Employe.__nbEmployes += 1

    def nbEmployes():
        return str(Employe.__nbEmployes)

    @property
    def codeEmploye(self):
        return self.__codeEmploye

    def __str__(self):
        return super().__str__() + " et un employe [" + self.__codeEmploye + "]"
