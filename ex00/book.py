import sys
import datetime
from typing import List, Dict
from recipe import Recipe

class Book:
    
    def	__init__(self, name, last, creation, recipes: Dict[str, List[Recipe]]) -> None:
        if (not isinstance(name, str) or len(name) is 0):
            print("ERROR: Not a valid name")
            sys.exit()
        self.name = name
        
        if (not isinstance(last, datetime.datetime)):
            print("ERROR: Not a valid last update")
            sys.exit()
        self.last_update = last
        
        if (not isinstance(creation, datetime.datetime)):
            print("ERROR: Not a valid creation")
            sys.exit()
        self.creation = creation
        
        if (not isinstance(recipes, dict) or len(recipes) is 0):
            print("ERROR: Not a valid recipe dict")
            sys.exit()
        for recipe in recipes.keys():
            if recipe != "starter" or recipe != "launch" or recipe != "dessert":
                print("ERROR: Not a valid recipe dict")
                sys.exit()
        self.recipe_list = recipes

    def get_recipe_by_name(self, name):
        for recipe in self.recipe_list.get("starter"):
            if (name is recipe):
                print(recipe)
                return(recipe)
        for recipe in self.recipe_list.get("launch"):
            if (name is recipe):
                print(recipe)
                return(recipe)
        for recipe in self.recipe_list.get("dessert"):
            if (name is recipe):
                print(recipe)
                return(recipe)
    
    def get_recipes_by_types(self, recipe_type):
        for recipe in self.recipe_list.keys():
            if (recipe_type is recipe):
                return(self.recipe_list.get(recipe))
        
    def add_recipe(self, recipe: Recipe):
        if (recipe.recipe_type is "entrante"):
            lst = self.recipe_list.get("starter")
            lst.append(recipe)
            self.recipe_list.update({"starter":lst})
        if (recipe.recipe_type is "comida"):
            lst = self.recipe_list.get("launch")
            lst.append(recipe)
            self.recipe_list.update({"launch":lst})
        if (recipe.recipe_type is "postre"):
            lst = self.recipe_list.get("dessert")
            lst.append(recipe)
            self.recipe_list.update({"dessert":lst})
        self.last_update = datetime.datetime()