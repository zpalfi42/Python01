from	recipe import Recipe
import	sys

def main( args ):
    tarta = Recipe("a", 4, 10, ["a", "b"], "Tarta muy buena", "postre")
    a = str(tarta)
    print(a)

if __name__ == "__main__":
    main( sys.argv )