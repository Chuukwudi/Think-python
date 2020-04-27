def do_twice(f):
	f()
	f()
	
def do_three(f):
    f()
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

#prints the horizontal part of the cell (+ - - - - )
def cell_row():
    print(' + ' + ' - ' * 4, end='')

#continues the horizontal part of the cell (+ - - - - +)
def another_cell_row():
    print(' + ' + ' - ' * 4, end=' +')

#this is (+ - - - - + - - - -+)
def row_for_two():
    cell_row()
    another_cell_row()

#this is (+ - - - - + - - - -+ - - - - + - - - -+)
def row_for_four():
    do_three(cell_row)
    another_cell_row()

#this is (|      )
def single_column():
    print(' | ' + '   ' * 4, end='')
#this is (|      |       |)
def two_columns():
    print('')
    do_three(single_column)
#this is (|      |       |      |       |)
def four_columns():
    do_three(single_column)
    do_twice(single_column)
    print('')

#here handles the top 2 boxes
def two_cell_boxes():
    row_for_two()
    do_four(two_columns)
    print('')

#here prints the 4 boxes, 2 above, 2 below)
def four_cell_boxes():
    do_twice(two_cell_boxes)
    row_for_two()
#here is to print 4 boxes on a row
def four_cell_rows():
    row_for_four()
    print('')
    do_four(four_columns)

#here is to print  4x2 boxes
def eight_cell_boxes():
    do_twice(four_cell_rows)
    row_for_four()

#here is to complete the 4x4 boxes
def sixteen_cell_boxes():
    do_four(four_cell_rows)
    row_for_four()

print('this is a 2x2 box')
four_cell_boxes()
print('')
print('this is a 4x4 box')
print('')
sixteen_cell_boxes()

