#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def solicitar_rango():
    while True:
        try:
            entrada = input("Ingrese el rango (ejemplo: '-10' para hasta 10, '20-' para desde 20, o '5 15' para un rango completo): ").strip()
            
            if entrada.startswith("-"):  
                sup = int(entrada[1:])
                return 1, sup
            
            elif entrada.endswith("-"):  
                inf = int(entrada[:-1])
                return inf, 60
            
            else:  
                inf, sup = map(int, entrada.split())
                return inf, sup
        
        except ValueError:
            print("Error: Formato incorrecto. Intente de nuevo.")

def factorial(num):
    if num < 0:
        return "Factorial no definido para números negativos"
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact


inf, sup = solicitar_rango()


for i in range(inf, sup + 1):
    print(f"Factorial de {i} es {factorial(i)}")
