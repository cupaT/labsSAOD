#2
import time
import matplotlib.pyplot as plt
import random

def all_unique_naive(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

def all_unique_set(lst):
    return len(lst) == len(set(lst))

sizes = [100, 200, 400, 800, 1600, 3200, 6400]
naive_times = []
set_times = []

all_unique_naive(list(range(100)))
all_unique_set(list(range(100)))

for size in sizes:
    test_list = list(range(size))
    random.shuffle(test_list)

    start = time.perf_counter()
    all_unique_naive(test_list)
    end = time.perf_counter()
    naive_times.append(end - start)

    start = time.perf_counter()
    all_unique_set(test_list)
    end = time.perf_counter()
    set_times.append(end - start)

plt.plot(sizes, naive_times, marker='o', label='Наивный (O(n²))')
plt.plot(sizes, set_times, marker='s', label='Множество (O(n))')
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (сек)")
plt.title("Сравнение алгоритмов проверки уникальности")
plt.legend()
plt.grid(True)
plt.show()