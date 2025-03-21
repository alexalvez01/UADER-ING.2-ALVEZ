#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys


inf = int(input("Ingrese el extremo inferior: "))
sup = int(input("Ingrese el extremo superior: "))


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

for i in range(inf, sup + 1):
    print(f"Factorial de {i} es {factorial(i)}")