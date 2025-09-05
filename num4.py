#4
import time
import matplotlib.pyplot as plt

sizes = [100000, 200000, 400000, 800000, 1600000, 3200000]
del_times_list = []
del_times_dict = []

for size in sizes:
    # Для списка
    lst = list(range(size))
    start = time.perf_counter()
    for i in range(size):
        del lst[-1]
    end = time.perf_counter()
    del_times_list.append(end - start)

    # Для словаря
    dct = {i: None for i in range(size)}
    start = time.perf_counter()
    for i in range(size):
        del dct[i]
    end = time.perf_counter()
    del_times_dict.append(end - start)

plt.plot(sizes, del_times_list, marker='o', label='del для списка')
plt.plot(sizes, del_times_dict, marker='s', label='del для словаря')
plt.xlabel('Размер структуры данных')
plt.ylabel('Время удаления всех элементов (секунды)')
plt.title('Сравнение производительности del для списка и словаря')
plt.legend()
plt.grid(True)
plt.show()