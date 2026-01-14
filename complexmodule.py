class Complex(object): 
    """ Module for complex numbers """

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.real*other.imag + other.real*self.imag)

    def __truediv__(self, other):
     
        denom = other.real**2 + other.imag**2
        if denom == 0:
            raise ZeroDivisionError("division by zero")

        return Complex(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom)


    def __str__(self): 
        return "{0},{1}i".format(self.real, self.imag)

        