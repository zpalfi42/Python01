import sys

class   Vector:
    def __init__(self, values) -> None:
        if (isinstance(values, list)):
            self.values = values
            if(len(values) == 1):
                self.shape = (1, len(values[0]))
            else:
                self.shape = (len(values), 1)
        
        if (isinstance(values, int)):
            self.values = []
            for i in range(values):
                self.values.append([float(i)])
            self.shape = (values, 1)
            
        if (isinstance(values, tuple)):
            if (len(values) > 2 or values[0] > values[1]):
                print("Error: Invalid vector initialization with invalid tuple!")
                sys.exit()
            self.values = []
            for i in range(values[0], values[1]):
                self.values.append([float(i)])
            self.shape = (len(values), 1)
            
    def dot(self, v):
        if (not isinstance(v, Vector)):
            print("Error: Not a valid argument.")
            sys.exit()
        
        if (self.shape[0] is not v.shape[0] and self.shape[1] is not v.shape[1]):
            print("Error: vector have not the same shape.")
            sys.exit()
        
        res = 0
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                res += self.values[x][y] * v.values[x][y]
        return res
    
    def T(self):
        values = []
        for x in range(self.shape[1]):
            value = []
            for y in range(self.shape[0]):
                value.append(self.values[y][x])
            values.append(value)
        v = Vector(values)
        return (v)
    
    def __add__(self, vx):
        if (not isinstance(vx, Vector) or self.shape[0] is not vx.shape[0] or self.shape[1] is not vx.shape[1]):
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(float(self.values[x][y] + vx.values[x][y]))
            values.append(value)
        
        v = Vector(values)
        return(v)

    def __radd__(self, vx):
        if (not isinstance(vx, Vector) or self.shape[0] is not vx.shape[0] or self.shape[1] is not vx.shape[1]):
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(float(self.values[x][y] + vx.values[x][y]))
            values.append(value)
        
        v = Vector(values)
        return(v)
    
    def __sub__(self, vx):
        if (not isinstance(vx, Vector) or self.shape[0] is not vx.shape[0] or self.shape[1] is not vx.shape[1]):
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(float(self.values[x][y] - vx.values[x][y]))
            values.append(value)
        
        v = Vector(values)
        return(v)

    def __rsub__(self, vx):
        if (not isinstance(vx, Vector) or self.shape[0] is not vx.shape[0] or self.shape[1] is not vx.shape[1]):
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(float(self.values[x][y] - vx.values[x][y]))
            values.append(value)
        
        v = Vector(values)
        return(v)
    
    def __truediv__(self, ix):
        if (not isinstance(ix, int) and not isinstance(ix, float)):
            print("Error: Wrong arguments")
            sys.exit()
        if (ix == 0):
            raise ZeroDivisionError("Division by zero")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(self.values[x][y] / ix)
            values.append(value)
        
        v = Vector(values)
        return(v)

    def ___rtruediv__(self, x):
        raise   NotImplementedError("Division of a scalar by a Vector is not defined here.")
    
    def __mul__(self, ix):
        if (not isinstance(ix, float) and not isinstance(ix, int)):
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(self.values[x][y] * ix)
            values.append(value)
            
        v = Vector(values)
        return(v)

    def __rmul__(self, ix):
        if (not isinstance(ix, float) and not isinstance(ix, int)):
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(ix * self.values[x][y])
            values.append(value)
            
        v = Vector(values)
        return(v)
    
    def __str__(self) -> str:
        txt = str(self.values)
        return (txt)
    
    def __repr__(self) -> str:
        txt = str(self.values)
        return(txt)
        

def	main( ):
    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output:
    # Vector([[0.0], [5.0], [10.0], [15.0]])
    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output
    # Vector([[0.0, 5.0, 10.0, 15.0]])
    v2 = v1 / 2.0
    print(v2)
    # Expected output
    # Vector([[0.0], [0.5], [1.0], [1.5]])
    # v1 / 0.0
    # Expected ouput
    # ZeroDivisionError: division by zero.
    2.0 / v1
        
if __name__ == "__main__":
    main()