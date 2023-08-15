import random
from source import films

def hasard(films):
    # pick a random element from a list of strings.
    movie = random.choice(films)
    print(movie)

hasard(films)   