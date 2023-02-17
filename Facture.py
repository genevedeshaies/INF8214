import datetime
from Item import Item


class Facture:

    def __init__(self):
        self.__noFacture__ = int(datetime.datetime.now().timestamp())
        self.__items__ = []
        self.__nbItems__ = 0


    @property #l'équivalent de getNoFacture...
    def noFacture(self):
        return self.__noFacture__


    def ajouterItem(self, description, prix):
        item = Item(str(description), float(prix))
        self.__items__.append(Item.__str__(item))
        self.__nbItems__ += 1
    

    def __str__(self):
        chaine = f"Facture {str(self.__noFacture__)} \n"
        for i in self.__items__:
            chaine += f"{i}$ \n"
        return chaine


    def __add__(self, other):
        facture3 = Facture()
        facture3.__items__ = self.__items__ + other.__items__
        facture3.__nbItems__ = self.__nbItems__ + other.__nbItems__

        # facture3.__items__.append(self.__items__)
        # facture3.__items__.append(other.__items__)
        return facture3

