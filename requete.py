from typing import Container
import requests

url = "https://6007f1a4309f8b0017ee5022.mockapi.io/api/m1/accounts"
continuer = True

while continuer:

    print("Bienvenue au sein de cette API bancaire")
    print()
    print("----------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("                                     Bienvenue au sein de cette API bancaire                                          ")
    print("                                                                                                                      ")
    print("||       1. Ajout d'un compte                                                                                       ||")
    print("||       2. Afficher l'ensemble des comptes                                                                         ||")
    print("||       3. Recherche d'un compte par n°id                                                                          ||")
    print("||       4. Recherche d'un compte par Iban                                                                          ||")
    print("||       5. Recherche d'un compte par nom                                                                           ||")
    print("||       6. Tri de richesse sur les comptes                                                                         ||")
    print("                                                                                                                      ")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("                                                                                                                      ")
    print("                                                                                                                      ")
    choix = int(input("-> ?   "))

    #if choix not in [1,2,3,4,5,6]:
        #print("Tu fais chier, essaye de faire un effort sérieux !")
    if choix == 1:
        iD = input("Identifiant -> ?   ")
        account_name = input("Nom du client -> ?   ")
        amount = input("Montant -> ?   ")
        iban = input("Iban -> ?   ")
        currency = input("Devise -> ?   ")

        newAccount = {
            'id' : iD,
            'account-name' : account_name,
            'amount' : amount,
            'iban' : iban,
            'currency' : currency
        }

        


