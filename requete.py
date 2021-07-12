import requests
import time

url = "https://6007f1a4309f8b0017ee5022.mockapi.io/api/m1/accounts"
continuer = True

while continuer:

    input("Appuyer sur enter pour continuer")
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

    # if choix not in [1,2,3,4,5,6]:
    #print("Tu fais chier, essaye de faire un effort sérieux !")

    if choix == 1:  # Fonctionnel
        iD = input("Identifiant -> ?   ")
        account_name = input("Nom du client -> ?   ")
        amount = input("Montant -> ?   ")
        iban = input("Iban -> ?   ")
        currency = input("Devise -> ?   ")

        newAccount = {
            # 'id' : iD,
            'account_name': account_name,
            'amount': amount,
            'iban': iban,
            'currency': currency
        }

        requete = requests.post(url, newAccount)
        if requete.status_code == 201:
            print("Succès de la requête")
            print(requests.get(f"{url}/{iD}").text)
        else:
            print("Echec de la requête")

    if choix == 2:  # Fonctionnel
        i = 1
        r = requests.get(f"{url}/{i}")
        while r.text != "\"Not found\"":
            i += 1
            print(r.text)
            r = requests.get(f"{url}/{i}")
            time.sleep(1)

    if choix == 3:  # Fonctionnel
        iD = int(input("Identifiant -> ?   "))
        reqResult = requests.get(f"{url}/{iD}")
        print(reqResult.text)  # Changer affichage si trop dégueulasse

    if choix == 4:
        iban = input("Iban -> ?   ")
        reqResult = requests.get(url).text
        i = 0
        cleartext = ""
        while i < len(reqResult):
            if i == '}':
                print(reqResult)

    if choix == 5:
        account_name = input("Nom du client -> ?   ")
        reqResult = requests.get(url).json()
        for account in reqResult:
            if account["account_name"] == account_name:
                print(account)

    if choix == 6:
        #reqResult = requests.get(url)
        #nbId = requests.get(url)
        print(type(requests.get(url)))
