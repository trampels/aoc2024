"""Advent Of Code 2024 - day 4 puzzle 1
   character salat find XMAS """
#sample 18
import fileinput, re

res=0
# data, row, col, row offset, col offset
def XMAS(data,row,col,ro,co) -> int:
    if 'X' == data[row][col] and \
        'M' == data[row+ro][col+co] and \
        'A' == data[row+ro+ro][col+co+co] and \
        'S' == data[row+ro+ro+ro][col+co+co+co]:
        return 1
    return 0

def XMAS_Lookup(data,row,col,rows,cols) -> int:
    matches = 0
    pos = data[row][col]
    #print("XMAS(pos, row, col, rows, cols) ", pos, row, col, rows, cols)
    # look for XMAS is all 8 directions
    if row>=3: # look upwards
        if col>=3: matches+=XMAS(data, row, col, -1, -1) # look NW
        matches+=XMAS(data, row, col, -1, 0) # look N
        if cols-col>3: matches+=XMAS(data, row, col, -1, 1)  # look NE

    if col>=3: matches+=XMAS(data, row, col, 0, -1) # look W
    if cols-col>3: matches+=XMAS(data, row, col, 0, 1)  # look E

    if rows-row>3:
        if col>=3: matches+=XMAS(data, row, col, 1, -1) # look SW
        matches+=XMAS(data, row, col, 1, 0) # look S
        if cols-col>3: matches+=XMAS(data, row, col, 1, 1)  # look SE

    return matches

# main
datafile = open('input/input_04.txt', 'r')
lines = datafile.readlines()

for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == 'X':
            res += XMAS_Lookup(lines, row, col, len(lines), len(lines[0]))

print(res)