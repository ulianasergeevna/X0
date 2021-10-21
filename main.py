def draw_field(field):
    print()
    print('|'.join(map(str, [" ", 1, 2, 3])))

    for i, row in enumerate(field):
        print('|'.join([str(i + 1)] + row))

    print()


def check_draw(field):
    for row in field:
        if '_' in row:
            return False

    return True


def create_field():
    return [['_'] * 3 for _ in range(3)], True


def check_victory(field, player):
    rows = [row for row in field]
    diagonals = [
        [field[i][i] for i in range(len(field))],
        [field[i][len(field) - i - 1] for i in range(len(field))],
    ]
    columns = [[field[i][j] for i in range(len(field))] for j in range(len(field))]

    for sequence in rows + columns + diagonals:
        if len(list(filter(lambda x: x != player, sequence))) == 0:
            return True


field, turn = create_field()
start_new = False
draw_field(field)

while True:
    x = input("Введи номер столбца: ")
    y = input("Введи номер строки: ")

    if not (x.isdigit() and y.isdigit()):
        print('Здесь должны быть числа\n')
        continue

    x, y = map(lambda n: int(n) - 1, [x, y])

    if not (x in range(3) and y in range(3)):
        print('Промазал. Попробуй ещё разок\n')
        continue

    if field[y][x] != '_':
        print('Занято!')
        continue

    player = 'X' if turn else 'O'
    field[y][x] = player

    draw_field(field)

    turn = not turn

    if check_draw(field):
        print('Победила дружба! =)\n')
        start_new = input("Сыграть ещё? (+/-)") == '+'

        if not start_new:
            break

    if check_victory(field, player):
        print(f'{player} выиграл!\n')
        start_new = input("Сыграть ещё? (+/-)") == '+'

        if not start_new:
            break

    if start_new:
        field, turn = create_field()
        draw_field(field)
        start_new = False