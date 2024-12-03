"""Advent Of Code 2024 - day 1 puzzle 1
   corrupted code, summ all products mul(v1, v1)
   do() enables, don't() disables next mul, default enabled """
#sample 48 (2*4 + 8*5)
import fileinput, re

res=0
do=True
with fileinput.input(files="input/input_03.txt", encoding="utf-8") as f:
    for line in f:
        for op in re.findall(r"mul\(\d+\,\d+\)|do\(\)|don't\(\)", line):
            cmd = re.split(r'[,\)\(]', op)
            if 'mul' == cmd[0]:
                if do: res += int(cmd[1])*int(cmd[2])
            elif 'do' == cmd[0]: do = True
            elif "don't" == cmd[0]: do = False
print(res)