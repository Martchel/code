from abc import ABC, abstractmethod


class Film(ABC):
    """Classe abstraite utilisée pour définir un film."""

    @abstractmethod
    def type(self):
        """Toutes les sous-classes de Film doivent implémenter type."""
        pass

    def __init__(self, name, date, location):
        """ initialise les informations du film."""
        self.name = name
        self.date = date
        self.location = location