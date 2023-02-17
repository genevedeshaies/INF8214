# Programmation orientée objet (cours 1 à 5)

# Objet : une entité qui a des attributs et des fonctionnalités.
# Exemple
class Compte:

    def __init__(self, noCompte, nomClient, prenomClient, nas, solde=0):
        """Ceci est un constructeur"""
        self.__noCompte = noCompte
        self.__nomClient = nomClient
        self.__prenomClient = prenomClient
        self.__nas = nas
        self.__solde = solde
        # dunder permet de protéger les attributs pour qu'ils ne soient accessibles qu'avec les mutateurs créés.

    def getsolde(self):
        """Ceci est un accesseur"""
        return self.__solde
    
    def setSolde(self, montant):
        """Ceci est un mutateur"""
        self.__solde = montant
        return self.__solde
    
    def depot(self, montant):
        """Ceci est un mutateur"""
        self.__solde += montant
        return self.__solde
    
    def retrait(self, montant):
        """Ceci est un mutateur"""
        if self.__solde >= montant:
            self.__solde -= montant
            return self.__solde
        else:
            return "Insufficient funds"
    
    def getInformation(self):
        """Ceci est une surcharge, parce qu'on réécrit pour la classe une fonction qui existe déjà."""
        return f"""
        No. Compte : {self.__noCompte},
        Prénom du client: {self.__prenomClient}, 
        Nom du client: {self.__nomClient}, 
        NAS: {self.__nas}, 
        Solde: {self.__solde}"""
    
    def eatAccount(self, other):
        """Additionne le solde du compte other au compte self et crée un nouveau compte au nom du client self"""
        solde2 = self.__solde + other.__solde
        return Compte(self.__noCompte+other.__noCompte, self.__nomClient, self.__prenomClient, self.__nas, solde2)


######################################################################33

# POO - Listes chaînées

