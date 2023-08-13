from film.film import Film

class FilmVHF(Film):
    """ Défini le type de film en vhf"""

    def __init__(self,):
        """ Initialise le type en vhf"""
        super().__init__()
        self.VHF = "VHF"

    def type(self):
        """ Donne le type du film"""
        return super().type()
    

    def __str__(self) -> str:
        return f"Le film {self.name} est en VHF"