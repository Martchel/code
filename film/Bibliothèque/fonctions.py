import random
from source import films, friends
from collections import defaultdict

def hasard(films):
    # pick a random element from a list of strings.
    movie = random.choice(films)
    print("Chosen movie:\n" +str(movie)+"\n")


def sort(films):
    sorted_films = sorted(films, key=lambda x: int(x[0].split("(")[-1].split(")")[0]))

    # Afficher les films triés
    print("Sorted movies:")
    for film in sorted_films:
        print(film)
    return print("\n")

def borrow(friends):
    borrow_films = defaultdict(list)
    
    for friend_borrow in friends:
        friend = friend_borrow[0] if len(friend_borrow) > 1 else None
        movie = friend_borrow[1] if len(friend_borrow) > 1 else None
        if friend and movie:
            borrow_films[friend].append(movie)
    
    list_borrow = [(friend, borrowed_movies) for friend, borrowed_movies in borrow_films.items()]
    return list_borrow
        # print(f"Borrowed movies for {friend}:\n{borrowed_movies}")

def friend_borrow(friends):
    list_friends = []
    if isinstance(friends, str):
        friends_name = [friends.split(':')[0]]
        list_friends.append(friends_name)
    print(list_friends)


hasard(films)

sort(films)


print("Borrowed movies list: ")
for friend, movies in borrow(friends):
    print(f"{friend}: {movies}")
