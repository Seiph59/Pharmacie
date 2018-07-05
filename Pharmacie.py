import sys

class Pharmacie: 
    pass


class Medicament:

    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock
        

class Client:

    def __init__(self, nom, credit):
        self.nom = nom
        self.credit = credit
        


def menu():
    print("""1 : Achat de medicament
2 : Approvisionnement en medicaments
3 : Etats des stocks et des credits
4 : Quitter""")
 
    while True:
        try:
            choix = int(input("Entrez votre choix: "))
            if choix in range(1, 5):
                break
        except ValueError:
            continue
 
    return choix

def affichage(list_clients, list_medicaments):
    print("\nListe clients + credit :")
    print("------------------")

    for client in list_clients:
        print(client.nom, client.credit)

    print("\nListe Medicaments + stock : ")
    print("-----------------------")

    for medicament in list_medicaments:
        print(medicament.nom, medicament.stock)

    print("\n\n")

def lireMedicament(medicControle, list_medicaments):
    
    for medicament in list_medicaments:
        if medicament.nom == medicControle.capitalize():
            return True
    else:    
        return False

def parcoursMedics(listeMedic, entreMed):
    for medicament in listeMedic:
        if medicament.nom == entreMed.capitalize():
            return medicament
        

def approvisionnement(list_medicaments):
    boucle = True
    while boucle != False :
        entreeMedicament = input("Quel medicament souhaitez-vous approvisionner ? : ")
        if lireMedicament(entreeMedicament, list_medicaments):
            entreeStock = int(input("Quel est la quantité à ajouter au stock ? :" ))
            bonMedicament = parcoursMedics(medicaments, entreeMedicament)
            bonMedicament.stock += entreeStock
            boucle = False
    print("nouveau stock : \n" + bonMedicament.nom, bonMedicament.stock)    

def lireClient(clientControle, clientListe):
    for client in clientListe:
        if client.nom == clientControle.capitalize():
            return True
    else:
        return False

def achat(listeClients, listeMedicaments):          
    entreeClient = input(" Nom du client ? :")
    if lireClient(entreeClient, listeClients) == True:
        nomCorrect = False
        while nomCorrect != True:
            entreMedicament = input(" Nom du médicament ? :")
            if lireMedicament(entreMedicament, listeMedicaments) == True:
                nomCorrect = True
            entreeQuantite = int(input("Quantité désirée ? :\n"))

            bonMedic = parcoursMedics(medicaments, entreMedicament)
            if bonMedic.stock < entreeQuantite :
                    print("Achat Impossible. Quantite insuffisante\n stock disponible: " +  str(medicament.stock) + "\n")

            else:
                bonMedic.stock -= entreeQuantite
                entreeMontant = int(input("Montant du paiement : "))
                for client in listeClients:
                    if client.nom == entreeClient.capitalize():
                        print(entreeClient.capitalize())
                        client.credit = client.credit + entreeMontant - bonMedic.prix * entreeQuantite
                        print(client.credit)
                    else: 
                        break           

               

malfichu = Client("Malfichu",0.0)
palichon = Client("Palichon",0.0)
 
aspiron = Medicament("Aspiron", 20.40, 5)
rhinoplexil = Medicament("Rhinoplexil", 19.15, 5)
 
clients = [malfichu, palichon]
medicaments = [aspiron, rhinoplexil]
 
while True:
 
    choix = menu()
 
    if choix == 1:
        achat(clients, medicaments)
    elif choix == 2:
        approvisionnement(medicaments)
    elif choix == 3:
        affichage(clients, medicaments)
    elif choix == 5:
        pass
    else:
       sys.exit()         
 
quitter()


