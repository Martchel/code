from movie import Film
from ami import Ami

class Bibliothèque:
    """Classe Bibliothèque pour information sur les films.
    """
    def __init__(self):
        """Initialise la classe.
        """
        self.films = []
        self.amis = []

    def ajout_film(self, nom, format):
        """Ajoute un film dans la liste film.

        Args:
            nom (str): nom du film
            format (str): type du film
        """
        film = Film(nom, format)
        self.films.append(film)

    def ajout_ami(self, nom):
        """Ajoute un ami dans la bibliothèque.

        Args:
            nom (str): nom de l'ami(e)
        """
        ami = Ami(nom)
        self.amis.append(ami)

    def trouver_film(self, nom_film):
        """Trouve un film dans la lsite de films.

        Args:
            nom_film (str): nom du film

        Returns:
            None: si le film n'existe pas.
        """
        for film in self.films:
            if film.name == nom_film:
                return film
        return None
    
    def preter_film(self, nom_ami, nom_film):
        """Films prétés.

        Args:
            nom_ami (str): nom de l'ami(e)
            nom_film (str): nom du film

        Returns:
            str: "ami introuvable"
        """
        ami =None
        for a in self.amis:
            if a.nom == nom_ami:
                ami = a
                break
        
        if ami is None:
            return "ami introuvable"
        
        film = self.trouver_film(nom_film)
        if film is None:
            return "Film introuvable"
        
        ami.emprunt_film(film)
        return f"{nom_ami} a emprunté: {nom_film}"