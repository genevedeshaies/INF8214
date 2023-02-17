__author__ = "Alix Boc"
__cours__  = "Inf8214"

""" Manipulation d'un compte bancaire utilisant un objet"""

from poo import Compte
from Client import Client

client = Client("Smith", "John", "111222333")
monCompte = Compte ( "12345", client, 1000 )

""" afficher les informations du compte """
print ( "\nCompte apres creation", monCompte )


""" faire un depot """
monCompte.depot(1000)

""" afficher les informations du compte """
print ( "\nCompte apres un depot de 1000$", monCompte )

""" faire un retrait """
monCompte.retrait(500)

""" afficher les informations du compte """
print ( "\nCompte apres un retrait de 500$", monCompte )


""" afficher les informations du client """
print ( "client=", monCompte.getClient() )


""" illustration de l'utilisation de la surcharge de < ( __lt__ ) """
monCompte2 = Compte("", monCompte.getClient(), 10000)
if monCompte < monCompte2:
    print ( "\nLe solde de monCompte est inférieur à celui de c2" )
else:
    print ( "\nLe solde de monCompte est supérieur ou égal à celui de c2" )


""" fusion de compte """
monCompte3 = monCompte + monCompte2
print ( monCompte3 , monCompte3.getClient() )
