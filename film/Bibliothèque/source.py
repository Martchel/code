from ami import Ami
from movie import Film
from bibli import Bibliothèque
from collections import defaultdict

bibliothèque = Bibliothèque()

films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]

for nom, format in films:
    bibliothèque.ajout_film(nom=nom, format=format)

friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]

pret_film = defaultdict(list)
for emprunt_film_ami in friends:
    ami = emprunt_film_ami[0] if len(emprunt_film_ami) > 0 else None
    emprunt_film = emprunt_film_ami[1] if len(emprunt_film_ami) > 1 else None 
    if emprunt_film:
        pret_film[ami].append(emprunt_film)

for nom_ami, nom_film in bibliothèque.preter_film.items():
    print(f"{nom_ami}: {nom_film}")

# Affichage des films empruntés par chaque ami
for ami in bibliothèque.amis:
    if ami.films_empruntes:
        films_empruntes = ", ".join([film.nom for film in ami.films_empruntes])
        print(f"{ami.nom} a emprunté les films : {films_empruntes}")
    else:
        print(f"{ami.nom} n'a pas emprunté de films")

# Tentative d'emprunt supplémentaire pour illustrer le cas où le film est introuvable
print(bibliothèque.preter_film("Paul", "Film inexistant"))