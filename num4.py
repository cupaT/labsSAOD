import matplotlib.pyplot as plt
import time

# Рекурсивная функция для вычисления n-го числа Фибоначчи.
def fibonacci(n):
    # F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # F(n) = F(n - 1) + F(n - 2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Рекурсивная функция для вычисления n-го числа Люка.
def lucas(n):
    # L(0) = 2, L(1) = 1
    if n == 0:
        return 2
    elif n == 1:
        return 1
    # L(n) = L(n - 1) + L(n - 2)
    else:
        return lucas(n - 1) + lucas(n - 2)

# Функция для вычисления числа Люка через числа Фибоначчи.
def lucas_with_fib(n):
    # LN = FN-1 + FN+1
    if n == 0:
        return 2
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n + 1)

# Функция для вычисления числа Фибоначчи через числа Фибоначчи и Люка.
def fib_with_lucas(n):
    # F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Fn = ((Fi + Lj) * (Fj + Li)) // 2, где i = n // 2, j = n - i
    i = n // 2
    j = n - i
    Fi = fib_with_lucas(i)
    Fj = fib_with_lucas(j)
    Li = lucas_with_fib(i)
    Lj = lucas_with_fib(j)
    return ((Fi + Lj) * (Fj + Li)) // 2

if __name__ == "__main__":
    # Сравнение времени работы двух способов вычисления чисел Фибоначчи.
    sizes = list(range(1, 35))
    times_fib = []
    times_fib_lucas = []

    for n in sizes:
        start = time.perf_counter()
        fibonacci(n)
        times_fib.append(time.perf_counter() - start)

        start = time.perf_counter()
        fib_with_lucas(n)
        times_fib_lucas.append(time.perf_counter() - start)

    # Построение графика сравнения быстродействия двух функций.
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, times_fib, 'o-', label='fibonacci(n)')
    plt.plot(sizes, times_fib_lucas, 'o-', label='fib_with_lucas(n)')
    plt.title("Сравнение быстродействия функций Фибоначчи")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()