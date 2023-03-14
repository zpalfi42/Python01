import sys

class	GotCharacter:
    def __init__(self, first_name=None, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive
        
class	Stark(GotCharacter):
    '''A class representing the Stark family. Or when bad thingshappen to good people'''
    def	__init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        
    def	print_house_words(self):
        print(self.house_words)
        
    def	die(self):
        self.is_alive = False
        
    def	__str__(self) -> str:
        txt = "{} with house {} and house words '{}' is alive? {}".format(self.first_name, self.family_name, self.house_words, self.is_alive)
        return(txt)
        
def	main( ):
    a = Stark("Peter", True)
    a.print_house_words()
    print(a)
    
if __name__ == "__main__":
    main()