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

Compte2 = Compte("2", "Lemieux", "Mathieu", "234567891", 10000)

print(Compte2.getInformation())

Compte3 = Compte1.eatAccount(Compte2)

print(Compte3.getInformation())
# print(Compte1.__solde) #Ceci donne une erreur parce que l'attribut solde est protégé