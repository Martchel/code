class Ami:
    """Classe Ami avec informations sur ami(e)s et le film emprunté.
    """
    def __init__(self, nom):
        """Initialise la classe Ami.

        Args:
            nom (str): nom des ami(e)s.
        """
        self.nom = nom
        self.films_empruntes = []


    def emprunt_film(self, film):
        """Créé une liste de film empruntés.

        Args:
            film (liste): liste des films empruntés.
        """
        self.films_empruntes.append(film)