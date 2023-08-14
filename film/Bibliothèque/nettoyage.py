from movie import Film
from source import films

class Nettoyage(Film):

    dvd_films = []
    vhf_films = []

    for movie, format in films:
        if format == "DVD" or format == "dvD":
            dvd_films.append(movie)
        elif format == "VHF" or format == "vhf":
            vhf_films.append(movie)

    print("DVD Movies:")
    for movie in dvd_films:
        print(movie)

    print("\nVHF Movies:")
    for movie in vhf_films:
        liste_film = (movie)
        print([liste_film])