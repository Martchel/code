a = "j'apprends python"
print(a)

b = 17
c =35
d = 2
print((b+c)*d)

nom = "marcello"
age = "23"
print(f"Je m'appelle {nom} et j'ai {age} ans")

age = "33"
print(f"{nom} a maintenant {age} ans")

nom = "Marcello"
age = 23
taille = 1.85
est_etudiant = True
print(f"Nom:{nom}")
print(f"age:{age}")
print(f"taille:{taille}")
print(f"est_etudiant:{est_etudiant}")

a = type(nom)
b = type(age)
c = type(taille)
d = type(est_etudiant)
print(f"type nom: {a}")
print(f"type age: {b}")
print(f"type taille: {c}")
print(f"type est_etudiant: {d}")

fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.insert(1, "ananas")
print(fruits)
len(fruits)
fruits.sort()
print(fruits)