def read_file(file_name):
    global N, L, K
    # Открывает файл для чтения
    with open(file_name, "r") as file:
        first_line = file.readline().strip()
        # Считывает размер поля и количество фигур
        N, L, K = map(int, first_line.split())
        coordinates_const_figure = []
        # Считывает координаты статических фигур
        for _ in range(K):
            x, y = map(int, file.readline().strip().split())
            coordinates_const_figure.append((x, y))
    return coordinates_const_figure


def mark_moves(game_field, x, y, mark, moves_of_figure):
    blocked_cells = []
    # Помечает текущую ячейку на поле
    game_field[x][y] = mark
    blocked_cells.append((x, y))
    # Проверяет возможные ходы фигуры и помечает их
    for dx, dy in moves_of_figure:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and game_field[nx][ny] == 0:
            game_field[nx][ny] = mark
            blocked_cells.append((nx, ny))
    return blocked_cells


def backtrack(game_field, remaining_figures, moves_of_figure, start_x, start_y, solutions, current_solution,
              static_coordinates):
    # Проверяет, остались ли фигуры для размещения
    if remaining_figures == 0:
        full_solution = current_solution[:] + static_coordinates
        solutions.append(full_solution[:])
        return 1
    count = 0
    # Перебирает все возможные ячейки на поле
    for x in range(start_x, N):
        for y in range(start_y if x == start_x else 0, N):
            if game_field[x][y] == 0:
                # Помечает ячейку и рекурсивно вызывает backtrack
                blocked_cells = mark_moves(game_field, x, y, 1, moves_of_figure)
                current_solution.append((x, y))
                count += backtrack(game_field, remaining_figures - 1, moves_of_figure, x, y, solutions,
                                   current_solution, static_coordinates)
                # Убирает пометки с ячеек после возврата из рекурсии
                for bx, by in blocked_cells:
                    game_field[bx][by] = 0
                current_solution.pop()
        start_y = 0 # Сбрасывает начальную координату для следующей строки
    return count


def save_solutions(solutions, file_name="output.txt"):
    # Сохраняет решения в файл
    with open(file_name, "w") as file:
        if not solutions:
            file.write("no solutions\n") # Если решений нет
        else:
            for solution in solutions:
                # Заполняет пустые места (-1, -1) при необходимости
                while len(solution) < (L + K):
                    solution.append((-1, -1))
                file.write(" ".join(f"({x}, {y})" for x, y in solution) + "\n") # Записывает решение в файл


def print_board(game_field):
    # Создание пустого игрового поля для отображения
    board = [['0' for _ in range(N)] for _ in range(N)]

    # Отметим статические фигуры на доске
    for x in range(N):
        for y in range(N):
            if game_field[x][y] == 1:
                board[x][y] = '#' # Отметка статической фигуры
                # Отмечаем атакующие клетки
                for dx, dy in moves_of_figure:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        board[nx][ny] = '*'

    # Проверяем, какие клетки атакуются другими фигурами
    for x in range(N):
        for y in range(N):
            if game_field[x][y] == 1:
                continue
            for dx, dy in moves_of_figure:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and game_field[nx][ny] == 1:
                    board[x][y] = '*'

    # Выводим доску на экран
    for row in board:
        print(' '.join(row))


def main():
    # Считываем координаты статических фигур из файла
    coordinates_const_figure = read_file("input.txt")
    game_field = [[0 for _ in range(N)] for _ in range(N)]
    global moves_of_figure
    # Определяем возможные ходы для фигур
    moves_of_figure = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (3, 1), (3, -1), (-3, 1), (-3, -1),
        (1, 3), (1, -3), (-1, 3), (-1, -3)]

    static_coordinates = coordinates_const_figure
    # Помечаем статические фигуры на игровом поле
    for x, y in static_coordinates:
        mark_moves(game_field, x, y, 1, moves_of_figure)

    solutions = []
    # Запускаем функцию backtrack для поиска решений
    result = backtrack(game_field, L, moves_of_figure, 0, 0, solutions, [], static_coordinates)
    print(f"Размер доски: {N}, Нужно поставить фигур: {L}, Уже стоят фигур: {K}")
    print()

    if solutions:
        chosen_solution = solutions[0] # Выбираем первое найденное решение
        for x, y in chosen_solution:
            if (x, y) != (-1, -1):
                mark_moves(game_field, x, y, 1, moves_of_figure)

    # Создаем поле для вывода
    output_game_field = [[0 for _ in range(N)] for _ in range(N)]
    for x, y in static_coordinates:
        output_game_field[x][y] = 1

    placed_figures = 0
    # Отмечаем размещенные фигуры на поле
    for x, y in chosen_solution:
        if placed_figures < L and (x, y) != (-1, -1):
            output_game_field[x][y] = 1
            placed_figures += 1

    print(f'    Доска')
    print_board(output_game_field)
    print("Количество комбинаций:", result)
    save_solutions(solutions)
    print("Решения сохранены в файл 'output.txt'.")


if __name__ == "__main__":
    main()
