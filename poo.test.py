from poo import Compte

#Test constructeur
Compte1 = Compte("1", "Deshaies", "Genève", "123456789", 10000) 

#Test accesseur
print(Compte1.getsolde())

#Tests mutateurs
print(Compte1.setSolde(20000))
print(Compte1.depot(50000))
print(Compte1.retrait(65000))
print(Compte1.retrait(10000))

print(Compte1.getInformation())

# print(Compte1.__solde) #Ceci donne une erreur parce que l'attribut solde est protégé