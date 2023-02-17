class Item:

    def __init__(self, description, prix):
        self.description = description
        self.prix = prix

    def __str__(self):
        return f"{self.description} : {self.prix}"