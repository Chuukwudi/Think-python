# Exercise 3-1
def right_justify(s):
  while len(s) < 70:
    s = ' ' + s
  print(s)

right_justify('monty')

# Exercise 3-2
def do_twice(func, val):
  func(val)
  func(val)

def print_twice(text):
  print(text)
  print(text)

do_twice(print_twice, 'spam')

def do_four(func, val):
  do_twice(func, val)
  do_twice(func, val)

do_four(right_justify, 'hello')

# Exercise 3-3
row_base = '+ ' + '- '*4
col_base = '| ' + ' '*8

def draw_row(grid_no):
  print(row_base * grid_no, end='')
  print('+')

def draw_col(grid_no):
  print(col_base * grid_no, end='')
  print('|')

def draw_grid(grid_no):
  draw_row(grid_no)
  do_four(draw_col, grid_no)

def two_by_two_grid(grid_no):
  do_twice(draw_grid, grid_no)
  draw_row(grid_no)

two_by_two_grid(2)

def four_by_four_grid(grid_no):
	do_four(draw_grid, grid_no)
	draw_row(grid_no)

four_by_four_grid(4)