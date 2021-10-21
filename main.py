def draw_field(field):
  print('|'.join(map(str, [" ", 1, 2, 3])))

  for i, row in enumerate(field):
    print('|'.join([str(i + 1)] + row))

def check_draw(field):
  for row in field:
    if '_' in row:
      return False

  return True


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


field = [['_'] * 3 for _ in range(3)]
turn = True

draw_field(field)

while True:
  x = input("Введи номер по вертикали: ")
  y = input("Введи номер по горизонтали: ")

  if not (x.isdigit() and y.isdigit()):
    print('Здесь должны быть числа')
    continue
        
  x, y = map(lambda n: int(n) - 1, [x, y])

  if not (x in range(3) and y in range(3)):
    print('Промазал. Попробуй ещё разок')
    continue

  if field[y][x] != '_':
    print('Занято!')
    continue

  player = 'X' if turn else 'O'
  field[y][x] = player

  draw_field(field)

  if check_draw(field):
    print('Ничья...')
    break

  if check_victory(field, player):
    print(f'{player} выиграл!')

  turn = not turn