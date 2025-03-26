# Conjetura de Collatz

Este repositorio contiene un programa en Python que calcula el número de iteraciones necesarias para que los números entre 1 y 10,000 converjan a la secuencia repetitiva de Collatz (1, 4, 2, 1). El programa genera un gráfico donde el eje X muestra el número inicial de la secuencia y el eje Y muestra el número de iteraciones que tarda en llegar a 1.

---

## Objetivo

El principal objetivo de este repositorio es calcular el número de iteraciones necesarias para que cada número entre 1 y 10,000 de la secuencia de Collatz llegue a 1, y representar estos resultados gráficamente.

---

### **Características Principales**

1. **Cálculo de Iteraciones de Collatz**:
   - El programa calcula el número de iteraciones que tarda un número en llegar a 1 utilizando la conjetura de Collatz.

2. **Gráfico de Iteraciones**:
   - El programa genera un gráfico donde se muestran las iteraciones necesarias para cada número entre 1 y 10,000.

---

## Ingeniería de Software II

### **1. Requisitos del Sistema**

- **Lenguaje de Programación**: Python 3.x
- **Bibliotecas**:
  - `matplotlib` (para generar el gráfico)
  
### **2. Algoritmo Implementado**

La conjetura de Collatz se basa en las siguientes reglas:
1. Si el número es par, se divide entre 2.
2. Si el número es impar, se multiplica por 3 y se le suma 1.
3. Se repiten estos pasos hasta llegar a 1.

El programa calcula cuántas iteraciones toma para que cada número entre 1 y 10,000 llegue a 1.

#### **Pseudocódigo del Algoritmo**

1. Crear una función que calcule el número de iteraciones de Collatz para un número dado.
2. Iterar sobre los números del 1 al 10,000 y calcular el número de iteraciones para cada uno.
3. Guardar los resultados en dos listas: una para los números y otra para las iteraciones.
4. Generar un gráfico de dispersión (scatter plot) donde en el eje X se muestra el número inicial y en el eje Y el número de iteraciones.

### **3. Casos de Uso**

1. Calcular las iteraciones de Collatz para los números entre 1 y 10,000.
2. Generar un gráfico de las iteraciones para cada número en ese rango.
