class Film:
    """Classe abstraite utilisée pour définir un film."""
    def __init__(self, name, format):
        """ initialise les informations du film."""
        self.name = name
        self.format =format