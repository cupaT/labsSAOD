#5
import time
import matplotlib.pyplot as plt

sizes = [10_000, 20_000, 40_000, 80_000, 160_000, 320_000]
times_list = []
times_set = []

for size in sizes:
    data_list = list(range(size))
    data_set = set(data_list)
    target = -1

    # Для списка
    start = time.perf_counter()
    _ = target in data_list
    end = time.perf_counter()
    times_list.append(end - start)

    # Для множества
    start = time.perf_counter()
    _ = target in data_set
    end = time.perf_counter()
    times_set.append(end - start)

plt.plot(sizes, times_list, marker='o', label='in для списка')
plt.plot(sizes, times_set, marker='s', label='in для множества')
plt.xlabel('Размер структуры данных')
plt.ylabel('Время выполнения операции in (секунды)')
plt.title('Сравнение производительности оператора in для списка и множества')
plt.legend()
plt.grid(True)
plt.show()