__author__ = "Alix Boc"

import random

prenoms = ["Tamesha","Mireille","Doloris","Alona","Keneth","Selene","Myrta","Mathew","Dylan","Edwardo","Deedra","Elizbeth","Lance","Luis","Chanda","Emilie"]
noms = ["Rayo","Lepage","Finlayson","Dauphinais","Mcie","Baginski","Macarthur","Watwood","Kreidler","Huang"]

class Personne:

    __nbPersonnes = 0

    def __init__ (self, nom=None, prenom=None, nas=None):
        if nom == None:
            nom = Personne.getNom()
        if prenom == None:
            prenom = Personne.getPrenom()
        if nas == None:
            nas = Personne.getNas()

        self.__nom = nom
        self.__prenom = prenom
        self.__nas = nas
        Personne.__nbPersonnes += 1

    def nbPersonnes():
        return str(Personne.__nbPersonnes)

    @property
    def nom(self):
        return self.__nom + "[Personne]"

    @property
    def prenom(self):
        return self.__prenom

    @property
    def nas(self):
        return self.__nas

    @nas.setter
    def nas(self,nas):
        self.__nas = nas


    def __str__(self):
        return "Je suis une personne [" + self.__nom + ", " + self.__prenom + ", " + self.__nas + "]"


    def getNom():
        return noms[ random.randint(0,len(noms)-1) ]

    def getPrenom():
        return prenoms[ random.randint(0,len(prenoms)-1) ]

    def getNas():
        return str(random.randint(100,999)) + str(random.randint(100,999)) + str(random.randint(100,999))
