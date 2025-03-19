# Propósito del Repositorio

Este repositorio contiene un programa en Python que calcula los números primos en un rango dado. El algoritmo utiliza una técnica eficiente para determinar los números primos y tiene como objetivo ser un ejercicio para aprender sobre la implementación de funciones matemáticas en Python.

---

## Objetivo

El principal objetivo de este repositorio es **calcular los números primos** entre un intervalo definido por el usuario. Este programa ayudará a entender cómo se pueden utilizar los algoritmos matemáticos en la programación para resolver problemas específicos.

---

### **Características Principales**

1. **Función de Cálculo de Números Primos**:
   - El programa usa el algoritmo de la **Criba de Eratóstenes** para determinar los números primos.

2. **Optimización**:
   - El algoritmo está optimizado para manejar rangos más grandes sin una pérdida significativa de rendimiento.

---

## Ingeniería de Software II

### **1. Requisitos del Sistema**

- **Lenguaje de Programación**: Python 3.x
- **Bibliotecas**:
  - math (para funciones matemáticas)
  
### **2. Algoritmo Implementado**

El algoritmo implementado es el de **Criba de Eratóstenes**. Este es uno de los métodos más eficientes para encontrar todos los números primos menores que un número dado.

#### **Pseudocódigo del Algoritmo**

1. Crear una lista booleana `primos` con valores inicializados a `True`.
2. Establecer los índices correspondientes a 0 y 1 como `False`, ya que 0 y 1 no son primos.
3. Iterar sobre cada número desde 2 hasta la raíz cuadrada del número máximo.
4. Marcar como `False` los múltiplos de cada número primo encontrado.

### **3. Casos de Uso**

1. Calcular los números primos entre 1 y 500.
2. Calcular los números primos entre 100 y 1000.

---
## Numeros Primos
https://es.wikipedia.org/wiki/N%C3%BAmero_primo
