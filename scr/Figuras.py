import math
from blessed import Terminal

term = Terminal()

class FiguraGeometrica:
    COLOR = term.pink  

    def area(self):
        return 0

    def perimetro(self):
        return 0

    def mostrar_resultados(self):
        print(self.COLOR + f"Área: {self.area():.2f}")
        print(self.COLOR + f"Perímetro: {self.perimetro():.2f}")

class Rectangulo(FiguraGeometrica):
    COLOR = term.pink

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(FiguraGeometrica):
    COLOR = term.blue

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado
    
class Circulo(FiguraGeometrica):
    COLOR = term.green

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

   

class Triangulo(FiguraGeometrica):
    COLOR = term.magenta

    def __init__(self, lado1, lado2, lado3, base=None, altura=None):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        if self.base is not None and self.altura is not None:
            return (self.base * self.altura) / 2
        else:
            s = self.perimetro() / 2
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
