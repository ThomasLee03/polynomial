class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x_value):
        # Returns the value of X, which is the variable itself
        return x_value

class Int:
    def __init__(self, i):
        self.i = i  # Ensure you store the value properly in self.i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x_value):
        # An integer evaluates to itself, independent of X
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x_value):
        # Evaluate both parts and add their values
        return self.p1.evaluate(x_value) + self.p2.evaluate(x_value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x_value):
        # Evaluate both parts and multiply their values
        return self.p1.evaluate(x_value) * self.p2.evaluate(x_value)

# Example polynomial:
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))

# Print the polynomial and evaluate it for X = -1
print(poly)
print(poly.evaluate(-1))  # This should evaluate the polynomial when X = -1
