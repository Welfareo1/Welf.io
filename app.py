print("=== Welf.io ===")

while True:
    print("\n1. Se connecter")
    print("2. Informations")
    print("3. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom d'utilisateur : ")
        print(f"Bienvenue {nom} !")

    elif choix == "2":
        print("Welf.io - Application de démonstration.")

    elif choix == "3":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")
