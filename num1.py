#1
# 1) Функция foo(i) преобразует целое число i в строку.
# 2) Вычислительная сложность функции foo(i) составляет O(d), где d - количество цифр в числе i.

import time
import matplotlib.pyplot as plt

def foo(i):
    digits = "0123456789"
    start = time.perf_counter()
    if i == 0:
        result = "0"
    else:
        result = ""
        while i > 0:
            result = digits[i % 10] + result
            i = i // 10
    end = time.perf_counter()
    return end - start

sizes = [10**n for n in range(1, 8)]
times = []

foo(10)

for i in sizes:
    times.append(foo(i))

plt.plot(sizes, times, marker='o')
plt.xlabel('Входные данные (i)')
plt.ylabel('Время выполнения (секунды)')
plt.title('График зависимости времени выполнения функции foo(i)')
plt.xscale('log')
plt.grid(True)
plt.show()