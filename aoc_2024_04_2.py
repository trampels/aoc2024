"""Advent Of Code 2024 - day 4 puzzle 2
   character salat find XMAS """
#sample 18
import fileinput, re

res=0
# data, row, col, row offset, col offset
def XMAS(data,row,col,rows,cols) -> int:
    mas = 0
    if row>0 and rows-row>1 and col>0 and cols-col>0:
        if 'M' == data[row-1][col-1] and 'S' == data[row+1][col+1]: mas+=1
        if 'M' == data[row-1][col+1] and 'S' == data[row+1][col-1]: mas+=1
        if 'M' == data[row+1][col-1] and 'S' == data[row-1][col+1]: mas+=1
        if 'M' == data[row+1][col+1] and 'S' == data[row-1][col-1]: mas+=1

    #print("XMAS(row, col, rows, cols) -> x", row, col, rows, cols, mas)
    if mas == 2:
        return 1
    return 0

# main
datafile = open('input/input_04.txt', 'r')
lines = datafile.readlines()

for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == 'A':
            res += XMAS(lines, row, col, len(lines), len(lines[0]))

print(res)