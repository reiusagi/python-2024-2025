#def listofstars(inputlist):
#    for var in inputlist:
#        print("*"*var)
from itertools import count

#listofstars([1,2,3,4,5])


#def even_numbers(inputlist):
#    for var in inputlist:
#        if var % 2 == 0:
#            print(var)


#even_numbers([1,2,3,4,5])

#def length_of_longest(inputlist):
#    longest = inputlist[0]
#    for  i in range(1, len(inputlist)):
#        if len(inputlist[i]) > len(longest):
#            longest = inputlist[i]
#    print(longest)

#length_of_longest(["first", "second", "fourth", "eleventh"])


#def formatted(mylist):
#    newlist = []
#    for var in mylist:
#        newlist.append(f"{var:.2f}")
#    print(newlist)

#formatted([1.234, 0.3333, 0.11111, 3.446])

#def everything_reversed(mylist):
#    newlist = []
#    iter = len(mylist)-1
#    while iter >= 0:
#            newlist.append(mylist[iter][::-1])
#            iter -= 1
#    return newlist

#my_list = ["Hi", "there", "example", "one more"]
#new_list = everything_reversed(my_list)
#print(new_list)

def count_matching_elements(list1,element):
    sayac = 0
    for row in list1:
        if element in row:
            sayac = sayac + row.count(element)
    return sayac
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 0))

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]
def print_grid(sudoku):
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print()

print_grid(sudoku)

def row_correct(sudoku: list,row_no: int):
    row =sudoku[row_no]
    rowcontrol = True
    for var in row:
        if var>0 and row.count(row_no)>0:
            rowcontrol = False
            break
    return rowcontrol

print(row_correct(sudoku,0))
print(row_correct(sudoku,1))


def column_correct(sudoku: list, column_no: int):
    column = [row[column_no] for row in sudoku]  # List comprehension ile sütunu al
    columncontrol = True

    for var in column:
        if var > 0 and column.count(var) > 1:  # Aynı sayı birden fazla varsa yanlış
            columncontrol = False
            break

    return columncontrol

print(column_correct(sudoku, 0))
print(column_correct(sudoku, 1))

def small_matrix_correct(sudoku,i,j):
    small_matrix = []
    for row in range (i,i+3):
        for col in range (j,j+3):
            small_matrix.append(sudoku[row][col])
    small_matrix_check =True
    for var in small_matrix:
        if small_matrix.count(var)>1 and var>0:
            small_matrix_check = False
            break

    return small_matrix_check

def sudoku_grid_correct(sudoku: list):
    grid_control = True
    for i in range(len(sudoku)):
        if row_correct(sudoku,i) == False:
            return False
    for i in range(len(sudoku)):
        if column_correct(sudoku,i) == False:
            return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            if small_matrix_correct(sudoku,i,j) == False:
                return False

    return True

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))



