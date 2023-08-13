from film.film import Film

class FilmDVD(Film):
    """ Défini le type de film en DVD"""

    def __init__(self,):
        """ Initialise le type en DVD"""
        super().__init__()
        self.dvd = "DVD"

    def type(self):
        """ Donne le type du film"""
        return super().type()
    

    def __str__(self) -> str:
        return f"Le film {self.name} est en DVD"