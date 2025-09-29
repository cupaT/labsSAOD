# Вариант 2. Рекурсивная функция для подсчёта количества вхождений элемента t в список some_list.
def recursive_count(some_list, t):
    # Если список пуст, возвращаем 0.
    if not some_list:
        return 0
    # Проверяем, равен ли первый элемент t, и рекурсивно считаем для оставшегося списка.
    return int(some_list[0] == t) + recursive_count(some_list[1:], t)

if __name__ == "__main__":
    sample_list = [1, 2, 3, 2, 4, 2, 5]
    t = 2
    count = recursive_count(sample_list, t)
    print(f"Element {t} appears {count} times in the list.")