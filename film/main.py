from Bibliothèque.movie import Film

from Bibliothèque.dvd import FilmDVD
from Bibliothèque.vhf import FilmVHF


def main():
    """Programme Principal.
    """
alice = Film("Alice", FilmDVD("DVD"))
bob = Film("Bob", FilmVHF("VHF"))


if __name__ == "__main__":
    main()