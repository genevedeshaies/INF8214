#==============================================================================
#= Programme principal. Ce script utilise la classe Facture à écrire
#=
#= Atelier facturation
#= Auteur : Alix Boc
#==============================================================================
from Facture import Facture

def selectionFacturesFusion(factures):
    return(selectionFactures(factures),selectionFactures(factures))

def afficherItems(facture):
    print("\nListe des items de la facture",facture.getNoFacture())
    if facture.nbItems() > 0:
        for i in range(0,facture.nbItems):
            print(i,":",facture.getItem(i).description(),facture.getItem(i).prix())
    else:
        print("aucun item")

def supprimerItem(facture):
    print("\nSaisir le numéro de l'item à supprimer, appuyer sur Enter pour terminer : ")
    """ TO DO """


def ajouterItems(facture):
    description = "first"
    prix = 0
    print("\nSaisir les items, appuyer sur Enter pour terminer : ")
    while description != "":
        description = input("Description : ")
        if description != "":
            prix = float(input("Prix : "))
            facture.ajouterItem(description,prix)

def selectionFactures(factures):
    print("\nSélectionner une facture : ")
    for i in range(0,len(factures)):
        print(i,factures[i].noFacture)
    if len(factures) == 0:
        print("\nAucune facture\n")
        return None
    else:
        return factures[int(input("\nVotre choix : "))]

def afficherMenu():
    print("\n")
    print("1. Créer une nouvelle facture")
    print("2. Ajouter des items à une facture")
    print("3. Supprimer des items d'une facture")
    print("4. Afficher une facture")
    print("5. Fusionner deux factures")
    print("6. Quitter")
    return int(input("\nVotre choix : "))

factures = []
choix = 0

while( choix != 6 ):
    choix = afficherMenu()
    if choix == 1:
        facture = Facture()
        factures.append(facture)
        print("\n\nLa facture ", facture.noFacture, "a été ajouté")

    elif choix == 2:
        facture = selectionFactures(factures)
        ajouterItems(facture)

    elif choix == 3:
        facture = selectionFactures(factures)
        """ TO DO """

    elif choix == 4:
        facture = selectionFactures(factures)
        if facture != None:
            print("\n\nDétails de la facture :\n")
            print(facture)

    elif choix == 5:
        (facture1,facture2) = selectionFacturesFusion(factures)
        if (facture1 != None) and (facture2 != None):
            print("\n\nFusion des factures ", facture1.noFacture, "et", facture2.noFacture)
            facture3 = facture1 + facture2
            print(facture3)
