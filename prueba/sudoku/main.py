###### TEST 20 ######
###### TEST 20 ######
###### TEST 20 ######

import sys
sys.setrecursionlimit(90000)

puzzle = list()

def main():
    print("Ingrese la matriz a resolver")
    raw = input()[1:-1].split(", ")

    for line in raw:
        line = "".join(line[1:-1].split(" "))
        puzzle.append(list(line))

    solve()
    for line in puzzle:
        print(line)

def is_valid(row, col, num):
    for y in range(9):
        if int(puzzle[row][y]) == num and col != y:

            return False
    for x in range(9):
        if int(puzzle[x][col]) == num and row != x:
            return False
        
    small_row = row//3
    small_col = col//3

    for x in range(small_row*3, small_row*3 + 3):
        for y in range(small_col*3, small_col*3 + 3):
            if int(puzzle[x][y]) == num and (x, y) != (row, col):
                return False
    
    return True

def find_blank():
    for row in range(9):
        for col in range(9):
            if int(puzzle[row][col]) == 0:
                return (row, col)
    return None  

def solve():
    coords = find_blank()

    if not coords:
        return True
    else:
        row, col = coords
        for num in range(1, 10):
            if is_valid(row, col, num):
                puzzle[row][col] = num
                if solve():
                    return True
                puzzle[row][col] = 0
        return False

if __name__ == "__main__":
    main()