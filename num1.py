import random
import time
import matplotlib.pyplot as plt

# Функция сортировки выбором: последовательно находит минимум и ставит его в начало неотсортированной части массива.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Рекурсивная реализация быстрой сортировки: делит массив относительно опорного элемента (pivot).
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# Функция для измерения времени выполнения алгоритма сортировки на копии массива.
def time_sort(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_func(arr_copy)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    sizes = [100 * i for i in range(1, 21)]

    timings_random_sel, timings_random_quick = [], []
    timings_sorted_sel, timings_sorted_quick = [], []
    timings_reversed_sel, timings_reversed_quick = [], []

    for n in sizes:
        random_list = [random.randint(0, 10 ** 6) for _ in range(n)]
        sorted_list = sorted(random_list)
        reversed_list = sorted(random_list, reverse=True)

        timings_random_sel.append(time_sort(selection_sort, random_list))
        timings_random_quick.append(time_sort(quick_sort, random_list))
        timings_sorted_sel.append(time_sort(selection_sort, sorted_list))
        timings_sorted_quick.append(time_sort(quick_sort, sorted_list))
        timings_reversed_sel.append(time_sort(selection_sort, reversed_list))
        timings_reversed_quick.append(time_sort(quick_sort, reversed_list))

    # График для случайного массива
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, timings_random_sel, 'o-', label='Selection Sort')
    plt.plot(sizes, timings_random_quick, 'o-', label='Quick Sort')
    plt.title("Случайный массив")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # График для отсортированного массива
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, timings_sorted_sel, 'o-', label='Selection Sort')
    plt.plot(sizes, timings_sorted_quick, 'o-', label='Quick Sort')
    plt.title("Отсортированный массив")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # График для обратно отсортированного массива
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, timings_reversed_sel, 'o-', label='Selection Sort')
    plt.plot(sizes, timings_reversed_quick, 'o-', label='Quick Sort')
    plt.title("Обратно отсортированный массив")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()