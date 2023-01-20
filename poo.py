# Programmation orientée objet (cours 1 à 5)

# Objet : une entité qui a des attributs et des fonctionnalités.
# Exemple
class Compte:

    def __init__(self, noCompte, nomClient, prenomClient, nas, solde=0):
        """Ceci est un constructeur"""
        self.__noCompte = noCompte
        self.__solde = solde
        self.__nomClient = nomClient
        self.__prenomClient = prenomClient
        self.__nas = nas
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
        return f"No. Compte : {self.__noCompte},\nPrénom du client: {self.__prenomClient}, \nNom du client: {self.__nomClient}, \nNAS: {self.__nas}, \nSolde: {self.__solde}"
    