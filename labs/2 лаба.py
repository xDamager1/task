def read_input(filename: str) -> tuple:
    # Считывает данные из файла
    with open(filename) as f:
        # Читает размеры доски и количество фигур
        N, L, K = map(int, f.readline().strip().split())
        # Читает позиции уже установленных фигур
        pieces = [tuple(map(int, f.readline().strip().split())) for _ in range(K)]
    return N, L, K, pieces


def mark_attacks(x: int, y: int, board: list):
    # Определяет возможные движения пони
    possible_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (3, 1), (3, -1), (-3, 1), (-3, -1),
        (1, 3), (1, -3), (-1, 3), (-1, -3)
    ]

    # Помечает клетки, которые могут быть атакованы
    for dx, dy in possible_moves:
        if 0 <= x + dx < n and 0 <= y + dy < n:
            board[x + dx][y + dy] = '*'
    board[x][y] = '#'  # Помечает позицию пони


def reset_tiles(x: int, y: int, board: list):
    # Сбрасывает позицию пони
    board[x][y] = '0'  # Возвращает клетку к исходному состоянию

    # Убирает метки атак
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                board[i][j] = '0'

    # Восстанавливает атаки для оставшихся пони
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                mark_attacks(i, j, board)


def is_valid_position(x: int, y: int, board) -> bool:
    # Проверяет, можно ли установить пони в заданной позиции
    possible_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (3, 1), (3, -1), (-3, 1), (-3, -1),
        (1, 3), (1, -3), (-1, 3), (-1, -3)
    ]

    # Проверяет, не находится ли позиция под атакой
    for dx, dy in possible_moves:
        if 0 <= x + dx < n and 0 <= y + dy < n:
            if board[x + dx][y + dy] == '#' or board[x][y] == '#':
                return False
    return True  # Позиция допустима


def place_knights(x: int, y: int, remaining: int, current_solution: list, existing_pieces: list, board: list,
                  cache: set):
    # Если все пони установлены, сохраняем решение
    if remaining == 0:
        sorted_solution = tuple(sorted(current_solution))
        if sorted_solution not in cache:  # Проверка на уникальность решения
            cache.add(sorted_solution)
            f.write(f"({', '.join(map(str, current_solution + existing_pieces))})\n")
        return

    # Цикл по всем возможным позициям для размещения пони
    for i in range(x, n):
        for j in range(y if i == x else 0, n):
            if is_valid_position(i, j, board):  # Проверка на допустимость позиции
                current_solution.append((i, j))  # Добавляем текущую позицию в решение
                mark_attacks(i, j, board)  # Помечаем атакуемые клетки
                place_knights(i, j, remaining - 1, current_solution, existing_pieces, board, cache)  # Рекурсивный вызов
                reset_tiles(i, j, board)  # Сброс состояния клеток
                current_solution.pop()  # Удаление последней позиции из текущего решения


def print_board(board: list):
    # Печатает доску на экран
    for row in board:
        print(' '.join(row))


def main():
    global n, l, f, const_pieces
    n, l, k, const_pieces = read_input('Input.txt')  # Чтение данных из файла
    board = [['0'] * n for _ in range(n)]  # Инициализация доски

    # Помечаем уже установленные фигуры
    for cx, cy in const_pieces:
        mark_attacks(cx, cy, board)

    with open('output.txt', 'w') as f:
        cache = set()  # Множество для хранения уникальных решений
        print(f'Размер доски: {n}, Нужно поставить фигур: {l}, Уже стоят фигур: {k}')  # Вывод информации
        place_knights(0, 0, l, [], const_pieces, board, cache)  # Начинаем размещение пони

    # Чтение результатов из выходного файла
    with open('output.txt', 'r+') as f:
        content = f.readline()
        if not content:
            f.write('no solution')  # Если решений нет
        else:
            coordinates = list(map(int, content.replace('(', '').replace(')', '').strip().split(', ')))
            placements = [(coordinates[i], coordinates[i + 1]) for i in range(0, len(coordinates), 2)]
            placements.sort()  # Сортировка размещений

            # Помечаем атакующие клетки на доске
            for x, y in placements:
                mark_attacks(x, y, board)

            print_board(board)  # Выводим финальную доску

# Условие для запуска программы
if __name__ == '__main__':
    main()