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
            return "trouvé"
    else:    
        return "j'ai pas trouvé le medicament"

def approvisionnement(list_medicaments):
    boucle = 1
    while boucle != 0 :
        entreeMedicament = input("Quel medicament souhaitez-vous approvisionner ? : ")
        lireMedicament(entreeMedicament, list_medicaments)
        if lireMedicament(entreeMedicament, list_medicaments) =="trouvé":
            entreeStock = int(input("Quel est la quantité à ajouter au stock ? :" ))
            for medicament in medicaments:
                if medicament.nom == entreeMedicament.capitalize():
                    medicament.stock = medicament.stock + entreeStock
            boucle = 0
    print("nouveau stock : \n" + aspiron.nom, aspiron.stock)    

def lireClient(clientControle, clientListe):
    for client in clientListe:
        if client.nom == clientControle.capitalize():
            return "trouvé"
    else:
        return "j'ai pas trouvé le client"

def achat(listeClients, listeMedicaments):          
    entreeClient = input(" Nom du client ? :")
    lireClient(entreeClient, listeClients)
    if lireClient(entreeClient, listeClients) == "trouvé":
        nomCorrect = False
        while nomCorrect != True:
            entreMedicament = input(" Nom du médicament ? :")
            lireMedicament(entreMedicament, listeMedicaments)
            if lireMedicament(entreMedicament, listeMedicaments) == "trouvé":
                nomCorrect = True
            entreeQuantite = int(input("Quantité désirée ? :\n"))
            for medicament in listeMedicaments:
                if medicament.nom == entreMedicament.capitalize():
                    if medicament.stock < entreeQuantite :
                        print("Achat Impossible. Quantite insuffisante\n stock disponible: " +  str(medicament.stock) + "\n")

                    else:
                        medicament.stock -= entreeQuantite
                        entreeMontant = int(input("Montant du paiement : "))
                        for client in listeClients:
                            if client.nom == entreeClient.capitalize():
                                print(entreeClient.capitalize())
                                client.credit = client.credit + entreeMontant - medicament.prix * entreeQuantite
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
    else:
       sys.exit()         
 
quitter()


