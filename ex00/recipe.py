import sys

class Recipe:
    def __init__(self, name, level, time, ingredients, description, type) -> None:
        if (not isinstance(name, str) or len(name) is 0):
            print("ERROR: Not a valid name")
            sys.exit()
        self.name = name
        
        if (not isinstance(level, int) or level > 5 or level < 1):
            print("ERROR: Not a valid level")
            sys.exit()
        self.cooking_lvl = level
        
        if (not isinstance(time, int) or time < 0):
            print("ERROR: Not a valid time")
            sys.exit()
        self.cooking_time = time
        
        if (not isinstance(ingredients, list) or len(ingredients) is 0):
            print("ERROR: Not a valid ingredients")
            sys.exit()
        self.ingredients= ingredients
        
        self.description = description
        
        if (not isinstance(type, str) or (type is not "entrante" and type is not "comida" and type is not "postre")):
            print("ERROR: Not a valid type")
            sys.exit()
        self.recipe_type = type
    
    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        txt = "Recipe name: {}\nNeccessary level: {}\nCooking time: {}\nIngredients: {}\nDescription: {}\nRecipe type: {}\n".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients,self.description, self.recipe_type)
        """Your code here"""
        return txt