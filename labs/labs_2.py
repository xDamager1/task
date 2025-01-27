# Функция для чтения данных из файла
def read_file(file_name):
    global N, L, K
    with open(file_name, "r") as file:
        first_line = file.readline().strip()  
        N, L, K = map(int, first_line.split())
        coordinates_const_figure = []
        for _ in range(K):
            x, y = map(int, file.readline().strip().split())
            coordinates_const_figure.append((x, y))
    return coordinates_const_figure

# Функция для пометки клеток, которые блокируются из-за хода фигуры
def mark_moves(game_field, x, y, moves_of_figure):
    blocked_cells = []  # Список заблокированных клеток
    game_field[x][y] = -1  # Помечаем клетку с фигурой как заблокированную
    blocked_cells.append((x, y))
    for dx, dy in moves_of_figure:  # Для каждого возможного хода фигуры
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:  # Проверяем, что новые координаты внутри доски
            if game_field[nx][ny] != -1:  # Если клетка еще не заблокирована
                game_field[nx][ny] += 1  # Помечаем, что сюда можно ходить
                blocked_cells.append((nx, ny))
    return blocked_cells

# Функция для снятия блокировки с клеток после проверки текущего решения
def unmark_moves(game_field, blocked_cells):
    for bx, by in blocked_cells:
        if game_field[bx][by] > 0:  # Если клетка была доступной для хода
            game_field[bx][by] -= 1  # Уменьшаем ее "заблокированность"
        elif game_field[bx][by] == -1:  # Если клетка была занята фигурой
            game_field[bx][by] = 0  # Снимаем блокировку

# Функция для поиска всех возможных решений с помощью рекурсии (обратного хода)
def backtrack(game_field, remaining_figures, moves_of_figure, start_x, start_y, solutions, current_solution,
              static_coordinates):
    if remaining_figures == 0:
        full_solution = current_solution + static_coordinates  # Составляем полное решение
        solutions.append(full_solution)  # Добавляем решение в список
        return 1  # Возвращаем 1, чтобы подсчитать количество решений
    count = 0
    for x in range(start_x, N):
        for y in range(start_y if x == start_x else 0, N):
            if game_field[x][y] == 0:  # Если клетка свободна (не занята)
                blocked_cells = mark_moves(game_field, x, y, moves_of_figure)  # Блокируем клетки, которые не доступны
                current_solution.append((x, y))
                count += backtrack(game_field, remaining_figures - 1, moves_of_figure, x, y, solutions,
                                   current_solution, static_coordinates)  # Рекурсивно пробуем разместить следующую фигуру
                unmark_moves(game_field, blocked_cells)  # Снимаем блокировки
                current_solution.pop()
        start_y = 0
    return count

# Функция для сохранения решений в файл
def save_solutions(solutions, file_name="output.txt"):
    with open(file_name, "w") as file:
        if not solutions:
            file.write("no solutions\n")
        else:
            for solution in solutions:  # Проходим по всем решениям
                while len(solution) < (L + K):  # Если решения не хватает до полного числа фигур
                    solution.append((-1, -1))  # Добавляем пустые клетки
                file.write(" ".join(f"({x}, {y})" for x, y in solution) + "\n")

# Функция для вывода доски с обозначениями фигур и доступных клеток
def print_board(game_field, moves_of_figure):
    for x in range(N):
        for y in range(N):
            if game_field[x][y] == 1:  # Если в клетке есть фигура
                game_field[x][y] = "#"
                for dx, dy in moves_of_figure:  # Помечаем клетки, на которые фигура может ходить
                    if 0 <= x+dx < N and 0 <= y+dy < N:
                        game_field[x+dx][y+dy] = "*"
    
    # Выводим доску
    for row in game_field:
        print(*row)  # Выводим каждую строку доски

# Основная функция
def main():
    coordinates_const_figure = read_file("Input.txt")
    game_field = [[0 for _ in range(N)] for _ in range(N)]
    global moves_of_figure
    moves_of_figure = [ 
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (3, 1), (3, -1), (-3, 1), (-3, -1),
        (1, 3), (1, -3), (-1, 3), (-1, -3)]

    static_coordinates = coordinates_const_figure  # Список координат статичных фигур
    for x, y in static_coordinates:  # Для каждой статичной фигуры блокируем клетки
        mark_moves(game_field, x, y, moves_of_figure)

    solutions = []  # Список для хранения решений
    result = backtrack(game_field, L, moves_of_figure, 0, 0, solutions, [], static_coordinates)  # Поиск решений
    print(f"Размер доски: {N}, Нужно поставить фигур: {L}, Уже стоят фигур: {K}")
    print()

    if solutions:
        chosen_solution = solutions[0]  # Выбираем первое решение
        for x, y in chosen_solution:
            if (x, y) != (-1, -1):
                mark_moves(game_field, x, y, moves_of_figure)  # Помечаем клетки, занятые фигурами

    output_game_field = [[0 for _ in range(N)] for _ in range(N)]  # Создаем пустую доску для вывода
    for x, y in static_coordinates:  # Размещаем статичные фигуры на доске
        output_game_field[x][y] = 1

    placed_figures = 0  # Счетчик размещенных фигур
    for x, y in chosen_solution:  # Размещаем остальные фигуры
        if placed_figures < L and (x, y) != (-1, -1):
            output_game_field[x][y] = 1
            placed_figures += 1

    print(f'    Итоговая доска')
    print_board(output_game_field, moves_of_figure)  # Выводим доску с фигурами и возможными ходами
    print("Количество комбинаций:", result)
    save_solutions(solutions)
    print("Решения сохранены в файл 'output.txt'.")


if __name__ == "__main__":
    main()
