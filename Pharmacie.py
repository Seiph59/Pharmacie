import sys
import matplotlib.pyplot as plt 

class BaseGraph: 
    
    def __init__(self):
        self.show_grid = True
        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "Y-axis label"
        
    
    def show(self, historiqueAspiron):
        x_values, y_values = self.xy_values(historiqueAspiron)
        self.plot(x_values, y_values)
        
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def plot(self, x_values, y_values):
        plt.plot(x_values, y_values, '.')
    
    def xy_values(self,historiques):
        return x_values, y_values
        raise NotImplementedError

class AspironGraph(BaseGraph):
    
    def __init__(self):

        super(AspironGraph, self).__init__()

        self.title = "Evolution du stock d'Aspiron"
        self.x_label = "Période"
        self.y_label = "Stock disponible"

    def xy_values(self, historiqueAspiron):
        x_values = [i for i in range(0,len(historiqueAspiron))]
        y_values = [aspi for aspi in historiqueAspiron]
        return x_values, y_values

class RhinoplexilGraph(BaseGraph):
    
    def __init__(self):

        super(RhinoplexilGraph, self).__init__()

        self.title = "Evolution du stock de Rhinoplexil"
        self.x_label = "Période"
        self.y_label = "Stock disponible"

    def xy_values(self, historiqueRhinoplexil):
        x_values = [i for i in range(0,len(historiqueRhinoplexil))]
        y_values = [aspi for aspi in historiqueRhinoplexil]
        return x_values, y_values


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
4 : Affichage Graph
5 : Quitter""")
 
    while True:
        try:
            choix = int(input("Entrez votre choix: \n"))
            if choix in range(1, 6):
                break
        except ValueError:
            continue
 
    return choix

def menuGraph():
    print("""Quel Graph souhaitez-vous afficher ?
1: Evolution des Stocks Aspiron
2: Evolution des Stocks Rhinoplexil""")
 
    while True:
        try:
            choix2 = int(input("Entrez votre choix:\n"))
            if choix2 in range(1, 3):
                break
        except ValueError:
            continue
 
    return choix2

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
            if bonMedicament == aspiron:
                historiqueAspiron.append(bonMedicament.stock)
                print(historiqueAspiron)
            elif bonMedicament == rhinoplexil:
                historiqueRhinoplexil.append(bonMedicament.stock)
                print (historiqueRhinoplexil)
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
                bonMedic.stock  -= entreeQuantite
                if bonMedic == aspiron:
                    historiqueAspiron.append(bonMedic.stock)
                    print(historiqueAspiron)
                elif bonMedic == rhinoplexil:
                    historiqueRhinoplexil.append(bonMedic.stock)
                    print (historiqueRhinoplexil)
                entreeMontant = int(input("Montant du paiement : "))
                for client in listeClients:
                    if client.nom == entreeClient.capitalize():
                        print(entreeClient.capitalize())
                        client.credit = client.credit + entreeMontant - bonMedic.prix * entreeQuantite
                        print(client.credit)
                    else: 
                        break           

historiqueAspiron =[5]
historiqueRhinoplexil = [5]               

malfichu = Client("Malfichu",0.0)
palichon = Client("Palichon",0.0)
 
aspiron = Medicament("Aspiron", 20.40,historiqueAspiron[-1])
rhinoplexil = Medicament("Rhinoplexil", 19.15,historiqueRhinoplexil[-1])


 
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
    elif choix == 4:
        choix2= menuGraph()
        if choix2 == 1:
            graph_aspiron = AspironGraph()
            graph_aspiron.show(historiqueAspiron)
        if choix2 ==2:
            graph_rhinoplexil = RhinoplexilGraph()
            graph_rhinoplexil.show(historiqueRhinoplexil)
    else:
       sys.exit()         
 
quitter()


