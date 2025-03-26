class Factorial:
    def __init__(self):
        """Constructor de la clase Factorial"""
        pass

    def calcular(self, num):
        """Método para calcular el factorial de un número"""
        if num < 0:
            return "Factorial no definido para números negativos"
        elif num == 0 or num == 1:
            return 1
        else:
            fact = 1
            for i in range(2, num + 1):
                fact *= i
            return fact

    def run(self, min_value, max_value):
        """Método para calcular el factorial de números entre min y max"""
        for i in range(min_value, max_value + 1):
            print(f"Factorial de {i} es {self.calcular(i)}")


if __name__ == "__main__":
    while True:
        try:
            rango = input("Ingrese el rango en formato '-hasta', 'desde-', o un solo número: ").strip()

            if rango.startswith("-") and rango[1:].isdigit():  
                
                min_value = 1
                max_value = int(rango[1:])

            elif rango.endswith("-") and rango[:-1].isdigit():
                
                min_value = int(rango[:-1])
                max_value = 60

            elif rango.isdigit():
                
                min_value = int(rango)
                max_value = int(input("Ingrese el otro extremo del rango: ").strip())

            else:
                print("Formato inválido. Intente de nuevo.")
                continue  

            if min_value > max_value:
                print("El límite inferior no puede ser mayor que el superior.")
                continue  

            factorial_obj = Factorial()
            factorial_obj.run(min_value, max_value)
            break

        except ValueError:
            print("Ingrese un número válido.")