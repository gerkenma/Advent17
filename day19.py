grid = []
f = open("day19.txt", "r")
for line in f:
  if len(line) > 1:
    gridline = list(line[:-1])
    grid.append(gridline)

def is_valid_move(fx, fy):
  return (
    fx >= 0 and
    fx < len(grid[0]) and
    fy >=0 and
    fy < len(grid) and
    grid[y + dy][x + dx] != ' ')

y = 0
x = grid[0].index("|")
dy = 1
dx = 0
s = ""
sc = 1
while True:
  if not is_valid_move(x + dx, y + dy):
    if dy != 0:
      dy = 0
      dx = -1
      if not is_valid_move(x + dx, y + dy):
        dx = 1
        if not is_valid_move(x + dx, y + dy):
          break
    else:
      dy = -1
      dx = 0
      if not is_valid_move(x + dx, y + dy):
        dy = 1
        if not is_valid_move(x + dx, y + dy):
          break
  if grid[y + dy][x + dx].isalpha():
    s += grid[y + dy][x + dx]
  y += dy
  x += dx
  sc += 1
print s
print sc