# **Cálculo de Números Primos y Factoriales en Python**

Este repositorio contiene programas en Python para el cálculo de **números primos** y **factoriales** dentro de un rango dado. Los algoritmos utilizados son eficientes y buscan ser un ejercicio de aprendizaje sobre la implementación de funciones matemáticas en Python.

---

##  **Objetivo**

El principal objetivo de este repositorio es permitir el cálculo de:

1. **Números primos** en un intervalo definido por el usuario, utilizando un algoritmo eficiente.
2. **Factoriales** de números en un rango dado, asegurando que el usuario ingrese valores correctos y permitiendo el uso de formatos personalizados para definir el intervalo.

Estos programas ayudarán a comprender cómo se pueden aplicar los algoritmos matemáticos en la programación para resolver problemas específicos.

---

##  **Características Principales**

###  **Cálculo de Números Primos**
- Implementado con el algoritmo de la **Criba de Eratóstenes**.
- Optimizado para manejar rangos grandes sin una pérdida significativa de rendimiento.

###  **Cálculo de Factoriales**
- Permite calcular factoriales de un número o de un rango definido por el usuario.
- Soporta rangos personalizados, permitiendo ingresar valores con los formatos:
  - **`-hasta`** → Calcula desde `1` hasta el número indicado.
  - **`desde-`** → Calcula desde el número indicado hasta `60`.
- Manejo de errores para asegurarse de que el usuario ingrese un número válido.

---

## **Requisitos del Sistema**

- **Lenguaje de Programación**: Python 3.x  
- **Bibliotecas necesarias**:
  - `math` (para funciones matemáticas)

---

## **Algoritmos Implementados**

###  **A) Algoritmo de Números Primos (Criba de Eratóstenes)**
Uno de los métodos más eficientes para encontrar todos los números primos menores que un número dado.

**Pseudocódigo:**
1. Crear una lista booleana `primos` con valores inicializados a `True`.
2. Establecer los índices correspondientes a 0 y 1 como `False`, ya que 0 y 1 no son primos.
3. Iterar sobre cada número desde 2 hasta la raíz cuadrada del número máximo.
4. Marcar como `False` los múltiplos de cada número primo encontrado.

###  **B) Algoritmo de Factorial**
El programa calcula el factorial de un número mediante un enfoque iterativo:

1. Se solicita al usuario ingresar los valores del rango.
2. Se valida la entrada para asegurarse de que sean números correctos.
3. Si el usuario introduce `-hasta`, se asume que el rango es desde `1` hasta ese número.
4. Si el usuario introduce `desde-`, se asume que el rango es desde ese número hasta `60`.
5. Se calcula el factorial de cada número en el rango utilizando un bucle.

---

##  **Casos de Uso**
- Calcular los números primos entre `1` y `500`.  
- Calcular los números primos entre `100` y `1000`.  
- Calcular el factorial de un número específico.  
- Calcular los factoriales de todos los números entre `1` y `N` (`-hasta`).  
- Calcular los factoriales de todos los números entre `M` y `60` (`desde-`).  

---

## **Referencias**
- Números Primos
  
  https://es.wikipedia.org/wiki/N%C3%BAmero_primo](https://www.smartick.es/blog/matematicas/numeros-enteros/numeros-primos-y-numeros-compuestos/

- Factorial
  
  https://es.wikipedia.org/wiki/Factorial



