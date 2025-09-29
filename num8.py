# Проверяет, можно ли поставить число num в ячейку (row, col) мини-судоку.
# Число должно быть уникальным в строке, столбце и квадрате 2x2.
def is_valid(matrix, row, col, num):
    # Проверяем строку и столбец
    for x in range(4):
        if matrix[row][x] == num or matrix[x][col] == num:
            return False
    # Проверяем квадрат 2x2
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if matrix[i][j] == num:
                return False
    return True

# Находит первую пустую ячейку (со значением 0) в мини-судоку.
def find_empty(matrix):
    # Возвращает координаты (i, j) или None, если пустых ячеек нет.
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return i, j
    return None

# Рекурсивная функция для решения мини-судоку 4x4.
def solve_sudoku(matrix):
    empty = find_empty(matrix)
    # Базовый случай: если нет пустых ячеек, решение найдено
    if not empty:
        return True
    row, col = empty
    # Рекурсивный случай: пробуем поставить каждое число от 1 до 4
    for num in range(1, 5):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            # Откат (backtracking)
            matrix[row][col] = 0
    # Если ни одно число не подошло, возвращаем False — решения нет
    return False

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 0],
        [3, 0, 0, 4]
    ]
    if solve_sudoku(sudoku):
        for row in sudoku:
            print(row)
    else:
        print("Решения нет")