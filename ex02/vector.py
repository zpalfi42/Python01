import sys

class   Vector:
    def __init__(self, values) -> None:
        if (isinstance(values, list)):
            self.values = values
            if(len(values) is 1):
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
    
    def __truediv__(self, x):
        if (not isinstance(x, int) or x is 0)
            print("Error: Wrong arguments")
            sys.exit()
        values = []
        for x in range(self.shape[0]):
            value = []
            for y in range(self.shape[1]):
                value.append(self.values[x][y] \ x)
            values.append(value)
        
        v = Vector(values)
        return(v)
    
    
        



def	main( ):
    v1 = Vector([[0.0, 1.0, 2.0, 3.0, 4.0]])
    v2 = Vector([[1.0, 2.0, 3.0, 4.0, 5.0]])
    v3 = v1.__add__(v2)
    print(v3.values)
        
if __name__ == "__main__":
    main()