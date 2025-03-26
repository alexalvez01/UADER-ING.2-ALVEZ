import matplotlib.pyplot as plt


def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations


numbers = []
iterations = []


for i in range(1, 10001):
    numbers.append(i)
    iterations.append(collatz_iterations(i))

plt.figure(figsize=(10, 6))
plt.scatter(numbers, iterations, s=1, color='blue', alpha=0.5)
plt.title('Número de Iteraciones de Collatz')
plt.xlabel('Número inicial')
plt.ylabel('Número de iteraciones hasta 1')
plt.grid(True)
plt.tight_layout()


plt.savefig('collatz_iterations.png')
plt.show()
