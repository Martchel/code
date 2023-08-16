from movie import Film
from source import films, friends
from collections import defaultdict

class Nettoyage(Film):
    
    def __init__(self, films, friends):
        super().__init__()  # Call the base class's constructor if necessary
        self.films = films
        self.friends = friends

    def clean(self):
            
        dvd_films = []
        vhf_films = []
        borrow_films = defaultdict(list)

        for movie, format in films:
            if format == "DVD" or format == "dvD" or format == "dVd":
                dvd_films.append(movie)
            elif format == "VHF" or format == "vhf" or format == "Vhf":
                vhf_films.append(movie)
        
        for friend_borrow in friends:
            friend = friend_borrow
            movie = friend_borrow[0] if len(friend_borrow)>1 else None
            borrow_films[friend].append(movie)
        

        print("DVD Movies:")
        print(dvd_films)

        print("\nVHF Movies:")
        print(vhf_films)

        print("\nBorrowed Movies:")
        print(borrow_films)
