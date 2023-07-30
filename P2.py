fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")


nombre_a_gauche = input()
nombre_a_droite = input()

operation = input()

resultat = 0

if (nombre_a_droite.isnumeric() and nombre_a_gauche.isnumeric()) == True:
  match operation:
      case '+':
        resultat = int(nombre_a_droite) + int(nombre_a_gauche)
        print(f"Le résultat de l'opération est: {resultat}")
      case '-':
        resultat = int(nombre_a_gauche) - int(nombre_a_droite)
        print(f"Le résultat de l'opération est: {resultat}")
      case '*':
        resultat = int(nombre_a_droite) * int(nombre_a_gauche)
        print(f"Le résultat de l'opération est: {resultat}")
      case '/':
        if nombre_a_droite == 0:
          print("Erreur: impossible de diviser par zéro.")
        else:
          resultat = int(nombre_a_gauche) / int(nombre_a_droite)
          print(f"Le résultat de l'opération est: {resultat}")
      case _:
        print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.") 
elif nombre_a_droite ==0:
  print("Erreur: impossible de diviser par zéro.")
else:
  print("Erreur: les deux nombres doivent être des nombres entiers")


  