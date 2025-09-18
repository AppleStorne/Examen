from blessed import Terminal #añadimos libreria blessed
from Figuras import Cuadrado, Circulo, Triangulo, Rectangulo #importamos del otro archivo las variables

term = Terminal() #declaramos para añadir color a los textos

def mostrar_menu(): #desplazamos el menu
    print(term.cyan("Calculadora de Figuras Geométricas"))
    print(term.white("1. Rectangulo"))
    print(term.black("2. Cuadrado"))
    print(term.green("3. Triangulo"))
    print(term.blue("4. Circulo"))
    print(term.pink("5. Salir"))

def main():
    while True:
        mostrar_menu()
        opcion = input(term.yellow("Seleccione una opción: "))

        if opcion == '1':
            base = float(input(term.cyan("Ingrese la base del rectángulo: ")))
            altura = float(input(term.cyan("Ingrese la altura del rectángulo: ")))
            figura = Rectangulo(base, altura)
            figura.mostrar_resultados()
        
        elif opcion == '2':
            lado = float(input(term.cyan("Ingrese el lado del cuadrado: ")))
            figura = Cuadrado(lado)
            figura.mostrar_resultados()

        elif opcion == '3':
            print(term.red("¿Cómo desea calcular el área del triángulo?"))
            print(term.pink("a) Base y altura"))
            print("b) Tres lados (fórmula de Herón)")
            sub_opcion = input(term.yellow("Seleccione opción (a/b): ")).lower()

            if sub_opcion == 'a':
                base = float(input(term.cyan("Ingrese la base: ")))
                altura = float(input(term.cyan("Ingrese la altura: ")))
                lado1 = float(input(term.cyan("Ingrese lado 1: ")))
                lado2 = float(input(term.cyan("Ingrese lado 2: ")))
                lado3 = float(input(term.cyan("Ingrese lado 3: ")))
                figura = Triangulo(lado1, lado2, lado3, base=base, altura=altura)
                figura.mostrar_resultados()

            elif sub_opcion == 'b':
                lado1 = float(input(term.cyan("Ingrese lado 1: ")))
                lado2 = float(input(term.cyan("Ingrese lado 2: ")))
                lado3 = float(input(term.cyan("Ingrese lado 3: ")))
                figura = Triangulo(lado1, lado2, lado3)
                figura.mostrar_resultados()

            else:
                print(term.red("Opción inválida"))


        elif opcion == '4':
            radio = float(input(term.cyan("Ingrese el radio del círculo: ")))
            figura = Circulo(radio)
            figura.mostrar_resultados()

        elif opcion == '5':
            print(term.green("Saliendo del programa"))
            break

        else:
            print(term.red("Opción inválida, intente de nuevo."))

        print()  
if __name__ == "__main__":
    main()
