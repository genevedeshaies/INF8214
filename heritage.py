from personne import Personne

class Employe (Personne): #classe qu'on crée (classe dont on hérite des propriétés)

    def __init__(self, nom=None, prenom=None, nas=None):

        super().__init__(nom, prenom, nas) #fonction qui vient de la classe mère
        self.__codeEmploye = f"{self.nom[:3].upper()}_{self.prenom[:1]}"