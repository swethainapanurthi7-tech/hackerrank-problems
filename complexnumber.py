import math
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imag = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imag)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        real = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imag = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(real, imag)
    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            return f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            if self.imaginary >= 0:
                return f"0.00+{self.imaginary:.2f}i"
            else:
                return f"0.00-{abs(self.imaginary):.2f}i"
        else:
            if self.imaginary >= 0:
                return f"{self.real:.2f}+{self.imaginary:.2f}i"
            else:
                return f"{self.real:.2f}-{abs(self.imaginary):.2f}i"
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='
