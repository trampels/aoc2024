"""Advent Of Code 2024 - day 1 puzzle 1
   sum of distances in sorted lists"""
import fileinput

data1 = []
data2 = []
with fileinput.input(files="input/input_01.txt", encoding="utf-8") as f:
    for line in f:
        values = line.split()
        data1.append(int(values[0]))
        data2.append(int(values[1]))
res=0
data1.sort()
data2.sort()
while 0<len(data1):
    res += abs(int(data1.pop(0)) - int(data2.pop(0)))
print(res)