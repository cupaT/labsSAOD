# Рекурсивная функция для вычисления n-го числа Трибоначчи
def tribonacci(n):
    # Базовые случаи:
    # Если n == 0 или n == 1, возвращаем 0
    if n == 0 or n == 1:
        return 0
    # Если n == 2, возвращаем 1
    elif n == 2:
        return 1
    # Если n > 2, возвращаем сумму трёх предыдущих чисел ряда
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

if __name__ == "__main__":
    # Первые 10 чисел ряда Трибоначчи
    for i in range(10):
        print(f"tribonacci({i}) = {tribonacci(i)}")