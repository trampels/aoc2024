"""Advent Of Code 2024 - day 1 puzzle 2
similarity score, how often each number from the left list appears in the right list"""
import fileinput

data1 = []
data2 = []
with fileinput.input(files="input/input_01.txt", encoding="utf-8") as f:
    for line in f:
        values = line.split()
        data1.append(int(values[0]))
        data2.append(int(values[1]))
res=0
while 0<len(data1):
    val = int(data1.pop(0))
    res += val*sum(1 for n in data2 if n == val )
print(res)