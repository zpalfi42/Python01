import sys
import datetime

class Book:
    def	__init__(self, name, last, creation, recipes) -> None:
        if (not isinstance(name, str) or len(name) is 0):
            print("ERROR: Not a valid name")
            sys.exit()
        self.name = name
        
        if (not isinstance(last, datetime)):
            print("ERROR: Not a valid last update")
            sys.exit()
        self.last_update = last
        
        if (not isinstance(creation, datetime)):
            print("ERROR: Not a valid creation")
            sys.exit()
        self.creation = creation
        
        if (not isinstance(recipes, dict) or len(recipes) is 0):
            print("ERROR: Not a valid recipe list")
            sys.exit()
        self.recipe_list = recipes

    def get_recipe_by_name(self, name):
        print("a")
    
    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        print("b")
        
    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        print("c")